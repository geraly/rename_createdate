import argparse
import json
import os.path
import os
import re
import subprocess
import tempfile

PATH_EXIFTOOL = "G:\\tools\\exiftool\\exiftool.exe"


def rename_createdate(target_path: os.path, dry_run=True):

    # 一時ファイルを作成してファイルパスを書き込む。
    # tempfile.TemporaryFile()だとリソース解放時に自動で削除してくれるが、
    # exiftoolから参照できないのでtempfile.mkstemp()を使う。
    temp_file_fp, temp_file_path = tempfile.mkstemp(prefix='exiftool_')
    os.write(temp_file_fp, target_path.encode())
    os.close(temp_file_fp)

    # exiftoolを用いて指定フォルダ配下のファイルについて
    # DateTimeOriginal, CreationDate, CreateDateを取得する
    cmd = [PATH_EXIFTOOL, '-r', '-json', '-charset', 'FileName=UTF8',
           '-DateTimeOriginal', '-CreationDate', '-CreateDate', '-@', temp_file_path]
    try:
        exif_tool_out = subprocess.run(
            cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    finally:
        os.remove(temp_file_path)

    if len(exif_tool_out.stdout.decode()) == 0:
        return
    targets = json.loads(exif_tool_out.stdout.decode())
    # /と\が混在するため'SourceFile'をos.pathに変換しておく。
    for target in targets:
        target['SourceFile'] = os.path.normpath(target['SourceFile'])

    # 新しいファイル名を決定する
    # DateTimeOriginalがあればそれを、CreateDateがあればそれを用いる
    # 新しいファイル名は YYYY-MM-DD_hh-mm-dd.元のファイルの拡張子 とする
    pattern = re.compile('(\d{4}):(\d{2}):(\d{2}) (\d{2}):(\d{2}):(\d{2})')
    # renameで上書きしないようにするため、同じファイルが作られないか確認する
    # key: 新しいファイル名
    # value: 古いファイルパス
    files = {}
    for target in targets:
        if 'DateTimeOriginal' in target:
            date = target['DateTimeOriginal']
        elif 'CreationDate' in target:
            date = target['CreationDate']
        elif 'CreateDate' in target:
            date = target['CreateDate']
        else:
            print(
                f"{target['SourceFile']}: DateTimeOriginal and CreateDate not found.")
            continue
        # YYYY:MM:DD hh:mm:ss       -> YYYY-MM-DD_hh-mm-ss
        # YYYY:MM:DD hh:mm:ss+aa:bb -> YYYY-MM-DD_hh-mm-ss
        m = re.search(pattern, date)
        if m is None:
            raise Exception(
                f"{target['SourceFile']}: datetime format is invalid. ({date})")
        ext = os.path.splitext(target['SourceFile'])[1]
        new_file = f"{m.group(1)}-{m.group(2)}-{m.group(3)}_{m.group(4)}-{m.group(5)}-{m.group(6)}{ext}"
        if new_file in files:
            raise Exception(
                f"{target['SourceFile']}: same datetime file exists. ({files[new_file]})")

        files[new_file] = target['SourceFile']

    # リネームする
    for new_file, current_file_path in files.items():
        dir_path = os.path.dirname(current_file_path)
        new_file_path = os.path.join(dir_path, new_file)
        if not dry_run:
            os.rename(current_file_path, new_file_path)
        print(f"{current_file_path} -> {new_file_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='ファイル内の管理情報をもとにファイル名をファイル作成日に変更する。')
    parser.add_argument('path', help='処理対象のファイルパス')
    parser.add_argument('--execute', action='store_true', help='ファイル名を変更する。')

    args = parser.parse_args()

    print(f'target path: {os.path.normpath(args.path)}')
    if args.execute:
        print('mode: execute')
    else:
        print('mode: dry-run')

    if not os.path.exists(PATH_EXIFTOOL):
        print('Error: exiftool not found. Set PATH_EXIFTOOL to correct path.')
        quit(1)

    rename_createdate(args.path, dry_run=(not args.execute))

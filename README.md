# rename_createdate

## 概要

ファイル内の管理情報をもとにファイル名をファイル作成日に変更する。

## 詳細

exiftoolを用いて指定したフォルダ配下（サブフォルダを含む）のファイルについてファイル名を"YYYY-MM-DD_hh-mm-ss.元の拡張子"の形で作成日時に変更する。  
作成日時はDateTimeOriginal, CreationDate, CreateDateを順番に確認して存在するものを用いる。  
いずれも参照できない場合はそのファイルは処理しない。

同一日時かつ拡張子のファイルが複数ある場合はエラーとし、終了する。どのファイルもリネームされない。

なお、exiftoolのグループ指定はしていないので、メディアによって参照するグループが異なる。

* 例1: DateTimeOriginalの場合、JPEG, HEICはEXIFグループを、MTSはH264グループを参照するものがあった。
* 例2: CreateDateの場合、JPEGはEXIFグループを、MOVはQuickTimeグループを、HEICはXMPグループを参照するものがあった。

exiftoolが処理対象のパスに日本語を含むと正しく認識しないため、パスを一時ファイルに記載してそのファイルをexiftoolへ渡している。

## 使い方 (Windowsの場合)

### 準備

1. exiftoolをダウンロードし、適切なパスに展開する。

    [ExifTool by Phil Harvey](https://exiftool.org/)

2. exiftool(-k).exeをexiftool.exeにリネームする。
3. rename_createdate.pyのPATH_EXIFTOOLを配置したパスに置き換える。

### 実行

```plain
python .\rename_createdate.py path_to_directory
python .\rename_createdate.py --execute path_to_directory
```

## Usage

```plain
python .\rename_createdate.py -h
usage: rename_createdate.py [-h] [--execute] path

ファイル内の管理情報をもとにファイル名をファイル作成日に変更する。

positional arguments:
  path        処理対象のファイルパス

options:
  -h, --help  show this help message and exit
  --execute   ファイル名を変更する。
```

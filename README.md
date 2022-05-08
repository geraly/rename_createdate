# rename_createdate

## �T�v

�t�@�C�����̊Ǘ��������ƂɃt�@�C�������t�@�C���쐬���ɕύX����B

## �ڍ�

exiftool��p���Ďw�肵���t�H���_�z���i�T�u�t�H���_���܂ށj�̃t�@�C���ɂ��ăt�@�C������"YYYY-MM-DD_hh-mm-ss.���̊g���q"�̌`�ō쐬�����ɕύX����B  
�쐬������DateTimeOriginal, CreationDate, CreateDate�����ԂɊm�F���đ��݂�����̂�p����B  
��������Q�Ƃł��Ȃ��ꍇ�͂��̃t�@�C���͏������Ȃ��B

����������g���q�̃t�@�C������������ꍇ�̓G���[�Ƃ��A�I������B�ǂ̃t�@�C�������l�[������Ȃ��B

�Ȃ��Aexiftool�̃O���[�v�w��͂��Ă��Ȃ��̂ŁA���f�B�A�ɂ���ĎQ�Ƃ���O���[�v���قȂ�B

* ��1: DateTimeOriginal�̏ꍇ�AJPEG, HEIC��EXIF�O���[�v���AMTS��H264�O���[�v���Q�Ƃ�����̂��������B
* ��2: CreateDate�̏ꍇ�AJPEG��EXIF�O���[�v���AMOV��QuickTime�O���[�v���AHEIC��XMP�O���[�v���Q�Ƃ�����̂��������B

exiftool�������Ώۂ̃p�X�ɓ��{����܂ނƐ������F�����Ȃ����߁A�p�X���ꎞ�t�@�C���ɋL�ڂ��Ă��̃t�@�C����exiftool�֓n���Ă���B

## �g���� (Windows�̏ꍇ)

### ����

1. exiftool���_�E�����[�h���A�K�؂ȃp�X�ɓW�J����B

    [ExifTool by Phil Harvey](https://exiftool.org/)

2. exiftool(-k).exe��exiftool.exe�Ƀ��l�[������B
3. rename_createdate.py��PATH_EXIFTOOL��z�u�����p�X�ɒu��������B

### ���s

```plain
python .\rename_createdate.py path_to_directory
python .\rename_createdate.py --execute path_to_directory
```

## Usage

```plain
python .\rename_createdate.py -h
usage: rename_createdate.py [-h] [--execute] path

�t�@�C�����̊Ǘ��������ƂɃt�@�C�������t�@�C���쐬���ɕύX����B

positional arguments:
  path        �����Ώۂ̃t�@�C���p�X

options:
  -h, --help  show this help message and exit
  --execute   �t�@�C������ύX����B
```

#!/bin/bash
version=`cat version.txt`
create-version-file metadata.yml --outfile file_version_info.txt --version $version

pyinstaller --onefile --icon=icon.ico --windowed pyEMG.py --name=pyEMG --add-data "version.txt;." --add-data "icon.ico;." -w --version-file=file_version_info.txt

mkdir -p dist/pyEMG/games && cp -avr games dist/pyEMG
mv dist/pyEMG.exe dist/pyEMG
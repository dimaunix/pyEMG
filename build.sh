#!/bin/bash
create-version-file metadata.yml --outfile file_version_info.txt --version $1

pyinstaller --onefile --windowed pyEMG.py --name=pyEMG -w --version-file=file_version_info.txt

mkdir -p dist/pyEMG/games && cp -avr games dist/pyEMG/games
mv dist/pyEMG.exe dist/pyEMG
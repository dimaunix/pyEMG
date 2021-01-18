#!/bin/bash
join_by() { local IFS="$1"; shift; echo "$*"; }
var=global
version=`cat version.txt`
type="$1"

readarray -td. array_version <<<"$version"
if [ "$type" = "major" ] ;
  then
    array_version[0]="$((array_version[0]+1))"
    array_version[1]=0
    array_version[2]=0
    array_version[3]=0
elif [ "$type" = "minor" ];
  then
    array_version[1]="$((array_version[1]+1))"
    array_version[2]=0
    array_version[3]=0
elif [ "$type" = "hotfix" ];
  then
    array_version[2]="$((array_version[2]+1))"
    array_version[3]=0
elif [ "$type" = "patch" ];  then array_version[3]="$((array_version[3]+1))"
else
    readarray -td. array_version <<<"$type"
fi

new_version=$(join_by "." ${array_version[@]})
echo $new_version > version.txt

create-version-file metadata.yml --outfile file_version_info.txt --version $new_version

pyinstaller --onefile -w --additional-hooks-dir "hooks" --icon="resources/icon.ico" pyEMG.py --name=pyEMG --add-data "version.txt;." --add-data "resources;resources" --version-file=file_version_info.txt

echo "preparing version for packaging..."
mkdir -p dist/pyEMG/games && cp -avr games dist/pyEMG
mv dist/pyEMG.exe dist/pyEMG
cd dist

echo "packaging version into archive..."
archive_name="pyEMG_windows_x64_v${new_version}.zip"
7z a $archive_name pyEMG

echo "your new version: $archive_name"
#!/bin/bash
# assume running from AnoDesign
# run like sh scripts/copy_files.sh

[ -d /Volumes/Develop/SourceControl/AnoDesign/gen/GSOT1 ] || mkdir \
  /Volumes/Develop/SourceControl/AnoDesign/gen/GSOT1

[ -d /Volumes/Develop/SourceControl/AnoDesign/gen/GSOT1/code ] || mkdir \
  /Volumes/Develop/SourceControl/AnoDesign/gen/GSOT1/code

[ -d /Volumes/Develop/SourceControl/AnoDesign/gen/GSOT1/patchers ] || mkdir \
  /Volumes/Develop/SourceControl/AnoDesign/gen/GSOT1/patchers

cp "$HOME/Documents/Max 9/Projects/GSOTTgenB1/Booknotes.md" \
/Volumes/Develop/SourceControl/AnoDesign/gen/GSOT1/

cp "$HOME/Documents/Max 9/Projects/GSOTTgenB1/GSOTTgenB1.maxproj" \
/Volumes/Develop/SourceControl/AnoDesign/gen/GSOT1/

cp -R "$HOME/Documents/Max 9/Projects/GSOTTgenB1/code" \
/Volumes/Develop/SourceControl/AnoDesign/gen/GSOT1/

cp -R "$HOME/Documents/Max 9/Projects/GSOTTgenB1/patchers" \
/Volumes/Develop/SourceControl/AnoDesign/gen/GSOT1/

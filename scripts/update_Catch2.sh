#!/bin/bash
# assume running from AnoDesign
# run like sh scripts/update_Catch2.sh

[ -d /Volumes/Develop/SourceControl/AnoDesign/cpp/Catch2 ] || mkdir \
  /Volumes/Develop/SourceControl/AnoDesign/cpp/Catch2

cd /Volumes/Develop/SourceControl/AnoDesign/cpp/Catch2 || exit
curl -O https://raw.githubusercontent.com/catchorg/Catch2/devel/extras/catch_amalgamated.hpp
curl -O https://raw.githubusercontent.com/catchorg/Catch2/devel/extras/catch_amalgamated.cpp

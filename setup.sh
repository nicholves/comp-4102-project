#!/bin/bash

git submodule update --init
mkdir "./yolov5/runs"
mkdir "./yolov5/run/train"

search_dir=./models/
for entry in "$search_dir"
do
  cp -r $entry ./yolov5/runs/train
done
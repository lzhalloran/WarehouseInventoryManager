#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'This program runs on Python3, but it looks like Python3 is not installed.
    Installing Python3...'
  exit 1
fi

python3 main.py
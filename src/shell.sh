#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
    echo 'This program runs on Python3, but it looks like Python3 is not installed.
    Installing Python3...'
    sudo apt-get update
    sudo apt-get install python3
fi

if ! [[ -x "$(command -v pip)" ]]
then
    echo 'This program requires pip installer, but it looks like pip is not installed.
    Installing pip...'
    sudo apt-get install python3-pip
fi

python3 -m venv .venv
source .venv/bin/activate

python3 main.py

deactivate

rm -rf .venv .pytest_cache
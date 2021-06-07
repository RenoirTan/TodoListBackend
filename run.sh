#!/usr/bin/bash

if [ "$1" -eq "" ]; then
    echo "You must specify at least one positional argument."
else
    python -m todolist_backend $@
fi
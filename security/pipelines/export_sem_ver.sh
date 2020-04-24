#! /bin/bash

# Setup.py expected to contain:
    # setup(
    #     version="1.1"
    # )
# Find version= in setup.py
# Trim characters before version
# Trim characters after the last , (assumes , can't be used in version)
# Finally remove the "'s from the string
#
export SEM_VER=$(cat setup.py | grep version= | sed -e 's/.*version=//g' | sed -e 's/,.*//g' | tr -d '"')

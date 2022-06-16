#!/usr/local/bin/bash

function changeToProjectRoot {

    areHere=$(basename "${PWD}")
    export areHere
    if [[ ${areHere} = "scripts" ]]; then
        cd ..
    fi
}

changeToProjectRoot

#
#  Assumes python 3 is on PATH
#
clear

if [[ $# -eq 0 ]] ; then
        echo "in alias mode"
        rm -rf build dist
        # python setup.py py2app -A --iconfile src/org/pyut/resources/img/Pyut.icns
        python setup.py py2app
else
    if [[ ${1} = 'deploy' ]] ; then
            echo "in deploy mode"
            rm -rf build dist
            # python -O setup.py py2app --packages=wx,xmlschema,pygmlparser --iconfile src/org/pyut/resources/img/Pyut.icns
            python -O setup.py py2app --packages=click
            echo "remove invalid link that code signing complains about"
            cd "dist/peskytm.app/Contents/Resources/lib/python3.10"  || ! echo "No such directory"
            rm -rfv site.pyo
    else
        echo "Unknown command line arguments"
    fi
fi

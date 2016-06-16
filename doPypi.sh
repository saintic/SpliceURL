#!/bin/bash
#编译打包程序并上传到Pypi

if [ "$1" = "upload" ]; then
    python setup.py register sdist upload
else
    python setup.py build
    sudo python setup.py install
fi

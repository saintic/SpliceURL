#!/usr/bin/env python

import re
from SpliceURL import __version__, __doc__, __author__

try:
    from setuptools import setup, find_packages
except ImportError:
    print "Install it using your package manager (usually python-setuptools) or via pip (pip install setuptools)."
    exit(127)

setup(
    name = 'SpliceURL',
    version = __version__,
    description = __doc__,
    author = __author__,
    author_email = re.split('<?>?', __author__)[1],
    keywords = "WebURL",
    url = 'https://github.com/saintic/SpliceURL',
    download_url = 'https://github.com/saintic/SpliceURL',
    license = "MIT",
    packages = find_packages(),
    py_modules = [ 'SpliceURL', 'demo', ],
    classifiers = [
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

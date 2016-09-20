#!/usr/bin/env python

import re
from SpliceURL import __version__, __doc__, __author__

try:
    from setuptools import setup, find_packages
except ImportError:
    raise ImportError("Cannot import setuptools")

setup(
    name = 'SpliceURL',
    version = __version__,
    description = __doc__,
    author = __author__,
    author_email = re.split('<?>?', __author__)[1],
    keywords = "URL, splice, split, modify",
    url = 'https://github.com/saintic/SpliceURL',
    download_url = 'https://github.com/saintic/SpliceURL/releases/tag/v1.1',
    license = "MIT",
    py_modules = [ 'SpliceURL', ],
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

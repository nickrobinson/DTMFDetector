#!/usr/bin/env python

from distutils.core import setup

DESCRIPTION = """
DTMF Detection Library that takes wav files as input and outputs DTMF digit string. Project hosted at: http://fbdtmfdetector.sourceforge.net/ Written by David Luu
"""[1:-1]


CLASSIFIERS = """
Development Status :: 4 - Beta
License :: Public Domain
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(name         = 'dtmf-detector',
      version      = '0.1.0',
      description  = 'DTMF Detection Library',
      long_description = DESCRIPTION,
      author       = 'David Luu',
      author_email = 'nick@nlrobinson.com',
      url          = 'http://github.com/nickrobinson/DTMFDetector',
      license      = 'Public Domain',
      keywords     = 'voip sip dtmf phone analog testing',
      platforms    = 'any',
      classifiers  = CLASSIFIERS.splitlines(),
      package_dir  = {'' : 'src'},
      packages     = ['dtmf-detector'],
      package_data = {'dtmf-detector': ['tests/*.txt']},
      install_requires=[
      ],
)

""" From now on use this approach

python setup.py sdist upload
git tag -a 1.2.3 -m 'version 1.2.3'
git push --tags"""

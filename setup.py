"""
pyrtf-ng - The next generation in Rich Text Format documents for Python.

pyrtf-ng is a pure python module for the efficient creation and parsing of rich
text format documents. Supports styles, tables, cell merging, jpg and png
images and tries to maintain compatibility with as many RTF readers as
possible. 
"""
import os
from distutils.core import setup

doclines = __doc__.split("\n")

packageName = 'rtfng'

def findPackages():
    packages = []
    for directory, subdirectories, files in os.walk(packageName):
        if '__init__.py' in files:
            packages.append(directory.replace(os.sep, '.'))
    return packages

setup(name = 'pyrtf-ng',
    version = open('VERSION').read().strip(),
    author = 'Duncan McGreggor',
    author_email = 'oubiwann@adytum.us',
    url = 'http://code.google.com/p/pyrtf-ng/',
    license = 'MIT',
    platforms = ['Any'],
    description = doclines[0],
    long_description = '\n'.join( doclines[2:]),
    keywords = ('RTF', 'Rich Text', 'Rich Text Format', 'documents',
        'word'),
    packages = findPackages(),
    classifiers = [f.strip() for f in """
        Development Status :: 4 - Beta
        Topic :: Text Editors :: Text Processing
        Topic :: Software Development :: Libraries :: Python Modules
        Intended Audience :: Developers
        Programming Language :: Python
        License :: OSI Approved :: MIT
        """]
    )

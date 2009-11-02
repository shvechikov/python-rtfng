#!/usr/bin/env python
"""
This script introspects the RTF unit tests and generates the files that are
used for comparison when running those tests.

Note that this script intentionally only writes to a pending directory. You
must manually verify that the generated files are what you expect (I recommend
using OpenOffice for this). Aftwards, copy the good files over to the
sources/rtfng directory.

Once verified and copied, the docs generated will be used in the unit tests
against which test output will be checked. Thus any changes introduced into the
codebase that affect how these generated RTF files are rendered may cause the
tests to fail. For buggy code, this is exactly what we want, so that we can see
the error(s) happening in our tests and write new ones when our fixes are in
place. For new features, we need to update the unit tests, verify that they
create the correct output, and then regenerate the reference RTF files with
this script.
"""
import os, sys
from unittest import TestCase

from rtfng.utils import findTests, importModule

from test.test_all import searchDirs, skipFiles

base = ['test', 'sources', 'rtfng']
pending = base + ['pending']
baseDir = os.path.join(*base)
pendingDir = os.path.join(*pending)
doneList = []

requestedList = sys.argv[1:]
if requestedList:
    print 'Only writing these methods: %s' % ', '.join(requestedList)

# iterate through the test files
for startDir in searchDirs:
    for testFile in findTests(startDir, skipFiles):
            modBase = os.path.splitext(testFile)[0]
            name = modBase.replace(os.path.sep, '.')
            # import the testFile as a module
            mod = importModule(name)
            # iterate through module objects, checking for TestCases
            for objName in dir(mod):
                if not objName.endswith('TestCase'):
                    continue
                obj = getattr(mod, objName)
                if not issubclass(obj, TestCase):
                    continue
                # iterate through the TestCase attrs, looking for make_*
                # methods
                for attrName in dir(obj):
                    if attrName.startswith('make_'):
                        
                        # Make sure this is not a duplicate.
                        if attrName in doneList:
                            raise Exception('Duplicate test method found: %s' % attrName)
                        else:
                            doneList.append(attrName)
                        
                        # Skip if not requested.
                        rootName = attrName.split('make_')[1]
                        if requestedList and rootName not in requestedList:
                            continue

                        # Save file.
                        filename = '%s.rtf' % rootName
                        doc = getattr(obj, attrName)()
                        fh = open(os.path.join(pendingDir, filename), 'w+')
                        print "Writing %s ..." % filename
                        doc.write(fh)
                        fh.close()


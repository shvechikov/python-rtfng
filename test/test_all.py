#!/usr/bin/env python
import os
from unittest import TestCase, TestSuite
from unittest import TestLoader, TextTestRunner

from rtfng.utils import findTests, importModule

from test_doctests import suite as doctestSuite

searchDirs = ['rtfng', 'test']
skipFiles = ['test_doctests.py', 'test_all.py']

def getSuites():
    suites = [doctestSuite]
    loader = TestLoader()
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
                # create a suite from any test cases
                suite = loader.loadTestsFromTestCase(obj)
                # append to suites list
                suites.append(suite)
    return suites

if __name__ == '__main__':
    suites = getSuites()
    runner = TextTestRunner(verbosity=2)
    runner.run(TestSuite(suites))

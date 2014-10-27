import unittest

from loremipsum.tests import test_loremipsum
from loremipsum.tests import test_generator
from loremipsum.tests import test_plugs
from loremipsum.tests import plugs_testpackage
# from loremipsum.tests import test_serialization

suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_generator))
suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_loremipsum))
suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_plugs))
# suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_serialization))
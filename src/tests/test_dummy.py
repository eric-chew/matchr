import unittest
from main import dummy

class TestMain(unittest.TestCase):
    def test_dummy(self):
        assertEqual(dummy('a'), 'a')
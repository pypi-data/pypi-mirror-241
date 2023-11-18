import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plaincities import Countries

class GeneratedFilesTestCase(unittest.TestCase):

    def test_load_generated_files(self):
        countries = Countries('ko', path='tests/generated')
        usa = countries['US']
        self.assertEqual(usa.name, '미국')

if __name__ == '__main__':
    unittest.main()

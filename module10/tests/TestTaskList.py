# Test the various task list features
# often this will be broken up tinto separate test files - one per object
import unittest
import sys
import os

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

class TestTaskList(unittest.TestCase):

    pass 


if __name__ == '__main__':
    unittest.main()

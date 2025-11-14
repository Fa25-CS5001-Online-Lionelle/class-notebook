# Test the various task list features
# often this will be broken up into separate test files - one per object
import unittest
import sys
import os

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ListItem import ListItem 
from TaskList import loadListFromFile

class TestTaskList(unittest.TestCase):
    
    def test_init_ListItemValid(self) -> None:
        item = ListItem("Short Description", "Longer One")
        self.assertEqual(item.shortName, "Short Description")
        self.assertEqual(item.details, "Longer One")

    def test_init_ListItemInValid(self) -> None:
        """
        Tests to see if a ListItem raises a TypeError 
        when initialized with no shortName
        """
        with self.assertRaises(TypeError):
            _ = ListItem("")
            _ = ListItem(None)

    def test_load_file(self) -> None:
        """Going to load the file from list.csv, and check that contents match
        the values from the file in the list created 
        see - loadListFromFile
        """
        tlist = loadListFromFile("data/list.csv", "Test List")
        self.assertEqual(tlist.size, 3)
        item1 = tlist.getItem(0)
        self.assertEqual(item1.shortName, "project01")
        self.assertEqual(item1.details, "Figure out features of project")
        self.assertFalse(item1._ListItem__completed)  # Accessing the private attribute for testing




if __name__ == '__main__':
    unittest.main()

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work"""
        formatted_name = get_formatted_name('janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
    	formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    	self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

import unittest
from file1 import Names


class TestFullName(unittest.TestCase):
    def setUp(self):
        self.haley = Names('Haley', 'Smith')
        self.jaxon = Names('Jaxon', 'Narramore')

    def test_full_name(self):
        self.assertEqual(self.haley.full_name, 'Haley Smith')


if __name__ == '__main__':
    unittest.main()

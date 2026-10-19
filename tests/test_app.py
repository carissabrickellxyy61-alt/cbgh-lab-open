import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import unittest
from app import add, greet

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_greet(self):
        self.assertEqual(greet('world'), 'hello world')

if __name__ == '__main__':
    unittest.main()

import unittest
from Demo_functions.add import add

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.add = add
        
    def test_add(self):
        fve = 5
        self.assertEqual(self.add(3,2), fve)

    def test_add_fail2(self):
        with self.assertRaises(TypeError):
            self.add(2, "3")       
        
    def tearDown(self):
        del self.add
        
        
if __name__ == '__main__':
    unittest.main()
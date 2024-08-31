import unittest
from parameterized import parameterized

def fruit_count(fruit, basket):
    return len([item for item in basket if item == fruit])

class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        ('apple', 5),
        ('banana', 3),
        ('orange', 2)
    ])
    def test_fruit_count(self, fruit, expected_count):
        # Create a sample basket with the specified fruits
        basket = [fruit] * expected_count

        # Test the fruit count
        self.assertEqual(fruit_count(fruit, basket), expected_count)

if __name__ == '__main__':
    unittest.main()
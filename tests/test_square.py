import unittest
from sources.square import hi_square

class TestSquare(unittest.TestCase):
    
    def test_hi_square(self):
        result = hi_square(3)
        self.assertEqual(result, 9)

        result = hi_square(-2)
        self.assertEqual(result, 4)

        result = hi_square(0)
        self.assertEqual(result , 0)

if __name__ == '__main__':
    unittest.main()
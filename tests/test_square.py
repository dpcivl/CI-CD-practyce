import sys
import os

# sources 디렉터리를 모듈 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sources')))

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
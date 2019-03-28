import unittest
from python_function import high_pass_filter

class TestHighPassFilter(unittest.TestCase):
    def test_python(self):
     self.assertEqual(high_pass_filter(11), 10)
     self.assertEqual(high_pass_filter(4), 4)



if __name__ == '__main__':
    unittest.main()

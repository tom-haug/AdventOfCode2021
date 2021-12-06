import unittest

import day03_part01 as part01
import day03_part02 as part02

class TestDay03(unittest.TestCase):
    def test_part01_sample01(self):
        result = part01.get_part_one_result("input_sample01.txt")
        self.assertEqual(result, 198)

    def test_part01(self):
        result = part01.get_part_one_result("input.txt")
        self.assertEqual(result, 693486)

    def test_part02_sample01(self):
        result = part02.get_part_two_result("input_sample01.txt")
        self.assertEqual(result, 230)

    def test_part02(self):
        result = part02.get_part_two_result("input.txt")
        self.assertEqual(result, 3379326)


if __name__ == "__main__":
    unittest.main()

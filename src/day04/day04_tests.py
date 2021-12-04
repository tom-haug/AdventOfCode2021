import unittest
import day04_part01 as part01


class TestDay04(unittest.TestCase):
    def test_part01_sample01(self):
        result = part01.get_part_one_result("input_sample01.txt")
        self.assertEqual(result, 4512)

    def test_part01(self):
        result = part01.get_part_one_result("input.txt")
        self.assertEqual(result, 25410)

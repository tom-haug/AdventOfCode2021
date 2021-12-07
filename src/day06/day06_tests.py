import unittest
import day06_part01 as part01


class TestDay05(unittest.TestCase):
    def test_part01_sample01(self):
        result = part01.get_part_one_result("input_sample01.txt")
        self.assertEqual(result, 5934)

    def test_part01(self):
        result = part01.get_part_one_result("input.txt")
        self.assertEqual(result, 375482)


if __name__ == "__main__":
    unittest.main()

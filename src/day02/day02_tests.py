import unittest
import day02_part01 as part01
import day02_part02 as part02


class TestDay01(unittest.TestCase):
    def test_part01_sample01(self):
        result = part01.get_part_one_result("input_sample01.txt")
        self.assertEqual(result, 150)

    def test_part01(self):
        result = part01.get_part_one_result("input.txt")
        self.assertEqual(result, 1962940)

    def test_part02_sample01(self):
        result = part02.get_part_two_result("input_sample01.txt")
        self.assertEqual(result, 900)

    def test_part02(self):
        result = part02.get_part_two_result("input.txt")
        self.assertEqual(result, 1813664422)


if __name__ == "__main__":
    unittest.main()
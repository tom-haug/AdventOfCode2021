import pytest

from src.day15.common import process


class TestDay15:
    def test_part01_sample01(self):
        result = process("src/day15/input_sample01.txt", 1)
        assert result == 40

    def test_part01(self):
        result = process("src/day15/input.txt", 1)
        assert result == 595

    def test_part01_sample02(self):
        result = process("src/day15/input_sample01.txt", 5)
        assert result == 315

    @pytest.mark.skip("long-running test")
    def test_part02(self):
        result = process("src/day15/input.txt", 5)
        assert result == 2914

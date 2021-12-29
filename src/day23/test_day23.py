import pytest
from src.day23.common import get_game_result


class TestDay20:
    def test_part01_sample01(self):
        lowest_energy, _ = get_game_result("src/day23/input_sample01.txt")
        assert lowest_energy == 12521

    @pytest.mark.skip("long-running test")
    def test_part01(self):
        lowest_energy, _ = get_game_result("src/day23/input_part01.txt")
        assert lowest_energy == 15412

    @pytest.mark.skip("long-running test")
    def test_part02_sample02(self):
        lowest_energy, _ = get_game_result("src/day23/input_sample02.txt")
        assert lowest_energy == 44169

    @pytest.mark.skip("long-running test")
    def test_part02(self):
        lowest_energy, _ = get_game_result("src/day23/input_part02.txt")
        assert lowest_energy == 52358

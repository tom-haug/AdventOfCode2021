import pytest

from src.day18.part01 import *
from src.day18.part02 import *
from src.day18.common import *
from src.shared.utils import noop


class TestDay17:
    def test_load_statements_from_file(self):
        statements = load_statements_from_file("src/day18/test_data/input_load_from_file01.txt")

        assert len(statements) == 7
        assert str(statements[0]) == "[1,2]"
        assert str(statements[1]) == "[[1,2],3]"
        assert str(statements[2]) == "[9,[8,7]]"
        assert str(statements[3]) == "[[1,9],[8,5]]"
        assert str(statements[4]) == "[[[[1,2],[3,4]],[[5,6],[7,8]]],9]"
        assert str(statements[5]) == "[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]"
        assert str(statements[6]) == "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"

    @pytest.mark.parametrize("input_statement, result_statement", [
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
        ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
    ])
    def test_explode_success(self, input_statement: str, result_statement: str):
        statement = SnailStatement(input_statement, noop)

        result = statement.try_explode()

        assert result is True
        assert str(statement) == result_statement

    @pytest.mark.parametrize("input_statement, result_statement", [
        ("[[[[0,7],4],[15,[0,13]]],[1,1]]", "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"),
        ("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]", "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"),
    ])
    def test_split_success(self, input_statement: str, result_statement: str):
        statement = SnailStatement(input_statement, noop)

        result = statement.try_split()

        assert result is True
        assert str(statement) == result_statement

    @pytest.mark.parametrize("input_statement, expected_result", [
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
    ])
    def test_magnitude(self, input_statement: str, expected_result: str):
        statement = SnailStatement(input_statement, noop)

        result = statement.magnitude

        assert result == expected_result

    def test_part01_sample01(self):
        result = get_part_one_result("src/day18/test_data/input_sample01.txt")
        assert result == 4140

    def test_part01(self):
        result = get_part_one_result("src/day18/input.txt")
        assert result == 4173

    def test_part02_sample01(self):
        result = get_part_two_result("src/day18/test_data/input_sample01.txt")
        assert result == 3993

    def test_part02(self):
        result = get_part_two_result("src/day18/input.txt")
        assert result == 4706

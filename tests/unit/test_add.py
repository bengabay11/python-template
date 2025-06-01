import pytest

from src.main import add


@pytest.mark.parametrize("first_num,second_num,expected", [(1, 2, 3), (-1, -2, -3), (0, 0, 0)])
def test_add(first_num: int, second_num: int, expected: int) -> None:
    assert add(first_num, second_num) == expected

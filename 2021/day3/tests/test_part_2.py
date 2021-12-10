import os

import pytest
from day3.part_2 import get_rating


def test_get_life_support_rating():
    data = []
    input_file = os.path.abspath(
        os.path.join(os.getcwd(), "2021", "day3", "data", "input_example")
    )
    with open(input_file) as file:
        while line := file.readline().rstrip():
            data.append(line)

    # assert get_rating(data.copy(), True) == 23
    assert get_rating(data.copy(), False) == 10

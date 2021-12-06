import os

import pytest
from day3.part_1 import get_power_consumption


def test_get_power_consumption():
    data = []
    input_file = os.path.abspath(
        os.path.join(os.getcwd(), "2021", "day3", "data", "input_example")
    )
    with open(input_file) as file:
        while line := file.readline().rstrip():
            data.append(line)

    assert get_power_consumption(data) == 198

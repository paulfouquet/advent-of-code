import os
import pytest

from day2.part_1 import get_final_position

def test_get_final_position():
    data = []
    input_file = os.path.abspath(os.path.join(os.getcwd(), "2021", "day2", "data", "input_example"))
    with open(input_file) as file:
        while (line := file.readline().rstrip()):
            data.append(line)

    assert get_final_position(data) == 150
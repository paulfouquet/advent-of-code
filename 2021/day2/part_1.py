import os
from typing import List


def get_final_position(input: List[str]) -> int:
    forward = 0
    depth = 0

    for i in range(0, len(input)):
        current_input = input[i].split()
        direction = current_input[0]
        units = int(current_input[1])

        # FIXME: Python 3.10 has a match-case statement
        if direction == "forward":
            forward = forward + units
        elif direction == "down":
            depth = depth + units
        elif direction == "up":
            depth = depth - units
        else:
            print("unknow direction")

    return forward * depth


def main():
    data = []
    input_file = os.path.abspath(
        os.path.join(os.getcwd(), "2021", "day2", "data", "input")
    )
    with open(input_file) as file:
        while line := file.readline().rstrip():
            data.append(line)

    print(get_final_position(data))


if __name__ == "__main__":
    main()

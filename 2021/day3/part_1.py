import os
from typing import List


def get_power_consumption(data: List[str]) -> int:
    gamma = ""
    epsilon = ""

    for i in range(0, len(data[0])):
        count_zero = 0
        count_one = 0

        for j in range(0, len(data)):
            if data[j][i] == "0":
                count_zero = count_zero + 1
            else:
                count_one = count_one + 1

        if count_zero > count_one:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"

    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)

    return gamma_decimal * epsilon_decimal


def main():
    data = []
    input_file = os.path.abspath(
        os.path.join(os.getcwd(), "2021", "day3", "data", "input")
    )
    with open(input_file) as file:
        while line := file.readline().rstrip():
            data.append(line)

    print(get_power_consumption(data))


if __name__ == "__main__":
    main()

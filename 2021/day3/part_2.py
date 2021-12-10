import os
from typing import List


def get_rating(data: List[str], most_common: bool) -> int:

    while len(data) > 1:
        for i in range(0, len(data[0])):
            if len(data) == 1:
                break
            remove_data: List[str] = []
            print(data)
            count_one = sum(element[i] == "1" for element in data)
            count_zero = sum(element[i] == "0" for element in data)

            if most_common:
                bit_criteria = "1"
                if count_one < count_zero:
                    bit_criteria = "0"
            else:
                bit_criteria = "0"
                if count_one < count_zero:
                    bit_criteria = "1"

            for element in data:
                print(element)
                if not str(element[i]) == bit_criteria:
                    print("remove")
                    remove_data.append(element)

            for element in remove_data:
                data.remove(element)

    return int(data[0], 2)


def main():
    data = []
    input_file = os.path.abspath(
        os.path.join(os.getcwd(), "2021", "day3", "data", "input")
    )
    with open(input_file) as file:
        while line := file.readline().rstrip():
            data.append(str(line))

    print(get_rating(data.copy(), True) * get_rating(data.copy(), False))


if __name__ == "__main__":
    main()

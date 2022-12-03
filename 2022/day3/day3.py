import string


def main():
    with open("input", "r") as f:
        # Split the list using empty line which are two line return
        input_data = f.read().splitlines()

        # Part 1
        sum_priority = 0
        for line in input_data:
            first_half = line[slice(0, len(line) // 2)]
            second_half = line[slice(len(line) // 2, len(line))]
            print(first_half)
            print(second_half)
            # FIXME: Perfs - Probably not optimized at it does not stop at the first common char found
            common_letter = list(set(first_half).intersection(second_half))[0]
            # Index starts at 0 but first position should be 1
            position = string.ascii_lowercase.index(str.lower(common_letter)) + 1
            if str.isupper(common_letter):
                position += 26

            sum_priority += position

        print(f"Part 1: {sum_priority}")

        # Part 2
        sum_priority = 0
        groups = []
        current_group = []
        for line in input_data:
            if len(current_group) < 3:
                current_group.append(line)
            if len(current_group) == 3:
                groups.append(current_group.copy())
                current_group.clear()

        print(groups)

        for group in groups:
            common_item = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
            position = string.ascii_lowercase.index(str.lower(common_item)) + 1
            if str.isupper(common_item):
                position += 26

            sum_priority += position

        print(f"Part 2: {sum_priority}")


if __name__ == "__main__":
    main()

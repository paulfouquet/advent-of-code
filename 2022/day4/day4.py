def main():
    with open("input", "r") as f:
        # Split the list using empty line which are two line return
        input_data = f.read().splitlines()

        # Part 1
        count_one = 0
        for line in input_data:
            pairs = line.split(",")
            a, b = map(int, pairs[0].split("-"))
            c, d = map(int, pairs[1].split("-"))

            if (a >= c and b <= d) or (c >= a and d <= b):
                count_one += 1
                # print(line)

        print(count_one)

        # Part 2
        count_two = 0
        for line in input_data:
            pairs = line.split(",")
            a, b = map(int, pairs[0].split("-"))
            c, d = map(int, pairs[1].split("-"))

            if max(a, c) <= min(b, d):
                count_two += 1
                # print(line)

        print(count_two)


if __name__ == "__main__":
    main()

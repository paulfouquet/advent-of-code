def main():
    with open("input", "r") as f:
        # Split the list using empty line which are two line return
        input_data = f.read().split("\n\n")

        elves_calories = []
        for elf_calories in input_data:
            calories = []
            for calorie in elf_calories.splitlines():
                calories.append(int(calorie))
            elves_calories.append(calories)

        total_calories = []
        for elf_calories in elves_calories:
            total_calories.append(sum(elf_calories))
        total_calories = sorted(total_calories)

    print(f"Part 1 = {total_calories[-1]} / Part 2 = {sum(total_calories[-3:])}")

if __name__ == "__main__":
    main()

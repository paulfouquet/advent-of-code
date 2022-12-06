import re


def main():
    with open("input", "r") as f:
        # Part 1
        stacks, procedures = map(str.splitlines, f.read().rstrip().split("\n\n"))
        col = stacks[len(stacks) - 1]
        stack_columns = {}

        for stack in reversed(stacks[:-1]):
            for char_position, element in enumerate(stack):
                if element.isalpha():
                    if not stack_columns.get(col[char_position]):
                        stack_columns[col[char_position]] = []
                    stack_columns[col[char_position]].append(element)

        for procedure in procedures:
            number, ori, dst = map(int, re.findall(r"\d+", procedure))
            for _ in range(0, number):
                stack_columns[str(dst)].append(stack_columns[str(ori)].pop())

        top_list = ""
        for stack in stack_columns.values():
            top_list += stack.pop()

        print(top_list)


if __name__ == "__main__":
    main()

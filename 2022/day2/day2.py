from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class ScoreResult(Enum):
    LOST = 0
    DRAW = 3
    WIN = 6


def main():
    # Part 1
    conversion_a = {
        "A": Shape.ROCK,
        "B": Shape.PAPER,
        "C": Shape.SCISSORS,
        "X": Shape.ROCK,
        "Y": Shape.PAPER,
        "Z": Shape.SCISSORS,
    }
    with open("input", "r") as f:
        guide = f.read().splitlines()
        score = 0
        for game in guide:
            result = ScoreResult.WIN
            elf, me = game.split()
            elf = conversion_a.get(elf)
            me = conversion_a.get(me)
            if me == elf:
                result = ScoreResult.DRAW
            elif (
                (elf == Shape.ROCK and me != Shape.PAPER)
                or (elf == Shape.SCISSORS and me != Shape.ROCK)
                or (elf == Shape.PAPER and me != Shape.SCISSORS)
            ):
                result = ScoreResult.LOST
            score += result.value + me.value
        print(f"part1: {score}")

    # Part 2
    conversion_b = {
        "A": Shape.ROCK,
        "B": Shape.PAPER,
        "C": Shape.SCISSORS,
        "X": ScoreResult.LOST,
        "Y": ScoreResult.DRAW,
        "Z": ScoreResult.WIN,
    }
    with open("input", "r") as f:
        guide = f.read().splitlines()
        score = 0
        for game in guide:
            elf, result = game.split()
            elf = conversion_b.get(elf)
            result = conversion_b.get(result)
            if result == ScoreResult.LOST:
                if elf == Shape.ROCK:
                    score += Shape.SCISSORS.value
                if elf == Shape.PAPER:
                    score += Shape.ROCK.value
                if elf == Shape.SCISSORS:
                    score += Shape.PAPER.value
            elif result == ScoreResult.WIN:
                if elf == Shape.ROCK:
                    score += Shape.PAPER.value
                if elf == Shape.PAPER:
                    score += Shape.SCISSORS.value
                if elf == Shape.SCISSORS:
                    score += Shape.ROCK.value
            else:
                score += elf.value
            score += result.value

        print(f"part2: {score}")


if __name__ == "__main__":
    main()

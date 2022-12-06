def get_marker(signal: str, sequence_size: int) -> int:
    """Get the start marker which is the number of characters before
    the first sequence of sequence_size distinct characters in the 'signal'

    Args:
        signal: a series of seemingly-random characters
        sequence_size: the number of char to check

    Returns:
        the marker
    """
    for start in range(0, len(signal)):
        chars_sequence = signal[start : start + sequence_size]
        unique_chars = "".join(set(chars_sequence))

        if len(unique_chars) == len(chars_sequence):
            return start + sequence_size


def main():
    with open("input", "r") as f:
        input_data = f.read()
        # Part 1
        print(get_marker(input_data, 4))
        # Part 2
        print(get_marker(input_data, 14))


if __name__ == "__main__":
    main()

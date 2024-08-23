def count_true_love(name: str) -> dict:
    # Initialize a dictionary with letters as keys and counts as values

    count_letters = {"T": 0, "R": 0, "U": 0, "E": 0, "L": 0, "O": 0, "V": 0}

    for letter in name:
        if letter in count_letters:
            count_letters[letter] += 1

    return count_letters

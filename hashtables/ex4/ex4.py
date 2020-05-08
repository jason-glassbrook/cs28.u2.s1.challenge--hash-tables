def has_negatives(a):

    negatives = {(-n): None for n in a if n < 0}
    positives = {(+n): None for n in a if n > 0}

    matches = [n for n in positives if n in negatives]

    return matches


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

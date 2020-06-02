def has_negatives(a):

    negatives_map = {(-n): None for n in a if n < 0}
    positives_map = {(+n): None for n in a if n > 0}

    matches = [n for n in positives_map if n in negatives_map]

    return matches


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

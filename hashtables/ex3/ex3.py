def intersection(arrays):

    # set default output
    repeats_dict = {}

    # iteratively construct a dict, inserting repeats to `repeats_dict`
    items_dict = {}
    for array in arrays:
        for item in array:
            if item in items_dict:
                if item in repeats_dict:
                    repeats_dict[item] += 1
                else:
                    repeats_dict[item] = 1
            else:
                items_dict[item] = None

    return list(repeats_dict)


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

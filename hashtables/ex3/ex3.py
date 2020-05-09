def intersection(arrays):

    # set default `repeats_map`
    repeats_map = {}

    # iteratively construct a map, inserting repeats to `repeats_map`
    items_map = {}
    for array in arrays:
        for item in array:
            if item in items_map:
                if item in repeats_map:
                    repeats_map[item] += 1
                else:
                    repeats_map[item] = 1
            else:
                items_map[item] = None

    return list(repeats_map)


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

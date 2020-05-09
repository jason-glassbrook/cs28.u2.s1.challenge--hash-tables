from collections import defaultdict as DefaultDict


def get_indices_of_item_weights(weights, length, limit):

    # map weights to indices, allowing duplicates:
    weight_to_indices_map = DefaultDict(list)
    for (i, w) in enumerate(weights):
        weight_to_indices_map[w].append(i)

    # set default `matches`
    matches = None

    # find indices of weights which sum to limit:
    for (w1, i1s) in weight_to_indices_map.items():

        # the indices of weight 1
        i1s = weight_to_indices_map[w1]

        # the next necessary weight
        w2 = limit - w1

        # the indices of weight 2, maybe...
        i2s = weight_to_indices_map[w2] if w2 in weight_to_indices_map else None

        # if there could be any, try to get matching indices
        if i1s and i2s:

            # if weights are different, use first index of both
            if w1 != w2:
                matches = (i1s[0], i2s[0])
                break

            # if weights are same, there need to be enough indices
            # i1s == i2s, in this case
            elif len(i1s) > 1:
                matches = tuple(i1s[0:2])
                break

    return matches

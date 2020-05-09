def get_indices_of_item_weights(weights, length, limit):

    # map weights to indices:
    weight_to_index_map = {weight: index for (index, weight) in enumerate(weights)}

    # set default `matches`
    matches = (None, None)

    # find indices of weights which sum to limit:
    for weight_1 in weight_to_index_map:

        weight_2 = limit - weight_1

        if weight_2 in weight_to_index_map:

            matches = (
                weight_to_index_map[weight_1],
                weight_to_index_map[weight_2],
            )

            break

    # override `matches` if none found
    if None in matches:
        matches = None

    return matches

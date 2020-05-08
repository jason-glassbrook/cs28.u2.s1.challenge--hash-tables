def get_indices_of_item_weights(weights, length, limit):

    # dict of weights to indices:
    weight_to_index_dict = {weight: index for (index, weight) in enumerate(weights)}

    # set default output
    index_tuple = (None, None)

    # iterate through dict to find limit:
    for weight_1 in weight_to_index_dict.keys():

        weight_2 = limit - weight_1

        if weight_2 in weight_to_index_dict:

            index_tuple = (
                weight_to_index_dict[weight_1],
                weight_to_index_dict[weight_2],
            )

            break

    if None in index_tuple:
        index_tuple = None

    return index_tuple

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    # dict of sources to destinations:
    source_to_destination_dict = {ticket.source: ticket.destination for ticket in tickets}

    # set default output
    route = []

    # first ticket is...
    if None in source_to_destination_dict:
        route.append(source_to_destination_dict[None])

    # iterate through remaining tickets...
    while route[-1] is not None:
        route.append(source_to_destination_dict[route[-1]])

    return route

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    # map sources to destinations:
    source_to_destination_map = {ticket.source: ticket.destination for ticket in tickets}

    # set default `route`
    route = []

    # first ticket is...
    if None in source_to_destination_map:
        route.append(source_to_destination_map[None])

    # iterate through remaining tickets...
    while route[-1] is not None:
        route.append(source_to_destination_map[route[-1]])

    return route

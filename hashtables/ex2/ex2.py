#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """

    trips = {}

    route = []

    for x in tickets:
        print(x.source, "Source   - Key")
        print(x.destination, "Destination    - Value")
        #Add to dictionary
        trips[x.source] = x.destination

    #create loop variables for the list
        
    count = 0
    next_destination = "NONE"

    while count < length:
        #get the key from dictionary to know where to go next
        print(next_destination)
        next_destination = trips.get(next_destination)
        print(next_destination)
        #add the next destination to the list
        route.append(next_destination)
        print(route)
        count += 1
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
reconstruct_trip(tickets, 3)



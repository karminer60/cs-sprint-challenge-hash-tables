#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    Dict = {}
    route =[]  

    for index in range(len(tickets)):
        ticket = tickets[index]
        Dict[ticket] = index 

    for index in range(len(tickets)):
        ticket = tickets[index]
        if ticket.source == 'NONE':
            route.append(ticket)
        elif ticket.destination == ticket.source:
            route.append(ticket)
        else:
            route.append(ticket)        

    return route

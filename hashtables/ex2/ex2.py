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
        key = ticket.source
        value = ticket.destination
        Dict[key]= value
            
    print(Dict) 
    key = 'NONE'
    while True:
        key = Dict[key]
        route.append(key) 
        if key == 'NONE':
            break
       
    print(route)
    return route

    

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    Dict = {}
    for index in range(len(weights)):
        weight = weights[index]
        Dict[weight] = index  

    for index in range(len(weights)):
        weight = weights[index]
        if limit - weight in Dict:
            indexTwo = Dict[limit - weight]
            if index > indexTwo :
                return (index, indexTwo)
            else:
                return (indexTwo, index)
      
    return None

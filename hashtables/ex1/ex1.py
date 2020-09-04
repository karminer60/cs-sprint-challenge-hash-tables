def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    Dict = {}
    result = []
    for index in range(len(weights)):
        Dict[weights[index]] = index  

    for index in range(len(weights)):
        if Dict[weights[index]] == Dict.get(limit - weights[index], 0):
            result.append(weights[index])
            result.append(Dict[weights[index]])
            return result
        else:
            return None


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #Plan: Store keys with values, dict that stores (number, countOfNumber)
    #update the dict for each number in array and do that for each array
    #then look through the dict and look for number to have a count that matches the number of arrays, and filter 
    Dict = {}
    result = []
    for array in arrays:
        for key in array:
            Dict[key] = Dict.get(key, 0) + 1         
    for key,count in Dict.items():
        if count == len(arrays):
            result.append(key)
        
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

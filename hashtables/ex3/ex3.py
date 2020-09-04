cache = {}
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #Plan: Store keys with values, dict that stores (number, countOfNumber)
    #update the dict for each number in array ad do that for each array
    #then look through the dict and look for number to have a count that matches the number of arrays, and filter 
    key = (x, y)
    if key in cache:
	    return cache[key]
    if key not in cache:
	    cache[key] = intersection(x,y) 
    return cache[key]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

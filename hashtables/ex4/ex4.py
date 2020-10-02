def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Use a dictionary to add the negative numbers and use that to search for negative versions of the positive numbers
    Dict = {}
    result = []
    for number in a:
        if number < 0:
            Dict[number] = True  
    for number in a:
        if number > 0 and - number in Dict:
            result.append(number)       
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Use a dictionary to add the negative numbers and use that to search for negative versions of the positive numbers
    Dict = {}
    result = []
    for number in array:
        if number < 0:
            Dict.append(number)    
    for number in array:
        if number > 0 and number in Dict:
                
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

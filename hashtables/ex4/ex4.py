def has_negatives(a):

    """
    YOUR CODE HERE

    """
    #create number dictionary
    numbers = {}

    #create result list
    result = []

    #loop through A

    for x in a:

        #Check to see if x is already in the dictionary
        if numbers.get(abs(x)):
            print(x)
            #Check to see if current x and stored x value = 0 (Check for negatives)
            if (numbers.get(abs(x)) + x) == 0:
                #pass x into the results list
                print("Adding this to result list --", abs(x))
                result.append(abs(x))

        #If not
        else:
            #Set x as the key and its value
            numbers[abs(x)] = x


    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))

def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """

    #Create a dictionary
    weights_dictionary = {}

    #go over list of weights
    
    for x in range(length):  # X is going from 0 - length

        print(weights_dictionary, "**************Dictionary****************")
        #Check if key value pair is in dictionary

        print(limit, " Limit")
        print(weights[x], " Weight")

        #Check to see if it is in the dictionary
        y = weights_dictionary.get(limit - weights[x])

        print(y, "Key value pair")

        if y != None:
            #y is a key which is remainder that is already in dictionary
            #x is current index of weights
            print(x,y)
            return (x, y)

        else:

            #Setting key as current value since not found in dictionary
            weights_dictionary[weights[x]] = x

            print(weights_dictionary[weights[x]], " X (Weights index) ")

    print(weights_dictionary, "Dictionary")

    return None

weights_3 = [4, 6, 10, 15, 16]

get_indices_of_item_weights(weights_3, 5, 16)
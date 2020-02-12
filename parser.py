from shlex import *
from Tree import *

BINARY_KEYWORDS = ["compare", "more"]
BUZZWORDS = ["of", "by"]


def parse(query):
    words = split(query)
    for BUZZWORD in BUZZWORDS:
        words = [word for word in words if word != BUZZWORD]
    return words


def buildTree(array):
    # Base case is when input array has length 1
    if len(array) == 1:
        return Tree(array[0])
    # check if first item in array is unary keyword
    elif array[0] not in BINARY_KEYWORDS:
        newTree = Tree(array[0])
        array.pop(0)
        newTree.setRightChild(buildTree(array))
        return newTree

    # run else if binary keyword detected as first element in array
    else:
        newTree = Tree(array[0]+array[1])
        array.pop(0)
        array.pop(0)

        newArray = []   # newArray created to hold all arguments before and identifier
        count = 0       # count variable used to keep track of encapsulated binary arguments
        index = 0       # index used to loop through array

        ### TODO: Exception handling for when no "and" is detected and index exceeds size of array
        # While loop splits the first half of arguments before the and identifier and remaining arguments after
        # into two arrays (newArray and array)
        while (array[index] != "and") and (count != 0):
            if array[index] in BINARY_KEYWORDS:
                count += 1
                newArray.append(array.pop(0))
            elif (array[index] == "and"):
                count -= 1
                newArray.append(array.pop(0))
            else:
                newArray.append(array.pop(0))
            index+= 1

        # build left and right branches with the two arrays
        newTree.setLeftChild(buildTree(newArray))
        newTree.setRightChild(buildTree(array))
        return newTree

def split(array, newArray, delim):
    count = 0   # count variable used to keep track of encapsulated binary arguments
    index = 0   # index used to loop through array

    while (array[index] != delim) and (count == 0):
        print(array[index] != delim)
        if array[index] in BINARY_KEYWORDS:
            count += 1
            newArray.append(array.pop(0))
        elif (array[index] == delim):
            count -= 1
            newArray.append(array.pop(0))
        else:
            newArray.append(array.pop(0))
        index += 1

    print(array)
    print(newArray)

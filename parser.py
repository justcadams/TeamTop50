from Tree import *

BINARY_KEYWORDS = ["compare", "more"]
BUZZWORDS = ["of", "by"]


def parse(search):
    array = []
    word = ""
    for c in search:
        if c == " ":
            if word in BUZZWORDS:
                word = ""
            else:
                array.append(word)
                word = ""
        else:
            word += c
    if word != "":
        array.append(word)
    return array


def buildTree(array):
    # check if first item in array is unary keyword
    if array[0] not in BINARY_KEYWORDS:
        newTree = Tree(array[0])
        array.pop(0)
        newTree.setRightChild(buildTree(array))

    # run else if binary keyword detected as first element in array
    else:
        newTree = Tree(array[0]+array[1])
        array.pop(0)
        array.pop(1)

        newArray = []   # newArray created to hold all arguments before and identifier
        count = 0       # count variable used to keep track of encapsulated binary arguments
        index = 0       # index used to loop through array

        ### TODO: Exception handling for when no "and" is detected and index exceeds size of array
        # While loop splits the first half of arguments before the and identifier and remaining arguments after
        # into two arrays (newArray and array)
        while (array[index] == "and") and (count != 0):
            if array[index] in BINARY_KEYWORDS:
                count += 1
                newArray.append(array.pop(0))
            elif (array[index] == "and"):
                count -= 1
                newArray.append(array.pop(0))
            else:
                newArray.append(array.pop(0))
            index += 1

        # build left and right branches with the two arrays
        newTree.setLeftChild(buildTree(newArray))
        newTree.setRightChild(buildTree(array))



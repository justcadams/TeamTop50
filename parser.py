import shlex
from Tree import *
from keywords import *

def parse(query):
    # Splits query into array, preserving words in quotation marks
    words = shlex.split(query)
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
        newTree = Tree(array[0])
        array.pop(0)

        index = split(array, "and")

        newTree.setLeftChild(buildTree(array[0:index]))
        newTree.setRightChild(buildTree(array[index+1:]))
        return newTree


def split(array, delim):
    count = 0   # count variable used to keep track of encapsulated binary arguments
    index = 0   # index for the split point

    while (array[index] != delim) or (count != 0):
        if array[index] in BINARY_KEYWORDS:
            count += 1

        elif array[index] == delim:
            count -= 1
        index += 1
        if index == len(array)-1:
            return -1
    return index

    print(index)
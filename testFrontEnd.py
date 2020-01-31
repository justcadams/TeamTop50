from Tree import *

def testTree():
    tree1 = Tree("testing")
    tree1.setLeftChild("hello")
    tree1.setRightChild("world")
    tree1.rc.setRightChild("testing again")

    tests = [(str(tree1), "<testing: hello, <world: _, testing again>>")]

    passedTest = True 
    for n,test in enumerate(tests):
        output = test[0]
        expected = test[1]
        if output != expected:
            print("Tree __str__ test #" + str(n+1) + " failed.")
            print("Output: " + output)
            print("Expected: " + expected)
            passedTest = False
        else:
            print("Tree __str__ test #" + str(n+1) + " passed!")

    return passedTest

def testEvaluate():
    tree1 = Tree("artist")
    tree1.setRightChild("Shape of You")
    
    tree2 = Tree("popularity")
    tree2.setRightChild("artist")
    tree2.rc.setRightChild("Blank Space")
    tests = [(tree1.evaluate(), "Ed Sheeran"),
            (tree2.evaluate(), "92")]

    passedTest = True
    for n,test in enumerate(tests):
        output = test[0]
        expected = test[1]
        if output != expected:
            print("Tree evaluate test #" + str(n+1) + " failed.")
            print("Output: " + output)
            print("Expected: " + expected)
            passedTest = False
        else:
            print("Tree evaluate test #" + str(n+1) + " passed!")

    return passedTest


allPassed = True
if not testTree():
    allPassed = False
if not testEvaluate():
    allPassed = False

if allPassed:
    print("All tests passed!")
else:
    print("Some test failed.")



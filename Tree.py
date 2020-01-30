
# Binary tree for constructing and executing query commands
class Tree():
    def __init__(self, data):
        # Tree is initialized with some data. 
        # Right and left children are initialized to None 
        self.data = data
        self.rc = None
        self.lc = None

    def addLeftChild(self, lc):
        # Adds a left child. lc can either be another tree or data.
        if type(lc) is Tree:
            self.lc = lc
        else: 
            self.lc = Tree(lc)

    def addRightChild(self, rc):
        # Adds a right child. rc can either be another tree or data.
        if type(rc) is Tree:
            self.rc = rc
        else: 
            self.lc = Tree(rc)

    def isLeaf(self):
        # Checks if this Tree has any children
        return self.rc is None and self.lc is None

    def evaluate(self):
        # TODO
        # Evaluates value of tree by carrying out operations and 
        # doing database queries; this is where backend should connect
        pass

    def __str__(self):
        # Prints a Tree (for debugging use)
        # Format: <data, <lc, rc>>
        # If a child is None, default value is _
        if self.isLeaf():
            return self.data

        if self.rc is None:
            rc = "_"
        else:
            rc = str(self.rc)

        if self.lc is None:
            lc = "_"
        else:
            lc = str(self.lc)

        return "<" + self.data + ", <" + lc + ", " + rc + ">"


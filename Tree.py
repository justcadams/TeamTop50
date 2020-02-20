# Binary tree for constructing and executing query commands
import keywords
import commands

class Tree:
    def __init__(self, data):
        # Tree is initialized with some data.
        # Right and left children are initialized to None
        self.data = data
        self.rc = None
        self.lc = None

    def setLeftChild(self, lc):
        # Adds a left child. lc can either be another tree or data.
        if isinstance(lc, Tree):
            self.lc = lc
        else:
            self.lc = Tree(lc)

    def setRightChild(self, rc):
        # Sets a right child. rc can either be another tree or data.
        if isinstance(rc, Tree):
            self.rc = rc
        else:
            self.rc = Tree(rc)

    def isLeaf(self):
        # Checks if this Tree has any children
        return self.rc is None and self.lc is None

    @property
    def evaluate(self):
        # Evaluates value of tree by carrying out operations and
        # doing database queries; this is where backend should connect
        data = self.data
        if self.isLeaf():
            return data
        elif data not in keywords.KEYWORDS:
            return "ERROR: Invalid command."
        else:
            command = commands.commandMap()[data]
            
            # Unary command handling
            if data in keywords.UNARY_KEYWORDS:
                return command(self.rc.evaluate)
            # Binary command handling
            elif data in keywords.BINARY_KEYWORDS:
                song1 = self.rc.evaluate
                song2 = self.lc.evaluate
                q1 = command(song1)
                q2 = command(song2)
                if data in keywords.GREATER_KEYWORDS:
                    if q1 > q2:
                        return song1
                    else:
                        return song2
                else:
                    if q1 < q2:
                        return song1
                    else:
                        return song2
            # Poly command handling
            else:
                Q = []
                songs = self.rc.evaluate
                for song in songs:
                    Q.append(command(song))

                if data in keywords.GREATER_KEYWORDS:
                    return songs[Q.index(max(Q))]
                else:
                    return songs[Q.index(min(Q))]



    def __str__(self):
        # Prints a Tree (for debugging use)
        # Format: <data: lc, rc>
        # If a child is None, default value is _
        if self.isLeaf():
            return str(self.data)

        if self.rc is None:
            rc = "_"
        else:
            rc = str(self.rc)

        if self.lc is None:
            lc = "_"
        else:
            lc = str(self.lc)

        return "<" + self.data + ": " + lc + ", " + rc + ">"

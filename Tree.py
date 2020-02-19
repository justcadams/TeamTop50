# Binary tree for constructing and executing query commands
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
        import keywords
        import testCommands
        # Evaluates value of tree by carrying out operations and
        # doing database queries; this is where backend should connect
        if self.isLeaf():
            return self.data
        elif self.data not in keywords.KEYWORDS:
            return "ERROR: Invalid command."
        else:
            if self.data == "song":
                return testCommands.virtualServer.getSongsByArtist(self.rc.evaluate)
            if self.data == "artist":
                return testCommands.virtualServer.getArtistBySong(self.rc.evaluate)
            elif self.data == "length":
                return testCommands.virtualServer.getSongLength(self.rc.evaluate)
            elif self.data == "tempo":
                return testCommands.virtualServer.getSongTempo(self.rc.evaluate)
            elif self.data == "popularity":
                return testCommands.virtualServer.getPopularity(self.rc.evaluate)
            elif self.data == "danceability":
                return testCommands.virtualServer.getDanceability(self.rc.evaluate)
            else:
                return "ERROR"

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


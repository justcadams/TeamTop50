# Binary tree for constructing and executing query commands
import keywords
import testCommands
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
        if self.isLeaf():
            return self.data
        elif self.data not in keywords.KEYWORDS:
            return "ERROR: Invalid command."
        else:
            # UNARY COMMANDS
            if self.data == "songs":
                return ', '.join(testCommands.virtualServer.getSongsByArtist(self.rc.evaluate))
            elif self.data == "artist":
                return testCommands.virtualServer.getArtistBySong(self.rc.evaluate)
            elif self.data == "length":
                return testCommands.virtualServer.getLength(self.rc.evaluate)
            elif self.data == "tempo":
                return testCommands.virtualServer.getTempo(self.rc.evaluate)
            elif self.data == "popularity":
                return testCommands.virtualServer.getPopularity(self.rc.evaluate)
            elif self.data == "danceability":
                return testCommands.virtualServer.getDanceability(self.rc.evaluate)
            elif self.data == "genre":
                return testCommands.virtualServer.getSongGenre(self.rc.evaluate)
            elif self.data == "energy":
                return testCommands.virtualServer.getEnergy(self.rc.evaluate)
            elif self.data == "loudness":
                return testCommands.virtualServer.getLoudness(self.rc.evaluate)
            elif self.data == "liveliness":
                return testCommands.virtualServer.getLiveliness(self.rc.evaluate)
            elif self.data == "valence":
                return testCommands.virtualServer.getValence(self.rc.evaluate)
            elif self.data == "acousticness":
                return testCommands.virtualServer.getAccousticness(self.rc.evaluate)
            elif self.data == "speechiness":
                return testCommands.virtualServer.getSpeechiness(self.rc.evaluate)
            elif self.data == "birthplace":
                return testCommands.virtualServer.getBirthplace(self.rc.evaluate)
            elif self.data == "birthday":
                return testCommands.virtualServer.getBirthday(self.rc.evaluate)

            # BINARY COMMANDS
            elif self.data == "more popular":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                q1 = testCommands.virtualServer.getPopularity(song1)
                q2 = testCommands.virtualServer.getPopularity(song2)
                if q1 > q2:
                    return song1
                else:
                    return song2
            elif self.data == "more danceable":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                dance1 = testCommands.virtualServer.getDanceability(song1)
                dance2 = testCommands.virtualServer.getDanceability(song2)
                if q1 > q2:
                    return song1
                else:
                    return song2
            elif self.data == "longer":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                q1 = testCommands.virtualServer.getLength(song1)
                q2 = testCommands.virtualServer.getLength(song2)
                if q1 > q2:
                    return song1
                else:
                    return song2
            elif self.data == "shorter":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                q1 = testCommands.virtualServer.getLength(song1)
                q2 = testCommands.virtualServer.getLength(song2)
                if q1 < q2:
                    return song1
                else:
                    return song2
            elif self.data == "faster":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                q1 = testCommands.virtualServer.getTempo(song1)
                q2 = testCommands.virtualServer.getTempo(song2)
                if q1 > q2:
                    return song1
                else:
                    return song2
            elif self.data == "slower":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                q1 = testCommands.virtualServer.getTempo(song1)
                q2 = testCommands.virtualServer.getTempo(song2)
                if q1 < q2:
                    return song1
                else:
                    return song2
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

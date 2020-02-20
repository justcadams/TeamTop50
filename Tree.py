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
            # UNARY COMMANDS
            if data == "songs":
                return ', '.join(commands.virtualServer.getSongsByArtist(self.rc.evaluate))
            elif data == "artist":
                return commands.virtualServer.getArtistBySong(self.rc.evaluate)
            elif data == "length":
                return commands.virtualServer.getLength(self.rc.evaluate)
            elif data == "tempo":
                return commands.virtualServer.getTempo(self.rc.evaluate)
            elif data == "popularity":
                return commands.virtualServer.getPopularity(self.rc.evaluate)
            elif data == "danceability":
                return commands.virtualServer.getDanceability(self.rc.evaluate)
            elif data == "genre":
                return commands.virtualServer.getSongGenre(self.rc.evaluate)
            elif data == "energy":
                return commands.virtualServer.getEnergy(self.rc.evaluate)
            elif data == "loudness":
                return commands.virtualServer.getLoudness(self.rc.evaluate)
            elif data == "liveliness":
                return commands.virtualServer.getLiveliness(self.rc.evaluate)
            elif data == "valence":
                return commands.virtualServer.getValence(self.rc.evaluate)
            elif data == "acousticness":
                return commands.virtualServer.getAccousticness(self.rc.evaluate)
            elif data == "speechiness":
                return commands.virtualServer.getSpeechiness(self.rc.evaluate)
            elif data == "birthplace":
                return commands.virtualServer.getBirthplace(self.rc.evaluate)
            elif data == "birthday":
                return commands.virtualServer.getBirthday(self.rc.evaluate)

            # BINARY COMMANDS
            elif data == "more popular":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                q1 = commands.virtualServer.getPopularity(song1)
                q2 = commands.virtualServer.getPopularity(song2)
                if q1 > q2:
                    return song1
                else:
                    return song2
            elif data == "more danceable":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                dance1 = commands.virtualServer.getDanceability(song1)
                dance2 = commands.virtualServer.getDanceability(song2)
                if q1 > q2:
                    return song1
                else:
                    return song2
            elif data == "longer":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                q1 = commands.virtualServer.getLength(song1)
                q2 = commands.virtualServer.getLength(song2)
                if q1 > q2:
                    return song1
                else:
                    return song2
            elif data == "shorter":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                q1 = commands.virtualServer.getLength(song1)
                q2 = commands.virtualServer.getLength(song2)
                if q1 < q2:
                    return song1
                else:
                    return song2
            elif data == "faster":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                q1 = commands.virtualServer.getTempo(song1)
                q2 = commands.virtualServer.getTempo(song2)
                if q1 > q2:
                    return song1
                else:
                    return song2
            elif data == "slower":
                song1 = self.rc.evaluate
                song2 = self.rc.evaluate

                q1 = commands.virtualServer.getTempo(song1)
                q2 = commands.virtualServer.getTempo(song2)
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

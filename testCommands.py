from Tree import *

# These are temporary test functions. This is where helper functions
# that execute SQL code will live.

def getSongArtist(song):
    if song == "Shape of You":
        return "Ed Sheeran"
    elif song == "Blank Space":
        return "Taylor Swift"
    elif song == "Bad Guy":
        return "Billie Eilish"
    else:
        return "Song not found."

def getSongLength(song):
    if song == "Shape of You":
        return "180"
    elif song == "Blank Space":
        return "155"
    elif song == "Bad Guy":
        return "162"
    else:
        return "Song not found."

def getSongTempo(song):
    if song == "Shape of You":
        return "102"
    elif song == "Blank Space":
        return "94"
    elif song == "Bad Guy":
        return "132"
    else:
        return "Song not found."

def getSongPopularity(artist):
    if artist == "Ed Sheeran":
        return "85"
    elif artist == "Billie Eilish":
        return "76"
    elif artist == "Taylor Swift":
        return "92"
    else:
        return "Song not found"


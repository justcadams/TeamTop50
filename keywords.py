UNARY_KEYWORDS = ["songs", "artist", "popularity",
                  "danceability", "genre", "length", "tempo"]
BINARY_KEYWORDS = ["more popular", "more danceable",
                   "longer", "faster", "slower"]
POLY_KEYWORDS = ["longest song", "slowest song", "fastest song",
                 "most danceable", "most popular"]

KEYWORDS = UNARY_KEYWORDS + BINARY_KEYWORDS + POLY_KEYWORDS

WORD_HELP = {"songs": "Gets a list of songs by an artist.",
             "artist": "Gets the artist of a song.",
             "popularity": "Gets the popularity of a song.",
             "danceability": "Gets the danceability of a song.",
             "genre": "Gets the genre of a song.",
             "length": "Gets the length of a song.",
             "tempo": "Gets the tempo of a song.",
             "more popular": "Gets the more popular of two songs (separated by keyword 'and'.)",
             "more danceable": "Gets the more danceable of two songs (separated by keyword 'and'.)",
             "longer": "Gets the longer of two songs (separated by keyword 'and'.)",
             "faster": "Gets the faster of two songs (separated by keyword 'and'.)",
             "slower": "Gets the slower of two songs (separated by keyword 'and'.)",
             "most popular": "Gets the most popular of a list of songs.",
             "most danceable": "Gets the most danceable of a list of songs.",
             "longest song": "Gets the longest of a list of songs",
             "fastest song": "Gets the fastest of a list of songs",
             "slowest song": "Gets the slowest of a list of songs",
             }



BUZZWORDS = ["of", "by", "get"]

 
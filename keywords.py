UNARY_KEYWORDS = ["songs", "artist", "popularity",
                  "danceability", "genre", "length",
                  "tempo", "energy", "loudness",
                  "liveliness", "valence", "acousticness",
                  "speechiness", "birthplace", "birthday"]

BINARY_KEYWORDS = ["more popular", "less popular", "more danceable", "less danceable",
                   "longer", "shorter", "faster", "slower"]

POLY_KEYWORDS = ["most popular", "least popular", "most danceable", "least danceable",
                 "longest", "shortest", "fastest", "slowest"]

GREATER_KEYWORDS = ["more popular", "more danceable", "longer", "faster", 
                    "most popular", "most danceable", "longest", "fastest"]
LESS_KEYWORDS = ["less popular", "less danceable", "shorter", "slower",
                 "least popular", "least danceable", "shortest", "slowest"]

KEYWORDS = UNARY_KEYWORDS + BINARY_KEYWORDS + POLY_KEYWORDS

WORD_HELP = {"songs": "Gets a list of songs by an artist.",
             "artist": "Gets the artist of a song.",
             "popularity": "Gets the popularity of a song.",
             "danceability": "Gets the danceability of a song.",
             "genre": "Gets the genre of a song.",
             "length": "Gets the length of a song.",
             "tempo": "Gets the tempo of a song.",
             "energy": "Gets the energy of a song.",
             "loudness": "Gets the average recording decibels.",
             "liveliness": "Gets the liveliness of a song.",
             "valence": "Gets the valence of a song.",
             "acousticness": "Gets the acoustic value of a song.",
             "speechiness": "Gets the amount of speech in a song.",
             "birthplace": "Gets the birthplace of an artist.",
             "birthday": "Gets the birthday of an artist.",
             "more popular": "Gets the more popular of two songs (separated by keyword 'and'.)",
             "less popular": "Gets the less popular of two songs (separated by keyword 'and'.)",
             "more danceable": "Gets the more danceable of two songs (separated by keyword 'and'.)",
             "less danceable": "Gets the less danceable of two songs (separated by keyword 'and'.)",
             "longer": "Gets the longer of two songs (separated by keyword 'and'.)",
             "shorter": "Gets the shorter of two songs (separated by keyword 'and'.)",
             "faster": "Gets the faster of two songs (separated by keyword 'and'.)",
             "slower": "Gets the slower of two songs (separated by keyword 'and'.)",
             "most popular": "Gets the most popular of a list of songs.",
             "least popular": "Gets the least popular of a list of songs.",
             "most danceable": "Gets the most danceable of a list of songs.",
             "least danceable": "Gets the least danceable of a list of songs.",
             "longest": "Gets the longest of a list of songs",
             "shortest": "Gets the shortest of a list of songs",
             "fastest": "Gets the fastest of a list of songs",
             "slowest": "Gets the slowest of a list of songs",
             }

HELP_WORDS_LIST= [["songs", "Gets a list of songs by an artist."],
             ["artist", "Gets the artist of a song."],
             ["popularity", "Gets the popularity of a song."],
             ["danceability", "Gets the danceability of a song."],
             ["genre", "Gets the genre of a song."],
             ["length", "Gets the length of a song."],
             ["tempo", "Gets the tempo of a song."],
             ["more popular", "Gets the more popular of two songs (separated by keyword 'and'.)"],
             ["more danceable", "Gets the more danceable of two songs (separated by keyword 'and'.)"],
             ["longer", "Gets the longer of two songs (separated by keyword 'and'.)"],
             ["faster", "Gets the faster of two songs (separated by keyword 'and'.)"],
             ["slower", "Gets the slower of two songs (separated by keyword 'and'.)"],
             ["most popular", "Gets the most popular of a list of songs."],
             ["most danceable", "Gets the most danceable of a list of songs."],
             ["longest song", "Gets the longest of a list of songs"],
             ["fastest song", "Gets the fastest of a list of songs"],
             ["slowest song", "Gets the slowest of a list of songs"],

]

BUZZWORDS = ["of", "by", "get"]

from backEnd import SQLBackEnd


virtualServer: SQLBackEnd

commandMapDict = None

def makeCommandMap(server):
    global commandMapDict
    commandMapDict = {'songs': server.getSongsByArtist,
                  'artist': server.getArtistBySong,
                  'length': server.getLength,
                  'tempo': server.getTempo,
                  'popularity': server.getPopularity,
                  'danceability': server.getDanceability,
                  'genre': server.getSongGenre,
                  'energy': server.getEnergy,
                  'loudness': server.getLoudness,
                  'liveliness': server.getLiveliness,
                  'valence': server.getValence,
                  'acousticness': server.getAcousticness,
                  'speechiness': server.getSpeechiness,
                  'birthplace': server.getBirthplace,
                  'birthday': server.getBirthday,
                  'more popular': server.getPopularity,
                  'less popular': server.getPopularity,
                  'most popular': server.getPopularity,
                  'least popular': server.getPopularity,
                  'more danceable': server.getDanceability,
                  'less danceable': server.getDanceability,
                  'most danceable': server.getDanceability,
                  'least danceable': server.getDanceability,
                  'longer': server.getLength,
                  'shorter': server.getLength,
                  'longest': server.getLength,
                  'shortest': server.getLength,
                  'faster': server.getTempo,
                  'slower': server.getTempo,
                  'fastest': server.getTempo,
                  'slowest': server.getTempo}



#POLY_KEYWORDS = ["longest song", "slowest song", "fastest song",
#                 "most danceable", "most popular"]

def commandMap():
    return commandMapDict




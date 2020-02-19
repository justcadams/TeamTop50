import testCommands
from parserA import *
import backEnd

query = 'artist "You Need to Calm Down"'
tree = parse(query)

testCommands.virtualServer = backEnd.SQLBackEnd('server.mdf')
print('Please upload Top50SpotifySongs.csv')
testCommands.virtualServer.uploadCSV('TOP50', './Top50SpotifySongs2019.csv')
print('Please upload Top50SpotifyArtists.csv')
testCommands.virtualServer.uploadCSV('TOP50ARTISTS', './Top50SpotifyArtists2019.csv')

print(testCommands.virtualServer.getArtistBySong("You Need to Calm Down"))





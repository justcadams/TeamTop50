# Import sqlite3 and relevant tools.
import os
import sqlite3
import psutil
import regex
import urllib3
import tkinter as tk
import pandas as pd
from tkinter import filedialog
from sqlite3 import Error


class SQLBackEnd:
	# databaseConnection contains a tuple with the sqlite3 connection object first and the filename string object second.
	def __init__(self, filename, debug = False):
		# Field to maintain multiple connections.
		self.databaseConnections = list()
		# Field to identify the current server this terminal is interfacing with.
		self.currentConnection = 0
		# Field to store the current connection location.
		self.currentConnectionLocation = 0
		# Field to store the current location of this terminal's cursor.
		self.currentTerminal = 0
		# Connect to the server specified.
		self.connectToServer(filename)
		# Store the user's debug setting.
		self.debug = debug

	# Requires: Nothing
	# Modifies: Nothing
	# Effects: Returns the debug setting for testing, logging, and debugging on this virtual server.

	def getDebugSetting(self):
		return self.debug

	# Requires: Boolean setting - The desired setting for testing, logging, and debugging on this virtual server.
	# Modifies: Boolean debug - The current setting for testing, logging, and debugging on this virtual server.
	# Effects: Changes the debug boolean to setting's value.

	def setDebugSetting(self, setting):
		self.debug = setting

	# Requires: String filename - The name of the file or URI for the virtual server / distant server.
	# Modifies: list(tuple(Object, filename)) databaseConnection - List containing the relevant server connection information.
	# Effects: Creates a server connection and stores the relevant information.

	def connectToServer(self, filename):
		# TODO: Mount remote file system.
		try:
			# Attempt to connect to localhost.
			newConnection = sqlite3.connect(filename)
			# Store connection and filename for later reference.
			self.databaseConnections.append(tuple((newConnection,filename)))
			# Update current connection if the server connects with this terminal.
			self.currentConnection = newConnection
			# Update current terminal to reflect the current cursor location.
			self.currentTerminal = self.newConnection.cursor()
		except Error as e:
			# If there is an error print out the error to the log.
			print(e)

	# Requires: Integer connectionNumber - The number representing the connectionNumber in the array.
	# Modifies: Nothing.
	# Effects: Changes the current connnection SQL queries are dispatched to.

	def changeConnection(self, connectionNumber):
		# Ensure the connection this terminal is changing to is within the range of available server connections.
		if(connectionNumber > -1 and connectionNumber < len(self.databaseConnections)):
			# Update the current connection to reflect this terminal's selection.
			self.currentConnection = self.databaseConnections[connectionNumber][0]
			# Update the location of this terminal's cursor.
			self.currentTerminal = self.currentConnection.cursor()

	# Requires: Nothing
	# Modifies: Nothing
	# Effects: Prints out the connection number and the virtual memory address or URI for the connections on this virtual server.

	def displayConnections(self):
		# Select all of the objects in the database connection list.
		for conn in self.databaseConnections:
			# Print out the connection uri and the filename.
			print("Connection " + str(conn[0]) + " at " + conn[1] + ".")

	# Requires: Nothing
	# Modifies: Nothing
	# Effects: Prints out the current connection's memory address or URI.

	def displayCurrentConnection(self):
		print("Connection " + str(self.currentConnection) + " is selected.")

	# Requires: Integer connectionNumber - The number representing the connectionNumber in the array.
	# Modifies: The connectionNumber specified by closing the connection and removing the connection from the databaseConnections list.
	# Effects: Disconnects from the specified server, and removes the connection from the databaseConnections list.

	def disconnectFromServer(self, connectionNumber):
		sqlite3.disconnect(self.databaseConnections[connectionNumber][0])
		self.databaseConnections.remove(connectionNumber)

	# Requires: 
	# Modifies:
	# Effects:

	def createDatabase(self, filename):
		# TODO: Mount remote file system.
		dbExists = os.path.exists(filename)
		# TODO: Create the database if it does not exist.
		# TODO: Ask the user if they want to create the database if it does exist.
		if dbExists:
			# Let the user know that the database already exists.
			print("Database " + filename + "already exists.")
			# Ask the user if they would like to overwrite the current database.
			userResponse = input("Would you like to overwrite this database? Y/N: ")
			regexCheck = False
			if regexCheck:
				print("Hacking attempt detected. Ignoring user input.")
			else:
				if (userResponse == 'Y' or userResponse == 'y'):					
					try:
						# Attempt to connect to localhost.
						newConnection = sqlite3.connect(filename)
						# Print database connection status.
						print(newConnection.sqlite3_status())
						# Store connection and filename for later reference.
						self.databaseConnection.append(tuple((newConnection,filename)))
					except Error as e:
						# Print out the error if the connection produces one.
						print(e)
					finally:
						# 
						if self.databaseConnection[-1][0]:
							self.databaseConnection[-1][0].close()
		else:
			# Let the user know that the database does not exist.
			print("No database exists in the present schema.")
			# Ask the user if they would like to overwrite the current database.
			userResponse = input("Would you like to overwrite this database? Y/N: ")
			regexCheck = False
			if regexCheck:
				print("Hacking attempt detected. Ignoring user input.")
			else:
				if(userResponse == 'Y' or userResponse == 'y'):
					try:
						# Attempt to connect to localhost.
						newConnection = sqlite3.connect(filename)
						# Print database connection status.
						print(newConnection.sqlite3_status())
						# Store connection and filename for later reference.
						self.databaseConnections.append(tuple((newConnection,filename)))
					except Error as e:
						print(e)
					finally:
						if newConnection:
							newConnection.close()

	# Requires:
	# Modifies:
	# Effects:

	def createDatabase(self, filename, databaseName):
		# TODO: Mount remote file system.
		dbExists = os.path.exists(databaseName)
		# TODO: Create the database if it does not exist.
		# TODO: Ask the user if they want to create the database if it does exist.
		if dbExists:
			# Let the user know that the database already exists.
			print("Database " + databaseName + "already exists.")
			# Ask the user if they would like to overwrite the current database.
			userResponse = input("Would you like to overwrite this database? Y/N: ")
			if userResponse:					
				try:
					# Attempt to connect to localhost.
					newConnection = sqlite3.connect(filename)
					# Print database connection status.
					print(newConnection.sqlite3_status())
					# Store connection and filename for later reference.
					self.databaseConnections.append(tuple((newConnection,filename)))
				except Error as e:
					print(e)
				finally:
					if newConnection:
						newConnection.close()
		else:
			# Let the user know that the database does not exist.
			print("No database exists in the present schema.")
			# Ask the user if they would like to overwrite the current database.
			userResponse = input("Would you like to overwrite this database? Y/N: ")
			if userResponse:					
				try:
					# Attempt to connect to localhost.
					newConnection = sqlite3.connect(filename)
					# Print database connection status.
					print(newConnection.sqlite3_status())
					# Store connection and filename for later reference.
					self.databaseConnections.append(tuple((newConnection,filename)))
				except Error as e:
					print(e)
				finally:
					if newConnection:
						newConnection.close()

	# Requires:
	# Modifies:
	# Effects:

	def uploadCSV(self, tableName):
		root = tk.Tk()
		root.withdraw()
		filePath = filedialog.askopenfilename()
		songs = pd.read_csv(filePath)
		# dtypes = {'ID': 'INTEGER', 'Track.Name': 'str', 'Artist.Name': 'str', 'Genre': 'str', 'Beats.Per.Minute': 'INTEGER', 'Energy': 'INTEGER', 'Danceability': 'INTEGER', 'Loudness': 'INTEGER', 'Liveness': 'INTEGER', 'Valence': 'INTEGER', 'Length': 'INTEGER', 'Acousticness': 'INTEGER', 'Speechiness': 'INTEGER', 'Popularity': 'INTEGER'}
		songs.to_sql('TOP50', self.currentConnection, if_exists='append', index=False)
		self.currentConnection.commit()

	# Requires:
	# Modifies:
	# Effects:

	def deleteDatabase(self, databaseName):
		if(self.regexCheck(databaseName)):
			print("Hacking attempt detected. Ignoring user input.")
		else:
			self.currentTerminal.execute("DROP " + databaseName)
			self.currentTerminal.commit()

	# Requires:
	# Modifies:
	# Effects:

	def deleteTable(self, tableName):
		if(self.regexCheck(tableName)):
			print("Hacking attempt detected. Ignoring user input.")
		else:
			self.currentTerminal.execute("DROP TABLE " + tableName)
			self.currentTerminal.commit()

	# Requires:
	# Modifies:
	# Effects:

	def deleteColumn(self, tableName, columnNames):
		if(self.regexCheck(tableName + columnNames)):
			print("Hacking attempt detected. Ignoring user input.")
		else:
			SQLCommand = "ALTER TABLE " + tableName + " DROP COLUMN "
			for name in columnNames:
				if(len(columnNames) == 1):
					SQLCommand += name
				else:
					SQLCommand += ',' + name
			self.currentTerminal.execute(SQLCommand)
			self.currentTerminal.commit()

	# Requires:
	# Modifies:
	# Effects:

	def createTable(self, tableName):
		if(self.regexCheck(tableName)):
			print("Hacking attempt detected. Ignoring user input.")
		else:
			if(type(tableName) == str):
				print("Creating table.")
				self.databaseConnection.execute("CREATE TABLE " + tableName + "(rowID INTEGER PRIMARY KEY ASC)")
			else:
				print("Table name is not a valid type.")

	# Requires:
	# Modifies:
	# Effects:

	def createTable(self, tableName, columnNames, columnDataTypes):
		checkString = tableName
		for val in columnNames:
			checkString += val
		for val in columnDataTypes:
			checkString += val
		if(self.regexCheck(checkString)):
			print("Hacking attempt detected. Ignoring user input.")
		else:				
			if(len(columnNames) == len(columnDataTypes)):
				print("Creating table.")
				SQLString = "CREATE TABLE " + tableName + "("
				for i in range(len(columnNames)):
					SQLString += columnNames[i] + " " + columnDataTypes[i] + ", "
				SQLString += ");"
			self.currentTerminal.execute(SQLString)
			self.currentTerminal.commit()

	# Requires:
	# Modifies:
	# Effects:

	def createRows(self, tableName, columnnNames, columnDataTypes, rowData):
		if(self.regexCheck(tableName + columnnNames + rowData)):
			print("Hacking attempt detected. Ignoring user input.")
		else:
			print("Inserting rows.")

	# Requires:
	# Modifies:
	# Effects:

	def selectAllFromTable(self, tableName):
		SQLString = "SELECT * FROM " + tableName
		query = self.currentTerminal.execute(SQLString).fetchall()
		self.currentConnection.commit()
		if(self.debug):
			print(query)
		return query

	# Requires:
	# Modifies:
	# Effects:

	def getObjectFromTable(self, tableName, objectName):
		SQLString = "SELECT * FROM " + tableName + " "

	# Requires:
	# Modifies:
	# Effects:

	def getSongsbyArtist(self, artistName, tableName = "TOP50"):
		SQLString = "SELECT TrackName, ArtistName FROM " + tableName + " WHERE ArtistName ='" + artistName + "'"
		query = self.currentTerminal.execute(SQLString).fetchall()
		self.currentConnection.commit()
		songList = list()
		for val in query[0]:
			songList.append(val)
		if(self.debug):
			print(SQLString)
			print(query)
			print(songList)
		return songList

	# Requires:
	# Modifies:
	# Effects:

	def getPopularityBySong(self, songName, tableName = "TOP50"):
		SQLString = "SELECT Popularity, TrackName FROM " + tableName + " WHERE TrackName ='" + songName + "'"
		query = self.currentTerminal.execute(SQLString).fetchall()
		self.currentConnection.commit()
		popularity = query[0]
		if(self.debug):
			print(SQLString)
			print(query)
			print(popularity)
		return popularity

	# Requires:
	# Modifies:
	# Effects:

	def getArtistBySong(self, songName, tableName = "TOP50"):
		SQLString = "SELECT ArtistName, TrackName FROM " + tableName + " WHERE TrackName = '" + songName + "'"
		query = self.currentTerminal.execute(SQLString).fetchall()
		self.currentConnection.commit()
		artistName = query[0]
		if(self.debug):
			print(SQLString)
			print(query)
			print(artistName)
		return artistName

	# Requires:
	# Modifies:
	# Effects:

	def getLengthBySong(self, songName, tableName = "TOP50"):
		SQLString = "SELECT Length, TrackName FROM " + tableName + " WHERE TrackName = '" + songName + "'"
		query = self.currentTerminal.execute(SQLString).fetchall()
		self.currentConnection.commit()
		songLength = query[0]
		if(self.debug):
			print(SQLString)
			print(query)
			print(songLength)
		return songLength

	# Requires:
	# Modifies:
	# Effects:

	def getDanceabilityBySong(self, songName, tableName = "TOP50"):
		SQLString = "SELECT Danceability, TrackName FROM " + tableName + " WHERE TrackName = '" + songName + "'"
		query = self.currentTerminal.execute(SQLString).fetchall()
		self.currentConnection.commit()
		danceability = query[0]
		if(self.debug):
			print(SQLString)
			print(query)
			print(danceability)
		return danceability

	# Requires:
	# Modifies:
	# Effects:

	def getDanceabilityByArtist(self, artistName, tableName = "TOP50"):
		SQLString = "SELECT Danceability, ArtistName FROM " + tableName + " WHERE ArtistName = '" + artistName + "'"
		query = self.currentTerminal.execute(SQLString).fetchall()
		self.currentConnection.commit()
		summation = 0
		for val in query:
			summation = val[0] + summation
		average = summation/len(query)
		if(self.debug):
			print(SQLString)
			print(query)
			print(average)
		return average

	# Requires:
	# Modifies:
	# Effects:

	def getPopularityByArtist(self, artistName, tableName = "TOP50"):
		SQLString = "SELECT Popularity, ArtistName FROM " + tableName + " WHERE ArtistName ='" + artistName + "'"
		query = self.currentTerminal.execute(SQLString).fetchall()
		self.currentConnection.commit()
		summation = 0
		for val in query:
			summation = val[0] + summation
		average = summation/len(query[0])
		if(self.debug):
			print(SQLString)
			print(query)
			print(average)
		return average

	# Requires:
	# Modifies:
	# Effects:

	def getLengthByArtist(self, artistName, tableName = "TOP50"):
		SQLString = "SELECT Length, ArtistName FROM " + tableName + " WHERE ArtistName ='" + artistName + "'"
		query = self.currentTerminal.execute(SQLString).fetchall()
		self.currentConnection.commit()
		summation = 0
		for val in query:
			summation = val[0] + summation
		average = summation/len(query[0])
		if(self.debug):
			print(SQLString)
			print(query)
			print(average)
		return average

	# Requires:
	# Modifies:
	# Effects:

	def regexCheck(self):
		return False

# Justin's workspace

# Testing SQLBackEnd class.
virtualServer = SQLBackEnd('test1.mdf')
virtualServer.displayConnections()
virtualServer.connectToServer('test2.mdf')
virtualServer.connectToServer('test3.mdf')
virtualServer.displayConnections()
virtualServer.changeConnection(0)
virtualServer.displayCurrentConnection()
virtualServer.uploadCSV('TOP50')
virtualServer.uploadCSV('TOP50ARTISTS')
virtualServer.selectAllFromTable('TOP50')
virtualServer.getSongsbyArtist('Marshmello')
virtualServer.getPopularityBySong('Happier')
virtualServer.getPopularityByArtist('Marshmello')
virtualServer.getDanceabilityBySong('Happier')
virtualServer.getDanceabilityByArtist('Marshmello')
virtualServer.getLengthBySong('Happier')
virtualServer.getLengthByArtist('Marshmello')

    # def getSongLength(self, SongTitle):
    #     #Open a connection with database and collect the proper row
    #     query =  self.currentTerminal.execute("SELECT " + SongTitle + "FROM ##NAME OF TABLE##")

# Matt's workspace
	# def getSongLength(self, SongTitle):
    #     #Open a connection with database and collect the proper row
    #     databaseString =  self.currentTerminal.execute("SELECT " + SongTitle + "FROM ##NAME OF TABLE##")
	#
    #     #from that row navigate to the song length and pull from table
    #     #return this integer
    #     return "getSongLength is currently being worked on"
	
	
    # def getSongTempo(self, SongTitle):
    #     databaseString = self.currentTerminal.execute("SELECT " + SongTitle + "FROM ##NAME OF TABLE##")
    #     #From connection with database find the row associated with the song
    #     #Collect bpm data from the table
    #     #return this integer
    #     return "getSongTempo is currently being worked on"
	
    # def getArtistPopularity(self, Artist):
    #     databaseString = ""
    #     # from an existing connection with database find each of the rows with songs associated with the artist
    #     # Hold each of these songs individual popularities
    #     # Perform an average calculation on these songs popularity
    #     # Return the integer associated with popularitry between 0 and 100, 100 being very popular
	
    # def getArtistDanceability(self, SongTitle):
    #     databaseString = ""
    #     # from an existing connection with database find each of the rows with songs associated with the artist
    #     # Hold each of these songs individual danceability ratings
    #     # Perform an average calculation on these song's danceability ratings
    #     # Return the integer associated with danceability between 0 and 100, 100 being very danceable



# # Establish a connection to a local database.
# conn = sqlite3('test.db')

# # Create a cursor object to execute SQL commands.
# c = conn.cursor()

# # Delete the table if it exists
# c.execute("IF EXISTS(SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='test' AND TABLE_NAME='stocks') ELSE(DROP TABLE stocks)")

# # Create a table named stocks
# c.execute("IF NOT EXISTS(SELECT * from stocks) CREATE TABLE stocks (Date VARCHAR(10), Action VARCHAR(4), Ticker VARCHAR(4), Quantity INTEGER, Price Double)")

# # Select information from the table
# c.execute("SELECT * FROM stocks")

# # Insert a row of data.
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# # Save (commit) the changes
# conn.commit()

# # Close the connection and verify the system operates as specified.
# conn.close()

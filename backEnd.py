# Import sqlite3 and relevant tools.
import os
import sqlite3
import psutil
import regex
try:
    import urllib3
except:
    pass
try:
    import Tkinter as tk
except:
    pass

import pandas as pd
try:
    import tkFileDialog as filedialog
except:
    pass
from sqlite3 import Error

class SQLBackEnd:
    # databaseConnection contains a tuple with the sqlite3 connection object first and the filename string object second.
    def __init__(self,filename):
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

        # Requires: String filename - The name of the file or URI for the virtual server / distant server.
        # Modifies: list(tuple(Object, filename)) databaseConnection - List containing the relevant server connection information.
        # Effects: Creates a server connection and stores the relevant information.

    def connectToServer(self, filename):
        # TODO: Mount remote file system.
        try:
            # Attempt to connect to localhost.
            self.newConnection = sqlite3.connect(filename)
            # Store connection and filename for later reference.
            self.databaseConnections.append(tuple((self.newConnection,filename)))
            # Update current connection if the server connects with this terminal.
            self.currentConnection = self.newConnection
            # Update current terminal to reflect the current cursor location.
            self.currentTerminal = self.newConnection.cursor()
        except Error as e:
            # If there is an error print out the error to the log.
            print(e)

    def changeConnection(self,connectionNumber):
        # Ensure the connection this terminal is changing to is within the range of available server connections.
        if(connectionNumber > -1 and connectionNumber < len(self.databaseConnections)):
            # Update the current connection to reflect this terminal's selection.
            self.currentConnection = self.databaseConnections[connectionNumber][0]
            # Update the location of this terminal's cursor.
            self.currentTerminal = self.currentConnection.cursor()

    def displayConnections(self):
        # Select all of the objects in the database connection list.
        for conn in self.databaseConnections:
            # Print out the connection uri and the filename.
            print("Connection " + str(conn[0]) + " at " + conn[1] + ".")

    def displayCurrentConnection(self):
        print("Connection " + str(self.currentConnection) + " is selected.")

    def disconnectFromServer(self,listLocation):
        sqlite3.disconnect(self.databaseConnection[listLocation][1])

    def createDatabase(self, databaseName, filename):
        # TODO: Mount remote file system.
        db_exists = os.path.exists(databaseName)
        # TODO: Create the database if it does not exist.
        # TODO: Ask the user if they want to create the database if it does exist.
        if db_exists:
            # Let the user know that the database already exists.
            print("Database " + databaseName + "already exists.")
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
                        databaseConnection.append(tuple((newConnection,filename)))
                    except Error as e:
                        print(e)
                    finally:
                        if newConnection:
                            newConnection.close()

    def createDatabase(self, filename, databaseName):
        # TODO: Mount remote file system.
        db_exists = os.path.exists(databaseName)
        # TODO: Create the database if it does not exist.
        # TODO: Ask the user if they want to create the database if it does exist.
        if db_exists:
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
                    databaseConnection.append(tuple((newConnection,filename)))
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
                    databaseConnection.append(tuple((newConnection,filename)))
                except Error as e:
                    print(e)
                finally:
                    if newConnection:
                        newConnection.close()

    def uploadCSV(self):
        self.currentConnection.text_factory = str
        root = tk.Tk()
        root.withdraw()
        filePath = filedialog.askopenfilename()
        songs = pd.read_csv(filePath)
        # dtypes = {'ID': 'INTEGER', 'Track.Name': 'str', 'Artist.Name': 'str', 'Genre': 'str', 'Beats.Per.Minute': 'INTEGER', 'Energy': 'INTEGER', 'Danceability': 'INTEGER', 'Loudness': 'INTEGER', 'Liveness': 'INTEGER', 'Valence': 'INTEGER', 'Length': 'INTEGER', 'Acousticness': 'INTEGER', 'Speechiness': 'INTEGER', 'Popularity': 'INTEGER'}
        songs.to_sql('TOP50', self.currentConnection, if_exists='append', index = False)
        self.currentConnection.commit()

    def deleteDatabase(self,databaseName):
        if(regexCheck(databaseName)):
            print("Hacking attempt detected. Ignoring user input.")
        else:
            self.currentTerminal.execute("DROP " + databaseName)
            self.currentTerminal.commit()

    def deleteTable(self, tableName):
        if(regexCheck(databaseName)):
            print("Hacking attempt detected. Ignoring user input.")
        else:
            self.currentTerminal.execute("DROP TABLE " + tableName)
            self.currentTerminal.commit()

    def deleteColumn(self, tableName, columnNames):
        if(regexCheck(databaseName)):
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


    def createTable(self,tableName):
        regexCheck = False
        if(regexCheck(tableName)):
            print("Hacking attempt detected. Ignoring user input.")
        else:
            if(type(tableName) == str):
                print("Creating table.")
                self.databaseConnection.execute("CREATE TABLE " + tableName + "(rowID INTEGER PRIMARY KEY ASC)")
            else:
                print("Table name is not a valid type.")

    def createTable(self,tableName,columnNames,columnDataTypes):
        regexCheck = False
        if(regexCheck(tableName + columnnNames + columnDataTypes)):
            print("Hacking attempt detected. Ignoring user input.")
        else:
            if(len(columnNames) == len(columnDataTypes)):
                print("Creating table.")
                SQLString = "CREATE TABLE " + tableName + "("
                for i in range(len(columnNames)):
                    SQLString += columnnNames[i] + " " + columnnDataTypes[i] + ", "
                SQLString += ");"
            self.currentTerminal.execute(SQLString)
            self.currentTerminal.commit()

    def createRows(self,tableName,columnnNames,rowData):
        if(regexCheck(tableName + columnnNames + rowData)):
            print("Hacking attempt detected. Ignoring user input.")
        else:
            print("Inserting rows.")

    def selectAll(self, tableName):
        databaseString = self.currentTerminal.execute("SELECT * FROM " + tableName)
        print(databaseString)

    def getSongLength(self, SongTitle):
        databaseString = self.currentTerminal.execute("SELECT LEN")
# Justin's workspace

# Testing SQLBackEnd class.
virtualServer = SQLBackEnd('test1.mdf')
virtualServer.displayConnections()
virtualServer.connectToServer('test2.mdf')
virtualServer.connectToServer('test3.mdf')
virtualServer.displayConnections()
virtualServer.changeConnection(0)
virtualServer.displayCurrentConnection()
#virtualServer.uploadCSV()
virtualServer.selectAll('TOP50')

# Matt's workspace


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

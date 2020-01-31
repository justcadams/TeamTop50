# Import sqlite3 tool.
import os
import sqlite3
import re
from sqlite3 import Error
from urllib.request import pathname2url

class SQLBackEnd:
	# databaseConnection contains a tuple with the sqlite3 connection object first and the filename string object second.
	def __init__(self):
		self.databaseConnection = list()
		self.currentConnection
		self.currentThread
		
		def connectToServer(self, filename):
			# TODO: Mount remote file system.
			try:
				# Attempt to connect to localhost.
				newConnection = sqlite3.connect(filename)
		        # Print database connection status.
		        print(newConnection.sqlite3_status())
		        # Store connection and filename for later reference.
				databaseConnection.append(tuple((newConnection,filename)))
				self.currentConnection = newConnection
				self.currentThread = newConnection.cursor()
		    except Error as e:
		        print(e)
		    finally:
		        if newConnection:
		            newConnection.close()

		def displayConnections:
			for conn in self.databaseConnection:
				print("Connection " + conn[0] + " at " conn[1] ".")
		
		def disconnectFromServer(self,listLocation):
			sqlite3.disconnect(self.databaseConnection[listLocation][1])

		def createDatabase(self, databaseName):
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
					break
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
				else:
					break
		
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
					break
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
				else:
					break
		
		def deleteDatabase(self,databaseName):

		def createTable(self,tableName):
			regexCheck = False
			if(regexCheck):
				print("Hacking attempt detected. Ignoring user input.")
			else:
				if(type(tableName) == str):
					print("Creating table.")
					self.databaseConnection.execute("CREATE TABLE " + tableName + "(rowID INTEGER PRIMARY KEY ASC)")
				else:
					print("Table name is not a valid type.")

		def createTable(self,tableName,columnNames,columnDataTypes):
			regexCheck = False
			if(regexCheck):
				print("Hacking attempt detected. Ignoring user input.")
			else:				
				if(len(columnNames) == len(columnDataTypes)):
					print("Creating table.")
					SQLString = "CREATE TABLE " + tableName + "("
					for i in range(len(columnNames)):
						SQLString += columnnNames[i] + " " + columnnDataTypes[i] + ", "
					SQLString += ");"
				self.databaseConnection.execute(SQLString)

		def createRows(self,tableName,columnnNames,rowData):
			regexCheck = False
			if(regexCheck):
				print("Hacking attempt detected. Ignoring user input.")
			else:
				print("Inserting rows.")


# Establish a connection to a local database.
conn = sqlite3.connect('test.db')

# Create a cursor object to execute SQL commands.
c = conn.cursor()

# Delete the table if it exists
c.execute("IF EXISTS(SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='test' AND TABLE_NAME='stocks') ELSE(DROP TABLE stocks)")

# Create a table named stocks
c.execute("IF NOT EXISTS(SELECT * from stocks) CREATE TABLE stocks (Date VARCHAR(10), Action VARCHAR(4), Ticker VARCHAR(4), Quantity INTEGER, Price Double)")

# Select information from the table
c.execute("SELECT * FROM stocks")

# Insert a row of data.
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# Close the connection and verify the system operates as specified.
conn.close()
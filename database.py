import sqlite3

# LINK SQL CHEAT SHEET
# https://cheatography.com/fetttobse/cheat-sheets/sqlite/


dataBaseConnection = sqlite3.connect("Storage.db")
cursor = dataBaseConnection.cursor()
# Command TableName (ColoumnName DataType)
cursor.execute('''CREATE TABLE IF NOT EXISTS Directory (
               ProjectPath TEXT NOT NULL)''')

def addPathSQL(path):
    cursor.execute('''INSERT INTO Directory (ProjectPath) VALUES (?)''', (path,))
    dataBaseConnection.commit()

def closeConnection(): dataBaseConnection.close()

def fetchPathData(command):
    if command == "DIR":
        cursor.execute('''SELECT ProjectPath FROM Directory''')
        rows = cursor.fetchall()
        return [row[0] for row in rows]
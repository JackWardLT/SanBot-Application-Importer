import sqlite3

# LINK SQL CHEAT SHEET
# https://cheatography.com/fetttobse/cheat-sheets/sqlite/


dataBaseConnection = sqlite3.connect("lastPath.db")
cursor = dataBaseConnection.cursor()
# Command TableName (ColoumnName DataType)
cursor.execute('''CREATE TABLE IF NOT EXISTS Directory (
               ProjectPath TEXT NOT NULL)''')

def addPathSQL(path):
    cursor.execute(''' DELETE FROM DIRECTORY''')
    cursor.execute('''INSERT INTO Directory (ProjectPath) VALUES (?)''', (path,))
    dataBaseConnection.commit()

def closeConnection(): dataBaseConnection.close()

def fetchPathData():
    cursor.execute('''SELECT ProjectPath FROM Directory''')
    rows = cursor.fetchall()
    return [row[0] for row in rows]
    
def dirCounter():
    cursor.execute('''SELECT COUNT (*) FROM Directory''')
    return (cursor.fetchone()[0] == 0)
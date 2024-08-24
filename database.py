import sqlite3

# LINK SQL CHEAT SHEET
# https://cheatography.com/fetttobse/cheat-sheets/sqlite/


dataBaseConnection = sqlite3.connect("lastPath.db")
cursor = dataBaseConnection.cursor()

testDataBaseConnection = sqlite3.connect("testDataBase.db")
testApplications = testDataBaseConnection.cursor()
# TIL DETTE SÅ MÅ VI NESTEN SE PÅ GAMMEL KODE AN UPDATE IT, FRA UTILS OG MAIN



# Command TableName (ColoumnName DataType)
cursor.execute('''CREATE TABLE IF NOT EXISTS Directory (
               ProjectPath TEXT NOT NULL)''')

testApplications.execute('''CREATE TABLE IF NOT EXISTS Applications 
                         (ApplicationPath TEXT PRIMARY KEY)''')


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



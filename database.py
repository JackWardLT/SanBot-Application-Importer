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
def closeConnectionTest(): testDataBaseConnection.close()

def fetchPathData():
    return cursor.execute('''SELECT ProjectPath FROM Directory''').fetchone()[0] # We know there is only 1 path in the table
    
def dirCounter():
    cursor.execute('''SELECT COUNT (*) FROM Directory''')
    return (cursor.fetchone()[0] == 0)




# TEST SHIT
testDataBaseConnection = sqlite3.connect("testDataBase.db")
testApplications = testDataBaseConnection.cursor()
# TIL DETTE SÅ MÅ VI NESTEN SE PÅ GAMMEL KODE AN UPDATE IT, FRA UTILS OG MAIN

testApplications.execute('''CREATE TABLE IF NOT EXISTS Applications 
                         (ApplicationPath TEXT PRIMARY KEY)''')

def addPathMemory(path):
    # Check if the path already exists
    testApplications.execute('''SELECT COUNT(*) FROM Applications WHERE ApplicationPath = ?''', (path,))
    if testApplications.fetchone()[0] == 0:
        # If the path does not exist, insert it
        testApplications.execute('''INSERT INTO Applications (ApplicationPath) VALUES (?)''', (path,))
        testDataBaseConnection.commit()
    else:
        print(f"Path '{path}' already exists in the database.")

def fetchAllApplications():
    testApplications.execute('''SELECT ApplicationPath FROM Applications''')
    return [row[0] for row in testApplications.fetchall()] # So it returns String of list and not tuples


########################################################
#   connecting to database    #
testCon = sqlite3.connect("test.db")
testCursor = testCon.cursor()

#   creating table    #
testCursor.execute('''CREATE TABLE IF NOT EXISTS test (
                   path TEXT PRIMARY KEY, 
                   recent BOOLEAN, 
                   popularity INTEGER)''')

#   update table    #
def update(path): 
    testCursor.execute('''SELECT path FROM test WHERE path = ?''', (path,))
    if not testCursor.fetchall(): 
        testCursor.execute('''INSERT INTO test (path, recent, popularity) VALUES (?, ?, ?)''', 
                           (path, True, 1))
    else:
        elements = testCursor.execute('''SELECT path, recent, popularity FROM test WHERE path = ?''', 
                                      (path, )).fetchall()
        popularNum = elements[0][2]
        testCursor.execute('''UPDATE test SET recent = ?, popularity = ? WHERE path = ?''', 
                           (True, popularNum+1, path))

    testCursor.execute('''UPDATE test SET recent = ? WHERE PATH != ?''', (False, path))

#   Find the most recent pick   #
def fetchRecent(): 
    result = testCursor.execute('''SELECT path FROM test WHERE recent = ?''', (1,)).fetchone()
    if result is None:
        return "none"  
    return result[0]

#   Creating list of popular paths without the recently picked path  #
def getPopularityList(): 
    popularityList = testCursor.execute('''SELECT path, recent, popularity 
                                        FROM test WHERE path != ?''', (fetchRecent(), )).fetchall()
    sortedList = sorted(popularityList, key=lambda x: x[2], reverse=True)
    print(sortedList)
    return [val[0] for val in sortedList]


def close():
    testCon.commit()
    testCon.close()
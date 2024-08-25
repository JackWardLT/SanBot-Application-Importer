import sqlite3



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


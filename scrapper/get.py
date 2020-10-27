def get():  
  import sqlite3

  # Connect to database
  conn = sqlite3.connect('../backend/database.db')

  cur = conn.cursor()

  cur.execute('SELECT * FROM PARTICIPANTS')
  vals = cur.fetchall()

  response = []
  for i in vals:
    x = {}
    x["id"] = i[0]
    x["name"] = i[1]
    x["questscompleted"] = i[2]
    x["last"] = i[3]
    response.append(x)
  conn.close()
  return response
def getSorted():  
  import sqlite3

  # Connect to database
  conn = sqlite3.connect('../backend/database.db')

  cur = conn.cursor()

  cur.execute('SELECT * FROM PARTICIPANTS ORDER BY QUESTS DESC')
  vals = cur.fetchall()

  response = []
  for i in vals:
    x = {}
    x["id"] = i[0]
    x["name"] = i[1]
    x["questscompleted"] = i[2]
    x["last"] = i[3]
    response.append(x)

  return response

def getNameSorted():  
  import sqlite3

  # Connect to database
  conn = sqlite3.connect('../backend/database.db')

  cur = conn.cursor()

  cur.execute('SELECT * FROM PARTICIPANTS ORDER BY NAME')
  vals = cur.fetchall()

  response = []
  for i in vals:
    x = {}
    x["id"] = i[0]
    x["name"] = i[1]
    x["questscompleted"] = i[2]
    x["last"] = i[3]
    response.append(x)

  return response

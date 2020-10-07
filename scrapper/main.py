import scrap
import sqlite3

# Connect to database
conn = sqlite3.connect('../backend/database.db')

conn.execute("""
  CREATE TABLE IF NOT EXISTS PARTICIPANTS(
    ID  TEXT  UNIQUE,
    NAME  TEXT  NOT NULL,
    QUESTS  INT  NOT NULL
  );""")

url_file = open('urls.txt', 'r')
urls = []

for i in url_file.readlines():
    urls.append(i[:-1])

total = len(urls)
tmp = 1

for i in urls:
  x = scrap.scrap(i)
  # Get the id by removing the first part of the url
  id = i.replace('https://google.qwiklabs.com/public_profiles/','')
  id = id.replace('https://www.qwiklabs.com/public_profiles/','')
  # Get the cursor
  cur = conn.cursor()

  # Check if the id exists in the database
  cur.execute("SELECT * FROM PARTICIPANTS where ID=?",(id,))
  res = cur.fetchone()

  # If it exists, update the value
  if(res):
    conn.execute("UPDATE PARTICIPANTS SET QUESTS=? WHERE ID=?",(len(x["completed_quests"]),id))
  else:
    conn.execute("INSERT INTO PARTICIPANTS VALUES(?,?,?)",(id,x["Name"], len(x["completed_quests"])))
  conn.commit()
  print('completed' , tmp , 'out of' , total)
  tmp+=1


print('Updated the database')
conn.close()



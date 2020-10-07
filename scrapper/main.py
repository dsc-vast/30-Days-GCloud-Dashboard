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


urls = [
    'https://google.qwiklabs.com/public_profiles/d4ef0024-3c99-4d8a-8a1e-432c7f90d4b5',
    'https://google.qwiklabs.com/public_profiles/2648e85b-eed1-444f-a21a-864da942d851',
    'https://google.qwiklabs.com/public_profiles/1720359b-dd55-41b5-9a30-869101cdfeb7'
  ]
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


print('Updated the database')
conn.close()



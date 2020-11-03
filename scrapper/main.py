import scrap
import sqlite3
import re

# Connect to database
conn = sqlite3.connect('../backend/database.db')

conn.execute("""
  CREATE TABLE IF NOT EXISTS PARTICIPANTS(
    ID  TEXT  UNIQUE,
    NAME  TEXT  NOT NULL,
    QUESTS  INT  NOT NULL,
    LAST  TEXT NOT NULL
  );""")

url_file = open('urls.txt', 'r')
urls = []


for i in url_file.readlines():
    urls.append(i.replace('\n',''))

total = len(urls)
tmp = 0
fail = 0
for i in urls:
  try:
    x = scrap.scrap(i)
    # Get the id by removing the first part of the url
    id = re.split('public_profiles/',i)[1] 
    # Get the cursor
    cur = conn.cursor()

    # Check if the id exists in the database
    cur.execute("SELECT * FROM PARTICIPANTS where ID=?",(id,))
    res = cur.fetchone()

    # If it exists, update the value
    if(res):
        conn.execute("UPDATE PARTICIPANTS SET QUESTS=? WHERE ID=?",(len(x["completed_quests"]),id))
    else:
        conn.execute("INSERT INTO PARTICIPANTS VALUES(?,?,?,?)",(id,x["Name"], len(x["completed_quests"]), x["last"]))
    conn.commit()
    tmp+=1
    print('completed {0} out of {1}'.format(tmp, total))
  except:
    print('Failed url: {0}'.format(i))
    fail += 1  


print('Process Completed')
print('Succes: ', tmp)
print('Fail: ', fail)
print('Updated the database')
conn.close()



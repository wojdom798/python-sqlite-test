import sqlite3
import sys

if len(sys.argv) == 2:

  db_connection = sqlite3.connect("sample_db.db")

  cursor = db_connection.cursor()

  if sys.argv[1] == "create_db":
    cursor.execute("CREATE TABLE colors (name VARCHAR(255), red int, green int, blue int)")
    cursor.execute('INSERT INTO colors VALUES ("white", 255, 255, 255)')
    cursor.execute('INSERT INTO colors VALUES ("black", 0, 0, 0)')
    cursor.execute('INSERT INTO colors VALUES ("green", 0, 255, 0)')

    db_connection.commit()

    print("database created.")
  elif sys.argv[1] == "query_db":
    cursor.execute('SELECT * FROM colors')
    data = cursor.fetchall()
    for piece in data:
      print(piece)



  db_connection.close()

else:
  print("Invalid number of arguments.")
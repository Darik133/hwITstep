import sqlite3

connection = sqlite3.connect("AnimalKingdom.sl3", timeout=15)
cur = connection.cursor()

cur.execute("CREATE TABLE Animals (ID INTEGER, name TEXT, type TEXT);")
connection.commit()

cur.execute("INSERT INTO Animals (ID, name, type) VALUES (1, 'Лев', 'Ссавець');")
connection.commit()

cur.execute("INSERT INTO Animals (ID, name, type) VALUES (2, 'Крокодил', 'Плазун');")
connection.commit()

cur.execute("INSERT INTO Animals (ID, name, type) VALUES (3, 'Орел', 'Птах');")
connection.commit()

cur.execute("INSERT INTO Animals (ID, name, type) VALUES (4, 'Морська черепаха', 'Плазун');")
connection.commit()

cur.execute("INSERT INTO Animals (ID, name, type) VALUES (5, 'Мавпа', 'Ссавець');")
connection.commit()

cur.execute("UPDATE Animals SET name = 'Сокіл' WHERE name = 'Орел'")
connection.commit()

cur.execute("SELECT * FROM Animals WHERE type = 'Ссавець'")
connection.commit()

result = cur.fetchall()
print(result)

cur.execute("SELECT * FROM Animals")
connection.commit()

result = cur.fetchall()
print(result)
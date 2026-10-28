import sqlite3

conn = sqlite3.connect("malla.db")
c = conn.cursor()

query = """
SELECT *
FROM DATOS_CARRERAS

"""

c.execute(query)
rows = c.fetchall()

for r in rows:
    print(r)

conn.close()

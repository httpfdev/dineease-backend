import sqlite3

# Kapcsolódás az SQLite adatbázishoz
conn = sqlite3.connect('dineease.db')

# Kurzor objektum létrehozása a cursor() metódussal
cursor = conn.cursor()

# SQL lekérdezés az email, lastName, és firstName kiválasztására a users táblából
query = "SELECT email, lastName, firstName FROM users"

# SQL parancs végrehajtása
cursor.execute(query)

# Az összes sor lekérdezése és kiírása
for row in cursor.fetchall():
    print(f"Email: {row[0]}, Vezetéknév: {row[1]}, Keresztnév: {row[2]}")

# Kapcsolat bezárása
conn.close()

import sqlite3

database_name = "Tvrtka.db"


select_table_query = """
SELECT * FROM Employees WHERE id=?
"""

try:
    sqlite_connection = sqlite3.connect(database_name)
    cursor = sqlite_connection.cursor()

    cursor.execute(select_table_query, (2,))

    records = cursor.fetchall()

    for record in records:
        print(record)

    cursor.close()
    print("Resursi SQLite cursor objekta su uspjesno otpusteni.")

except sqlite3.Error as error:
    print("Error: ", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija je uspjesno zatvorena!")

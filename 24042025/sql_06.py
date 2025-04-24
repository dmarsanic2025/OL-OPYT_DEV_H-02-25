import sqlite3

database_name = "Tvrtka.db"


delete_table_query = """
DELETE FROM Employees 
WHERE id = ?
"""

try:
    sqlite_connection = sqlite3.connect(database_name)
    cursor = sqlite_connection.cursor()

    cursor.execute(delete_table_query, (3,))

    sqlite_connection.commit()

    cursor.close()
    print("Resursi SQLite cursor objekta su uspjesno otpusteni.")

except sqlite3.Error as error:
    print(error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija je uspjesno zatvorena!")

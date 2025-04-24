import sqlite3

database_name = "Tvrtka.db"


update_table_query = """
UPDATE Employees 
SET name = ?, email = ?
WHERE id = ?
"""

try:
    sqlite_connection = sqlite3.connect(database_name)
    cursor = sqlite_connection.cursor()

    cursor.execute(update_table_query, ("Ana Anic Horvat", "aahorvat@gmail.com", 2))

    sqlite_connection.commit()

    cursor.close()
    print("Resursi SQLite cursor objekta su uspjesno otpusteni.")

except sqlite3.Error as error:
    print(error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija je uspjesno zatvorena!")

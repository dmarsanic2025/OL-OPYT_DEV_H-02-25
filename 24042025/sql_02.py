import sqlite3

create_table_query = """
CREATE TABLE IF NOT EXISTS Employees(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
"""
database_name = "Tvrtka.db"

try:
    sqlite_connection = sqlite3.connect(database_name)
    cursor = sqlite_connection.cursor()
    print("Baza je uspjesno kreirana te je aplikacija spojena na SQLite.")

    cursor.execute(create_table_query)

    sqlite_connection.commit()

    print("Nova tabela Employees je uspjesno kreirana")

    cursor.close()
    print("Resursi SQLite cursor objekta su uspjesno otpusteni.")

except sqlite3.Error as error:
    print("Error: ", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija je uspjesno zatvorena!")

import sqlite3


select_query = "SELECT sqlite_version();"


try:
    sqlite_connection = sqlite3.connect("sqlite_python.db")

    cursor = sqlite_connection.cursor()

    print("Baza je uspjesno kreirana te je aplikacija spojena na SQLite.")

    cursor.execute(select_query)

    records = cursor.fetchone()

    print(f"SQLite verzija je : {records}")

    cursor.close()
    print("Resursi SQLite cursor objekta su uspjesno otpusteni.")
except sqlite3.Error as error:
    print("Error: ", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija je uspjesno zatvorena!")

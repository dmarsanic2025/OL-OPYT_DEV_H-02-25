import sqlite3

database_name = "Tvrtka.db"


insert_into_table_query = """
INSERT INTO Employees (name, email) VALUES (?, ?)
"""

lista_djelatnika = [
    ("Petar Peric", "pperic@email.com"),
    ("Ana Anic", "aanic@gmail.com"),
    ("Kresimir Horvat", "kperic123@yahoo.com"),
]

try:
    sqlite_connection = sqlite3.connect(database_name)
    cursor = sqlite_connection.cursor()

    for djelatnik in lista_djelatnika:
        cursor.execute(insert_into_table_query, djelatnik)

    sqlite_connection.commit()

    cursor.close()
    print("Resursi SQLite cursor objekta su uspjesno otpusteni.")

except sqlite3.Error as error:
    print("Error: ", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija je uspjesno zatvorena!")

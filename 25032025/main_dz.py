from sqlite_repo import (
    create_connection,
    create_table,
    create_employee,
    update_employee,
    delete_employee,
    delete_all_employees,
    select_all_employees,
    select_employees_by_id,
)

# Putanja do SQLite baze
database = r"TvrtkaDb.db"  # promijeni prema potrebi

# SQL upit za kreiranje Employees tablice
sql_create_employees_table = """
CREATE TABLE IF NOT EXISTS Employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
"""

def main():
    # Korak 1: Kreiraj konekciju prema bazi
    db_connection = create_connection(database)

    # Korak 2: Ako postoji konekcija, kreiraj tablicu
    if db_connection is not None:
        with db_connection:
            create_table(db_connection, sql_create_employees_table)

            # Očisti tablicu prije testiranja
            delete_all_employees(db_connection)

            # Dodaj nove djelatnike
            djelatnik1 = ('Ivan Horvat', 'ivan@example.com')
            djelatnik2 = ('Ana Kovač', 'ana@example.com')

            id1 = create_employee(db_connection, djelatnik1)
            id2 = create_employee(db_connection, djelatnik2)

            print("Nakon dodavanja:")
            select_all_employees(db_connection)

            # Ažuriraj djelatnika
            updated_djelatnik = ('Ivan H.', 'ivan.h@example.com', id1)
            update_employee(db_connection, updated_djelatnik)

            print("\nNakon ažuriranja Ivana:")
            select_all_employees(db_connection)

            # Dohvati po ID
            print(f"\nDohvat djelatnika po ID {id2}:")
            select_employees_by_id(db_connection, id2)

            # Obriši jednog djelatnika
            delete_employee(db_connection, id1)

            print("\nNakon brisanja Ivana:")
            select_all_employees(db_connection)
    else:
        print("Greška pri povezivanju s bazom podataka.")

if __name__ == '__main__':
    main()

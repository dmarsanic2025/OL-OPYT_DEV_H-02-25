import sqlite3

def create_connection(db_file):
    """ 
    Kreira konekciju prema SQLite bazi podataka
    Ako baza ne postoji, kreirat ce novu 
    :param db_file: Putanja do SQLite db datoteke
    :return: SQLite db connection objekt
    """
    pass


def create_table(db_connection, create_table_sql):
    """ Kreira tabelu definiranu u create_table_sql parametru
    :param db_connection: SQLite db connection objekt
    :param create_table_sql: Tekstualna varijable s CREATE TABLE upitom
    :return:
    """
    pass


def create_employee(db_connection, djelatnik):
    """ Kreira novi red u tabeli Employees na osnovu podataka pohranjenih u djelatnik paramateru tipa tuple
    :param db_connection: SQLite db connection objekt
    :param djelatnik: Tuple s podacima o djelatniku
    :return: id novog retka s podacima o djelatniku
    """
    pass


def update_employee(db_connection, djelatnik):
    """
    Azurira podtke o Djelatniku
    :param db_connection: SQLite db connection objekt
    :param djelatnik: Tuple s podacima o djelatniku
    :return: None
    """
    pass


def delete_employee(db_connection, id):
    """
    Brise zapis o djelatniku u tabeli na osnovu ID broja retka
    :param db_connection: SQLite db connection objekt
    :param id: id retka djelatnika
    :return: None
    """
    pass


def delete_all_employees(db_connection):
    """
    Brise sve zapise o djelatnicima iz tabele
    :param db_connection: SQLite db connection objekt
    :return: None
    """
    pass


def select_all_employees(db_connection):
    """
    Dohvaca sve zapise o djelatnicima
    :param db_connection: SQLite db connection objekt
    :return: print redak
    """
    pass


def select_employees_by_id(db_connection, id):
    """
    Dohvaca zapise o djelatniku na osnovu ID broja
    :param db_connection: SQLite db connection objekt
    :param id: id retka djelatnika
    :return: print redak
    """
    pass

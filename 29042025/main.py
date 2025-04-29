import sqlalchemy as db

db_engine = db.create_engine("sqlite:///Tvrtka.db")

db_connection = db_engine.connect()

db_metadata = db.MetaData()

employees = db.Table("Employees", db_metadata, autoload_with=db_engine)

id_column = employees.columns.id
email_column = employees.columns.email
name_column = employees.columns.name

sql_select_query = db.select(name_column, email_column).select_from(employees)

result_proxy = db_connection.execute(sql_select_query)

results = result_proxy.fetchone()

for row in results:
    print(row)

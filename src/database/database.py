import psycopg2


class Database:

    def __init__(self, host, dbname, user, password):
        self.connection = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def create_table(self, table_name, values):
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} ({values})""")
        self.connection.commit()

    def insert(self, table_name, values):
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({','.join(['?' for _ in values])})", values)
        self.connection.commit()

    def delete_one(self, table_name, identity):
        self.cursor.execute(f"DELETE from {table_name} WHERE identity=(?)", identity)
        self.connection.commit()

    def show_all(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        self.connection.commit()


def create_warehouse_db(db):

    db.create_table('workers', 'identity INTEGER, name TEXT, surname TEXT, age INTEGER, experience INTEGER, '
                               'job TEXT, change TEXT')

    db.create_table('warehouse_operators', 'identity INTEGER, name TEXT, surname TEXT, age INTEGER, experience INTEGER,' 
                                           ' job TEXT, change TEXT, amount_of_done_tasks INTEGER')

    db.create_table('leaders', 'identity INTEGER, name TEXT, surname TEXT, age INTEGER, '
                               'experience INTEGER, change TEXT')

    db.create_table('')


def insert_data_to_warehouse_db(obj, db, table_name: str):
    if table_name == 'Workers':
        db.insert(table_name, (obj.identity, obj.name, obj.surname, obj.age, obj.experience, obj.job, obj.change))

    if table_name == 'WarehouseOperators':
        db.insert(table_name, (obj.identity, obj.name, obj.surname, obj.age, obj.experience, obj.job, obj.change,
                               sum(obj.tasks_done)))

    if table_name == 'Leaders':
        db.insert(table_name, (obj.identity, obj.name, obj.surname, obj.age, obj.experience, obj.change))

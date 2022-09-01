import sqlite3


class Database:

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def create_table(self, table_name, values):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXIST {table_name}({values})''')
        self.connection.commit()

    def insert(self, table_name, values):
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({','.join(['?' for _ in values])}", values)
        self.connection.commit()

    def delete_one(self, table_name, identity):
        self.cursor.execute(f"DELETE from {table_name} WHERE identity=(?)", identity)
        self.connection.commit()

    def show_all(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")


def create_database(database):

    database.create_table('workers', 'identity INTEGER, name TEXT, surname TEXT, age INTEGER, experience INTEGER,'
                                     'tasks INTEGER, operator TEXT')
    database.create_table('warehouse_operators', 'identity INTEGER, name TEXT, surname TEXT, age INTEGER, '
                                                 'experience INTEGER, tasks INTEGER')
    database.create_table('components', 'location TEXT, index_number INTEGER, quantity INTEGER')

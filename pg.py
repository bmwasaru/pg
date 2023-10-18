import psycopg2
import psycopg2.extras

class Database:
    def __init__(self, db_url):
        self.db_url = db_url

    def get_connection(self):
        return psycopg2.connect(self.db_url)

    def execute(self, query, params=None):
        # perform operations that modify the database, such as inserting, updating, or deleting records
        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                connection.commit()

    def get(self, query, params=None):
        # retrieve a single result
        with self.get_connection() as connection:
            with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()

    def query(self, query, params=None):
        # retrieve multiple results
        with self.get_connection() as connection:
            with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()

    def row_to_obj(self, row):
        # converts an SQL row (returned by the psycopg2 library) to an instance of the RowObject class
        return RowObject(row)

class RowObject:
    """RowObject class, which supports both dictionary-style and attribute-style access"""
    def __init__(self, row):
        self._row = row

    def __getattr__(self, name):
        if name in self._row:
            return self._row[name]
        raise AttributeError(f"'RowObject' object has no attribute '{name}'")

    def __getitem__(self, key):
        return self._row.get(key)

    def __repr__(self):
        return f"<RowObject {self._row}>"

import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'codingdojo',
            'db': db,
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor,
            'autocommit': False
        }
        self.connection = pymysql.connect(**self.config)

    def query_db(self, query: str, data: dict = None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query)
                
                if query.lower().startswith("insert"):
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().startswith("select"):
                    return cursor.fetchall()
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
            # Don't close the connection in finally, because you might want to run multiple queries

    def close_connection(self):
        self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)
import psycopg2
import psycopg2.extras
from psycopg2.extras import Json
import json
import pandas.io.sql as sqlio


class PGBase():
    def __init__(self, _dbName, _user, _host, _pass):
        try:
            self.dbconn = psycopg2.connect(f"dbname='{_dbName}' user='{_user}' host='{_host}' password='{_pass}'")
        except psycopg2.Error as e:
            print("---- Failed to connect to the database")
            print(f"The error message is {e}")

    def queryData(self, _query):
        try:
            __cursor = self.dbconn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            __cursor.execute(_query)
            #return json.dumps(__cursor.fetchall())
            return __cursor.fetchall()
        except Exception as e:
            print(f"Failed to run query {e}")
            return None

    def executeQuery(self, _query):
        try:
            __cursor = self.dbconn.cursor()
            __cursor.execute(_query)
        except Exception as e:
            print(f"Failed to run query {e}")
            return None

    def fetchDataFrame(self, _query):
        try:
            return sqlio.read_sql_query(_query, self.dbconn)
        except Exception as e:
            print(f"Failed to run query {e}")
            return None

    def fetchiDataJson(self, _query):
        try:
            __cursor = self.dbconn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            __cursor.execute(_query)
            return __cursor.fetchall()
        except Exception as e:
            print(f"Failed to run query {e}")
            return None

    def commit(self):
        self.dbconn.commit()

if __name__ == "__main__":
    __dbBase = PGBase("cryptodb", "cryptouser", "192.168.1.166", "cryptouser")
    __ret = __dbBase.queryData("select to_char(current_timestamp, 'YYYY-MM-DD') as test")
    print(f"The retrn datais {__ret}")

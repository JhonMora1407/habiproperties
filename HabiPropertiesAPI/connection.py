import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


class Connection:

    def __init__(self):
        config = {
            "host": os.getenv('DB_HOST'),
            "port": int(os.getenv('DB_PORT')),
            "database": os.getenv('DB_DATABASE'),
            "user": os.getenv('DB_USER'),
            "password": os.getenv('DB_PASS')
        }
  
        try:
            self.connection = pymysql.Connect(**config)
        except Exception as e:
            print("Something went wrong:", e)

    def get_queryset(self, query):

        property = []

        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)

            return self.cursor.description, self.cursor.fetchall()
        except:
            raise
        finally:
            self.cursor.close()

import sqlite3
import json
from contextlib import contextmanager

class Database():
    def __init__(self, config_path):
        try:
            with open(config_path, 'r') as file:
                self.config_file = json.load(file)
                self.config = self.config_file["database_info"]
                self.config["timeout"] = 10
        except FileNotFoundError:
            print(f"Error : file '{config_path}' not found")
        except json.JSONDecodeError as e:
            print(f'JSON Error : {e}')
        
    @contextmanager
    def get_connection(self):
        connection = sqlite3.connect(**self.config)
        try:
            yield connection
        finally:
            connection.close()
    
    def test_connection(self):
        try:
            with self.get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                if result and result[0] == 1:
                    return True
                else:
                    return False
        except sqlite3.Error as err:
            print(f"Error : {err}")
            return False
    
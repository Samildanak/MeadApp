import mariadb
import json
from contextlib import contextmanager

class Database():
    def __init__(self, config_path):
        try:
            with open(config_path, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print(f"Error : file '{config_path}' not found")
        except json.JSONDecodeError as e:
            print(f'JSON Error : {e}')
        
    @contextmanager
    def get_connection(self):
        connection = mariadb.connect(**self.config)
        try:
            yield connection
        finally:
            connection.close()
    
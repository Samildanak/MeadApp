import sqlite3
import json
from contextlib import contextmanager

class Database():
    def __init__(self, config_path):
        try:
            with open(config_path, 'r+') as file:
                self.config_file = json.load(file)
                self.config = self.config_file["database_info"]
                self.config["timeout"] = 10
                if self.config_file["initialisation_info"]["first_launch"] == "yes":
                        self.initialize_database()
                        self.config_file["initialisation_info"]["first_launch"] = "no"
                        file.seek(0)
                        json.dump(self.config_file, file)
                        file.truncate()
        except FileNotFoundError:
            print(f"Error : file '{config_path}' not found")
        except json.JSONDecodeError as e:
            print(f'JSON Error : {e}')
    
    def initialize_database(self):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE recipe(recipe_id INTEGER PRIMARY KEY ASC, name, initial_date, volume, " \
                "predicted_alcohol, residual_sugar, honey_quantity, yeast_id, " \
                "fermaid_k, initial_brix, actual_brix, note)")
            cursor.execute("CREATE TABLE yeast_type(yeast_id INTEGER PRIMARY KEY ASC, yeast_name)")
            connection.commit()
        
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
    
    
from PySide6.QtWidgets import QDialog, QMessageBox
import json
from db_connection import Database

from MeadApp.ui_GetDatabasePath import Ui_GetDatabasePath

class DatabasePathWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GetDatabasePath()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)        

        self.ui.username.setFocus()
        self.ui.next.clicked.connect(self.onNextButtonClick)
        self.ui.cancel.clicked.connect(self.close)

    def onNextButtonClick(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            self.saveConfiguration()
        elif self.ui.stackedWidget.currentIndex() == 1:
            self.saveDatabaseSelection()
            with self.db.get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(f"USE {self.database_selected}")
                connection_success = self.db.test_connection()
                if connection_success:
                    self.ui.stackedWidget.setCurrentIndex(2)
                    self.enablePage3(cursor)

    def saveConfiguration(self):
        path = "./config/configuration.json"
            #connection_info_name.touch(exist_ok=True)
        config = {
            "username": self.ui.username.text(),
            "password": self.ui.password.text(),
            "host": self.ui.host.text(),
            "port": int(self.ui.port.text())
        }

        with open(path, "r+") as configuration_file:
            data = json.load(configuration_file)
            data["database_info"] = config
            configuration_file.seek(0)
            json.dump(data, configuration_file)
            configuration_file.truncate()

        return self.confirmConnection(path)

    def confirmConnection(self, database_config):
        self.db = Database(config_path=database_config)
        if self.db.test_connection():
            self.ui.stackedWidget.setCurrentIndex(1)
            self.enablePage2()
        else:
            msgBox = QMessageBox(text='The connection to the database failed')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.buttonClicked.connect(msgBox.close)
            msgBox.exec()
    
    def enablePage2(self):
        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")
            result = cursor.fetchall()

            if result:
                for database in result:
                    self.ui.database_available.addItem(database[0])
    
    def saveDatabaseSelection(self):
        path = "./config/configuration.json"
        self.database_selected = self.ui.database_available.currentText()

        with open(path, "r+") as configuration_file:
            data = json.load(configuration_file)
            data["database_info"]["database"] = self.database_selected
            data["initialisation_info"]["first_launch"] = "no"
            configuration_file.seek(0)
            json.dump(data, configuration_file)
            configuration_file.truncate()
    
    def enablePage3(self, cursor):
        cursor.execute("SHOW TABLES")
        tables_available = cursor.fetchall()
        if tables_available:
            for table in tables_available:
                self.ui.table_available.addItem(table[0])
        
        self.ui.next.setText("Finish")
        self.ui.next.clicked.connect(self.close)
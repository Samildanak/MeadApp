from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QApplication, QMessageBox, QFileDialog
import json
import sys

from MeadApp.ui_GetDatabasePath import Ui_GetDatabasePath

class DatabasePathWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GetDatabasePath()
        self.ui.setupUi(self)
        self.enablePath()

        self.ui.jsonConfigExist.toggled.connect(self.enablePath)
        self.ui.jsonConfigNotExist.toggled.connect(self.enableConfiguration)
        self.ui.browse.clicked.connect(self.browseForJsonFile)

        self.ui.buttonBox.accepted.connect(self.saveConfiguration)
        self.ui.buttonBox.rejected.connect(self.close)

    def enableConfiguration(self):
        if self.ui.jsonConfigNotExist.isChecked():
            # Enable actived LineEdit
            self.ui.username.setEnabled(True)
            self.ui.password.setEnabled(True)
            self.ui.host.setEnabled(True)
            self.ui.port.setEnabled(True)
            self.ui.username.setStyleSheet("")
            self.ui.password.setStyleSheet("")
            self.ui.host.setStyleSheet("")
            self.ui.port.setStyleSheet("")

            # Disable inactive button and LineEdit
            self.ui.pathLine.setEnabled(False)
            self.ui.browse.setEnabled(False)
            self.ui.pathLine.setStyleSheet("""
                background-color: lightgray;
                """)

    def enablePath(self):
        if self.ui.jsonConfigExist.isChecked():
            # Disable inactive LineEdit
            self.ui.username.setEnabled(False)
            self.ui.password.setEnabled(False)
            self.ui.host.setEnabled(False)
            self.ui.port.setEnabled(False)
            self.ui.username.setStyleSheet("background-color: lightgray;")
            self.ui.password.setStyleSheet("background-color: lightgray;")
            self.ui.host.setStyleSheet("background-color: lightgray;")
            self.ui.port.setStyleSheet("background-color: lightgray;")

            # Enable actived LineEdit
            self.ui.pathLine.setEnabled(True)
            self.ui.browse.setEnabled(True)
            self.ui.pathLine.setStyleSheet("")

    def browseForJsonFile(self):
        filename = QFileDialog.getOpenFileName(self,
                                               "Open Configuration Database File",
                                               "/home",
                                               "Config File (*.json)")
        print(filename)
        self.ui.pathLine.setText(filename[0])

    def saveConfiguration(self):
        if self.ui.jsonConfigExist.isChecked():
            path = self.ui.pathLine.text()
        elif self.ui.jsonConfigNotExist.isChecked():
            path = "../data/connection_info.json"
            config = {
                "username": self.ui.username.text(),
                "password": self.ui.password.text(),
                "host": self.ui.host.text(),
                "port": self.ui.port.text()
            }
            json_config = json.dumps(config, indent=4)

            with open("../data/connection_info.json", "w+") as connection_info:
                connection_info.write(json_config)
                connection_info.close()

        db_path = {
            "db_config_file": path
        }
        db_path_json = json.dumps(db_path, indent=4)
        with open("../config/config.json", "w+") as config_file:
            config_file.write(db_path_json)
            config_file.close

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DatabasePathWindow()
    widget.show()
    sys.exit(app.exec())
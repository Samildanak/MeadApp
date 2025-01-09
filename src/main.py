# This Python file uses the following encoding: utf-8
# Import system libraries
import sys
from datetime import datetime
import mariadb
import json
import os

# Import calculation library
import meadCalculation as mC

# Import User Database library
from db_connection import Database

from db_config_window import DatabasePathWindow

# Import Qt libraries
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QHeaderView, QTableView, QMessageBox
from PySide6.QtCore import QDate, Signal, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem

# Import UI Windows
from MeadApp.ui_MainWindow import Ui_MainWindow
from MeadApp.ui_NewRecipe import Ui_NewRecipeWindow
from MeadApp.ui_AddYeast import Ui_Dialog
from MeadApp.ui_ShowRecipe import Ui_ShowRecipeWindow
from MeadApp.ui_SelectedRecipe import Ui_SelectedRecipe

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.configuration_path = "./config/configuration.json"

        with open(self.configuration_path, 'r') as configuration:
            json_config = json.load(configuration)
            if json_config["initialisation_info"]["first_launch"] == "yes":
                msgBox = QMessageBox(text='This is your first launch of Mead Designer. \n We need to configure the Database you will use for your recipe')
                msgBox.setWindowTitle("Informative Window")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.buttonClicked.connect(msgBox.close)
                msgBox.exec()
                databaseConfigurationWindow = DatabasePathWindow(parent=self)
                databaseConfigurationWindow.exec()
       
        self.db = Database(config_path=self.configuration_path)

        if self.db.test_connection():
            self.ui.connectionStatus.setText("Connected")
            self.ui.connectionStatus.setStyleSheet("background-color: green;")
        else:
            self.ui.connectionStatus.setText("Not Connected")
            self.ui.connectionStatus.setStyleSheet("background-color: red;")

        self.ui.newRecipeButton.clicked.connect(self.onNewRecipeClicked)
        self.ui.showRecipeButton.clicked.connect(self.onShowRecipeClicked)

        self.ui.actionConnect.triggered.connect(self.onConnect)
        self.ui.actionChange_Database_Configuration.triggered.connect(self.onChangeConfiguration)

    def onNewRecipeClicked(self):
        newRecipe = NewRecipeWindow(parent = self, db = self.db)
        newRecipe.show()
    
    def onShowRecipeClicked(self):
        showRecipe = ShowRecipeWindow(parent = self, db = self.db)
        showRecipe.show()
    
    def onChangeConfiguration(self):
        print("Click")

    def onConnect(self):
        print("CLicki")

class NewRecipeWindow(QMainWindow):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.newRecipeUi = Ui_NewRecipeWindow()
        self.newRecipeUi.setupUi(self)
        self.dataList = []
        self.updateYeast = False
        self.db = db

        try:
            with self.db.get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT recipe_id FROM recipe ORDER BY recipe_id DESC LIMIT 1")
                result = cursor.fetchone()
            self.batchId = result[0] + 1
        except:
            self.batchId = 1
        today = datetime.now()

        self.loadYeastItem()

        self.newRecipeUi.batch_label.setText("Batch n°" + str(self.batchId))
        self.newRecipeUi.date_box.setDate(QDate.currentDate())
        self.newRecipeUi.honey_button.clicked.connect(self.calculateHoney)
        self.newRecipeUi.save_box.clicked.connect(self.savingRecipe)
        self.newRecipeUi.add_yeast_button.clicked.connect(self.addYeast)

    def calculateHoney(self):
        volume = self.newRecipeUi.volume_box.value()
        alcoholicConcentration = self.newRecipeUi.alcohol_box.value()
        residualSugar = self.newRecipeUi.sugar_box.value()

        honeyMass = mC.calculate_honey(volume, alcoholicConcentration, residualSugar)

        self.newRecipeUi.honey_box.setValue(honeyMass)

    def savingRecipe(self):
        name = self.newRecipeUi.name_box.text()
        volume = str(self.newRecipeUi.volume_box.value())
        alcoholicConcentration = str(self.newRecipeUi.alcohol_box.value())
        residualSugar = str(self.newRecipeUi.sugar_box.value())
        honeyMass = str(self.newRecipeUi.honey_box.value())
        fermaidK = 1 if self.newRecipeUi.fermaid_box.isChecked() else 0
        notes = self.newRecipeUi.note_box.toPlainText()
        date = self.newRecipeUi.date_box.date().toString("yyyy-MM-dd")
        yeast = self.newRecipeUi.comboBox.currentText()
        initialBrix = str(self.newRecipeUi.initial_brix.value())
        actualBrix = initialBrix

        # Insert new recipe in Database
        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT yeast_id FROM yeast_type WHERE yeast_name=%s", (yeast,))
            result = cursor.fetchone()
            try:
                if result is None:
                    raise ValueError("Yeast not found")
                else:
                    yeast_id = result[0]
            except ValueError as e:
                print(f"Error : {e}")

            insert_query = """
                INSERT INTO recipe (name, initial_date, volume, predicted_alcohol, residual_sugar, honey_quantity, yeast_id, fermaid_k, initial_brix, actual_brix, note)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)            
            """

            try:
                cursor.execute(insert_query, (name,
                                              date,
                                              volume,
                                              alcoholicConcentration,
                                              residualSugar,
                                              honeyMass,
                                              yeast_id,
                                              fermaidK,
                                              initialBrix,
                                              actualBrix,
                                              notes,))
                connection.commit()
                print("New Recipe successfully added")
            except mariadb.Error as err:
                print(f"Error : {err}")
                connection.rollback()

        self.close()

    def loadYeastItem(self):
        self.newRecipeUi.comboBox.clear()

        try:
            with self.db.get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT yeast_name FROM yeast_type")
                result = cursor.fetchall()

            for row in result:
                self.newRecipeUi.comboBox.addItem(row[0])
        except mariadb.Error as e:
            print(f"Error : {e}")
            connection.rollback()
    
    def addYeast(self):
        newYeast = NewYeastWindow(parent = self, db = self.db)
        newYeast.yeastTableUpdated.connect(self.loadYeastItem)
        newYeast.show()

class NewYeastWindow(QDialog):
    yeastTableUpdated = Signal()

    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.newYeastUi = Ui_Dialog()
        self.newYeastUi.setupUi(self)
        self.db = db

        self.newYeastUi.buttonBox.accepted.connect(self.saveNewYeast)
        self.newYeastUi.buttonBox.rejected.connect(self.close)        
    
    def saveNewYeast(self):
        newYeast = self.newYeastUi.lineEdit.text()
        yeast_exist = False

        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT yeast_name FROM yeast_type")
            result = cursor.fetchall()
            for yeast in result:
                if newYeast == yeast[0]:
                    print("Yeast already exist in Database")
                    yeast_exist = True
            
            if  not yeast_exist:
                try:
                    cursor = connection.cursor()
                    cursor.execute("""INSERT INTO yeast_type (yeast_name) 
                                VALUES (%s)""", (newYeast,))
                    connection.commit()
                    print("New Yeast added succesfully")
                except mariadb.Error as err:
                    print(f"Error : {err}")

        self.closeEvent(None)
        self.close()
    
    def closeEvent(self, event):
        self.yeastTableUpdated.emit()
        if event:
            event.accept()

class ShowRecipeWindow(QMainWindow):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.showRecipeUi = Ui_ShowRecipeWindow()
        self.showRecipeUi.setupUi(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Batch_Id", "Name"])

        self.showRecipeUi.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.showRecipeUi.tableView.setSelectionBehavior(QTableView.SelectRows)
        self.showRecipeUi.tableView.setModel(self.model)

        self.showRecipeUi.tableView.setColumnWidth(0, 80)
        header = self.showRecipeUi.tableView.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        self.db = db

        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT recipe_id, name FROM recipe")
            result = cursor.fetchall()

            for recipe in result:
                recipe_id = QStandardItem(str(recipe[0]))
                recipe_id.setTextAlignment(Qt.AlignCenter)
                name = QStandardItem(recipe[1])
                name.setTextAlignment(Qt.AlignCenter)
                modelRow = [recipe_id, name]
                self.model.appendRow(modelRow)                
        
        self.showRecipeUi.ConfirmBox.accepted.connect(self.showRecipe)
        self.showRecipeUi.ConfirmBox.rejected.connect(self.close)

    def showRecipe(self):
        recipe_selected = self.showRecipeUi.tableView.selectedIndexes()
        if recipe_selected:
            index_id = recipe_selected[0]
            recipe_batch_id = self.model.item(index_id.row(), index_id.column()).text()
            recipeModificationWindow = RecipeModificationWindow(parent=self, batch_id=recipe_batch_id, db=self.db)
            recipeModificationWindow.show()

class RecipeModificationWindow(QMainWindow):
    def __init__(self, db, parent=None, batch_id: str = ""):
        super().__init__(parent)
        self.recipeModificationUi = Ui_SelectedRecipe()
        self.recipeModificationUi.setupUi(self)

        self.batch_id = batch_id

        self.updateYeast = False

        self.db = db

        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT name, initial_date, volume, honey_quantity, yeast_id, fermaid_k, initial_brix, actual_brix, note 
                           FROM recipe WHERE recipe_id = %s""", (self.batch_id,))
            recipe = cursor.fetchone()
        
        self.loadYeastItem(recipe[4])

        self.recipeModificationUi.name_box.setText(recipe[0])
        self.recipeModificationUi.date_box.setDate(recipe[1])
        self.recipeModificationUi.volume_box.setValue(float(recipe[2]))
        self.recipeModificationUi.honey_box.setValue(float(recipe[3]))
        self.recipeModificationUi.fermaid_box.setChecked(True if recipe[5] == "Yes" else False)
        self.recipeModificationUi.initial_brix.setValue(float(recipe[6]))
        self.recipeModificationUi.actual_brix.setValue(float(recipe[7]))
        self.recipeModificationUi.note_box.setPlainText(recipe[8])
        self.updateAlcoholLabel()

        self.recipeModificationUi.actual_brix.valueChanged.connect(self.updateAlcoholLabel)
        self.recipeModificationUi.initial_brix.valueChanged.connect(self.updateAlcoholLabel)
        self.recipeModificationUi.save_box.clicked.connect(self.savingRecipe)
        self.recipeModificationUi.add_yeast_button.clicked.connect(self.addYeast)

    def updateAlcoholLabel(self):
        initial_brix = self.recipeModificationUi.initial_brix.value()
        actual_brix = self.recipeModificationUi.actual_brix.value()

        alcohol_concentration = mC.calculate_alcool_brix(initial_brix, actual_brix)

        self.recipeModificationUi.calculated_alcohol_concentration.setText(str(alcohol_concentration))

    
    def loadYeastItem(self, yeast_id):
        self.recipeModificationUi.comboBox.clear()

        try:
            with self.db.get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT yeast_name FROM yeast_type")
                result = cursor.fetchall()

            for row in result:
                self.recipeModificationUi.comboBox.addItem(row[0])
            self.recipeModificationUi.comboBox.setCurrentIndex(yeast_id-1)
        except mariadb.Error as e:
            print(f"Error : {e}")
            connection.rollback()

    def savingRecipe(self):
        update_query = """UPDATE recipe 
            SET name = %s, volume = %s, fermaid_k = %s, note = %s, initial_date = %s, yeast_id = %s, initial_brix = %s, actual_brix = %s
            WHERE recipe_id = %s"""

        name = self.recipeModificationUi.name_box.text()
        volume = str(self.recipeModificationUi.volume_box.value())
        fermaidK = 1 if self.recipeModificationUi.fermaid_box.isChecked() else 0
        notes = self.recipeModificationUi.note_box.toPlainText()
        date = self.recipeModificationUi.date_box.date().toString("yyyy-MM-dd")
        yeast = self.recipeModificationUi.comboBox.currentText()
        initialBrix = str(self.recipeModificationUi.initial_brix.value())
        actualBrix = str(self.recipeModificationUi.actual_brix.value())

        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT yeast_id FROM yeast_type WHERE yeast_name=%s", (yeast,))
            result = cursor.fetchone()
            yeast_id = result[0]

            try:
                cursor.execute(update_query, (name,
                                            volume,
                                            fermaidK,
                                            notes,
                                            date,
                                            yeast_id,
                                            initialBrix,
                                            actualBrix,
                                            self.batch_id))
                connection.commit()
                print("Recipe Updated")
            except mariadb.Error as err:
                print(f"Error : {err}")

        self.close()
    
    def addYeast(self):
        newYeast = NewYeastWindow(self)
        newYeast.yeastTableUpdated.connect(self.loadYeastItem)
        newYeast.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

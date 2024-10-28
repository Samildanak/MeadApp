# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime
import csv

# Import calculation library
import meadCalculation as mC

# Import Qt libraries
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QHeaderView, QTableView
from PySide6.QtCore import QDate, Signal, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem

# Import UI Windows
from MeadApp.ui_MainWindow import Ui_MainWindow
from MeadApp.ui_NewRecipe import Ui_NewRecipeWindow
from MeadApp.ui_AddYeast import Ui_Dialog
from MeadApp.ui_ShowRecipe import Ui_ShowRecipeWindow
from MeadApp.ui_SelectedRecipe import Ui_SelectedRecipe

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.newRecipeButton.clicked.connect(self.onNewRecipeClicked)
        self.ui.showRecipeButton.clicked.connect(self.onShowRecipeClicked)

    def onNewRecipeClicked(self):
        newRecipe = NewRecipeWindow(self)
        newRecipe.show()
    
    def onShowRecipeClicked(self):
        showRecipe = ShowRecipeWindow(self)
        showRecipe.show()

class NewRecipeWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.newRecipeUi = Ui_NewRecipeWindow()
        self.newRecipeUi.setupUi(self)
        self.csvpath = "./Data/meadData.csv"
        self.dataList = []
        self.updateYeast = False

        with open(self.csvpath, "r") as theFile:
            reader = csv.reader(theFile)
            self.headers = next(reader, None)
            for row in reader:
                if row:
                    row_dict = {h: v for h, v in zip(self.headers,row)}
                    self.dataList.append(row_dict)

        try:
            self.batchId = int(self.dataList[-1]["batch_id"]) + 1
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
        fermaidK = "Yes" if self.newRecipeUi.fermaid_box.isChecked() else "No"
        notes = self.newRecipeUi.note_box.toPlainText()
        date = self.newRecipeUi.date_box.date().toString("dd/MM/yyyy")
        yeast = self.newRecipeUi.comboBox.currentText()
        initialBrix = str(self.newRecipeUi.initial_brix.value())
        actualBrix = initialBrix

        # Construire un dictionnaire représentant une recette complète
        new_entry = {
            "batch_id": str(self.batchId),
            "name": name,
            "date": date,
            "volume": volume,
            "predicted_alcohol": alcoholicConcentration,
            "residual_sugar": residualSugar,
            "honey_quantity": honeyMass,
            "yeast" : yeast,
            "fermaid_k": fermaidK,
            "initial_brix": initialBrix,
            "actual_brix": actualBrix,
            "note": notes,
        }

        # Ajouter la nouvelle recette à la liste des recettes
        if not hasattr(self, "dataList"):
            self.dataList = []

        self.dataList.append(new_entry)

        # Écrire dans le fichier CSV
        try:
            with open(self.csvpath, "w", encoding="utf-8", newline='') as theFile:
                writer = csv.DictWriter(theFile, new_entry.keys())
                writer.writeheader()
                writer.writerows(self.dataList)
        except IOError as e:
            print(f"Writing Error : {e}")
        except Exception as e:
            print(f"Unexpected Error : {e}")

        self.close()

    def loadYeastItem(self):
        self.newRecipeUi.comboBox.clear()
        yeastPath = "./Data/yeast_type.csv"

        with open(yeastPath, 'r', encoding='utf-8') as theFile:
            reader = csv.reader(theFile)
            for row in reader:
                if row:
                    self.newRecipeUi.comboBox.addItem(row[0])
    
    def addYeast(self):
        newYeast = NewYeastWindow(self)
        newYeast.yeastTableUpdated.connect(self.loadYeastItem)
        newYeast.show()

class NewYeastWindow(QDialog):
    yeastTableUpdated = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.newYeastUi = Ui_Dialog()
        self.newYeastUi.setupUi(self)
        self.csvpath = "./Data/yeast_type.csv"
        self.dataList = []
        self.update = False

        with open(self.csvpath, 'r', encoding='utf-8') as theFile:
            reader = csv.reader(theFile)
            for row in reader:
                if row:
                    self.dataList.append(row[0])
        self.newYeastUi.buttonBox.accepted.connect(self.saveNewYeast)
        self.newYeastUi.buttonBox.rejected.connect(self.close)        
    
    def saveNewYeast(self):
        newYeast = self.newYeastUi.lineEdit.text()

        if newYeast and (newYeast not in self.dataList):
            self.dataList.append(newYeast)

        with open(self.csvpath, 'w', encoding='utf-8', newline='') as theFile:
            writer = csv.writer(theFile)
            for row in self.dataList:
                if row:
                    writer.writerow([row])

        self.closeEvent(None)
        self.close()
    
    def closeEvent(self, event):
        self.yeastTableUpdated.emit()
        if event:
            event.accept()

class ShowRecipeWindow(QMainWindow):
    def __init__(self, parent=None):
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

        self.dataList = []
        self.csvpath = "./Data/meadData.csv"

        with open(self.csvpath, "r") as theFile:
            reader = csv.reader(theFile)
            self.headers = next(reader, None)
            for row in reader:
                if row:
                    row_dict = {h: v for h, v in zip(self.headers,row)}
                    self.dataList.append(row_dict)
                    batchId = QStandardItem(str(row_dict["batch_id"]))
                    batchId.setTextAlignment(Qt.AlignCenter)
                    name = QStandardItem(str(row_dict["name"]))
                    name.setTextAlignment(Qt.AlignCenter)
                    modelRow = [batchId, 
                                name]
                    self.model.appendRow(modelRow)
        
        self.showRecipeUi.ConfirmBox.accepted.connect(self.showRecipe)

    def showRecipe(self):
        recipe_selected = self.showRecipeUi.tableView.selectedIndexes()
        if recipe_selected:
            index_id = recipe_selected[0]
            recipe_batch_id = self.model.item(index_id.row(), index_id.column()).text()
            recipeModificationWindow = RecipeModificationWindow(self, batch_id=recipe_batch_id)
            recipeModificationWindow.show()

class RecipeModificationWindow(QMainWindow):
    def __init__(self, parent=None, batch_id: str = ""):
        super().__init__(parent)
        self.recipeModificationUi = Ui_SelectedRecipe()
        self.recipeModificationUi.setupUi(self)

        self.batch_id = batch_id

        self.csvpath = "./Data/meadData.csv"
        self.updateYeast = False
        self.dataList = []

        with open(self.csvpath, "r") as theFile:
            reader = csv.reader(theFile)
            self.headers = next(reader, None)
            for row in reader:
                if row:
                    row_dict = {h: v for h, v in zip(self.headers,row)}
                    self.dataList.append(row_dict)
                    if row_dict["batch_id"] == self.batch_id:
                        self.recipeSelected = row_dict
        
        self.loadYeastItem()

        self.recipeModificationUi.name_box.setText(self.recipeSelected["name"])
        self.recipeModificationUi.date_box.setDate(QDate.fromString(self.recipeSelected["date"], "dd/MM/yyyy"))
        self.recipeModificationUi.volume_box.setValue(float(self.recipeSelected["volume"]))
        self.recipeModificationUi.honey_box.setValue(float(self.recipeSelected["honey_quantity"]))
        self.recipeModificationUi.fermaid_box.setChecked(True if self.recipeSelected["fermaid_k"] == "Yes" else False)
        self.recipeModificationUi.initial_brix.setValue(float(self.recipeSelected["initial_brix"]))
        self.recipeModificationUi.actual_brix.setValue(float(self.recipeSelected["actual_brix"]))
        self.recipeModificationUi.note_box.setPlainText(self.recipeSelected["note"])
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

    
    def loadYeastItem(self):
        self.recipeModificationUi.comboBox.clear()
        yeastPath = "./Data/yeast_type.csv"

        with open(yeastPath, 'r', encoding='utf-8') as theFile:
            reader = csv.reader(theFile)
            for row in reader:
                if row:
                    self.recipeModificationUi.comboBox.addItem(row[0])

    def savingRecipe(self):
        name = self.recipeModificationUi.name_box.text()
        volume = str(self.recipeModificationUi.volume_box.value())
        fermaidK = "Yes" if self.recipeModificationUi.fermaid_box.isChecked() else "No"
        notes = self.recipeModificationUi.note_box.toPlainText()
        date = self.recipeModificationUi.date_box.date().toString("dd/MM/yyyy")
        yeast = self.recipeModificationUi.comboBox.currentText()
        initialBrix = str(self.recipeModificationUi.initial_brix.value())
        actualBrix = str(self.recipeModificationUi.actual_brix.value())

        # Construire un dictionnaire représentant une recette complète
        update_entry = {
            "batch_id": str(self.batch_id),
            "name": name,
            "date": date,
            "volume": volume,
            "yeast" : yeast,
            "fermaid_k": fermaidK,
            "initial_brix": initialBrix,
            "actual_brix": actualBrix,
            "note": notes,
        }

        for index, entry in enumerate(self.dataList):
            if entry["batch_id"] == self.batch_id:
                self.dataList[index].update(update_entry)
                break

        # Écrire dans le fichier CSV
        try:
            with open(self.csvpath, "w", encoding="utf-8", newline='') as theFile:
                writer = csv.DictWriter(theFile, fieldnames=self.dataList[0].keys())
                writer.writeheader()
                writer.writerows(self.dataList)
        except IOError as e:
            print(f"Writing Error : {e}")
        except Exception as e:
            print(f"Unexpected Error : {e}")

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

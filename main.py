# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime

import csv


import meadCalculation as mC

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtCore import QDate

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from MeadApp.ui_MainWindow import Ui_MainWindow
from MeadApp.ui_NewRecipe import Ui_NewRecipeWindow

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
        print("Show Recipe")

class NewRecipeWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.newRecipeUi = Ui_NewRecipeWindow()
        self.newRecipeUi.setupUi(self)
        self.csvpath = "./Data/meadData.csv"

        with open(self.csvpath, "r") as theFile:
            reader = csv.reader(theFile)
            self.headers = next(reader, None)
            self.dataDict = {}
            for h in self.headers:
                self.dataDict[h] = []
            for row in reader:
                for h, v in zip(self.headers, row):
                    self.dataDict[h].append(v)

        try:
            self.batchId = int(self.dataDict["batch_id"][-1]) + 1
        except:
            self.batchId = 1
        today = datetime.now()

        self.newRecipeUi.batch_label.setText("Batch n°" + str(self.batchId))
        self.newRecipeUi.date_box.setDate(QDate.currentDate())
        self.newRecipeUi.honey_button.clicked.connect(self.calculateHoney)
        self.newRecipeUi.save_box.clicked.connect(self.savingRecipe)

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
        fermaidK = str(self.newRecipeUi.fermaid_box.isChecked())
        notes = self.newRecipeUi.note_box.toPlainText()
        date = self.newRecipeUi.date_box.date()

        self.dataDict["batch_id"].append(str(self.batchId))
        self.dataDict["name"].append(name)
        self.dataDict["date"].append(date)
        self.dataDict["volume"].append(volume)
        self.dataDict["predicted_alcohol"].append(alcoholicConcentration)
        self.dataDict["residual_sugar"].append(residualSugar)
        self.dataDict["honey_quantity"].append(honeyMass)
        self.dataDict["fermaid_k"].append(fermaidK)
        self.dataDict["note"].append(notes)

        print(self.dataDict)

        with open(self.csvpath, "w") as theFile:
            writer = csv.DictWriter(theFile, self.dataDict.keys())
            writer.writeheader()
            writer.writerow(self.dataDict)
        
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

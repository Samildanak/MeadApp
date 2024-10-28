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
        self.dataList = []

        with open(self.csvpath, "r") as theFile:
            reader = csv.reader(theFile)
            self.headers = next(reader, None)
            for row in reader:
                if row:
                    row_dict = {h: v for h, v in zip(self.headers,row)}
                    self.dataList.append(row_dict)

        print("Data uploaded : ", self.dataList)

        try:
            self.batchId = int(self.dataList[-1]["batch_id"]) + 1
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
        fermaidK = "Yes" if self.newRecipeUi.fermaid_box.isChecked() else "No"
        notes = self.newRecipeUi.note_box.toPlainText()
        date = self.newRecipeUi.date_box.date().toString("dd/MM/yyyy")

        print(f"name : {name}")
        print(f"volume : {volume}")
        print(f"alcoholicConcentration : {alcoholicConcentration}")
        print(f"residualSugar : {residualSugar}")
        print(f"honeyMass : {honeyMass}")
        print(f"fermaidK : {fermaidK}")
        print(f"date : {date}")

        # Construire un dictionnaire représentant une recette complète
        new_entry = {
            "batch_id": str(self.batchId),
            "name": name,
            "date": date,
            "volume": volume,
            "predicted_alcohol": alcoholicConcentration,
            "residual_sugar": residualSugar,
            "honey_quantity": honeyMass,
            "fermaid_k": fermaidK,
            "note": notes,
        }

        # Ajouter la nouvelle recette à la liste des recettes
        if not hasattr(self, "dataList"):
            self.dataList = []

        self.dataList.append(new_entry)

        # Vérifier la liste avant l'écriture
        print("Liste des recettes :", self.dataList)

        # Écrire dans le fichier CSV
        try:
            print(f"Chemin du fichier : {self.csvpath}")
            with open(self.csvpath, "w", encoding="utf-8", newline='') as theFile:
                writer = csv.DictWriter(theFile, new_entry.keys())
                writer.writeheader()
                writer.writerows(self.dataList)
            print("Données enregistrées avec succès.")
        except IOError as e:
            print(f"Erreur d'écriture : {e}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

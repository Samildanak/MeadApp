# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectedRecipe.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDoubleSpinBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_SelectedRecipe(object):
    def setupUi(self, SelectedRecipe):
        if not SelectedRecipe.objectName():
            SelectedRecipe.setObjectName(u"SelectedRecipe")
        SelectedRecipe.resize(571, 600)
        icon = QIcon()
        icon.addFile(u"../Resources/meadappico_Uh1_icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SelectedRecipe.setWindowIcon(icon)
        self.centralwidget = QWidget(SelectedRecipe)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 210, 101, 16))
        self.date_box = QDateEdit(self.centralwidget)
        self.date_box.setObjectName(u"date_box")
        self.date_box.setGeometry(QRect(120, 70, 110, 22))
        self.date_box.setCalendarPopup(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 130, 49, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 130, 49, 16))
        self.name_box = QLineEdit(self.centralwidget)
        self.name_box.setObjectName(u"name_box")
        self.name_box.setGeometry(QRect(120, 40, 411, 22))
        self.add_yeast_button = QPushButton(self.centralwidget)
        self.add_yeast_button.setObjectName(u"add_yeast_button")
        self.add_yeast_button.setGeometry(QRect(80, 250, 131, 24))
        self.volume_box = QDoubleSpinBox(self.centralwidget)
        self.volume_box.setObjectName(u"volume_box")
        self.volume_box.setGeometry(QRect(120, 130, 81, 22))
        self.volume_box.setMaximum(10000000.000000000000000)
        self.fermaid_box = QCheckBox(self.centralwidget)
        self.fermaid_box.setObjectName(u"fermaid_box")
        self.fermaid_box.setGeometry(QRect(120, 290, 21, 20))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(270, 140, 250, 151))
        self.tableWidget.setMinimumSize(QSize(250, 0))
        self.tableWidget.setMaximumSize(QSize(205, 16777215))
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 210, 131, 22))
        self.batch_label = QLabel(self.centralwidget)
        self.batch_label.setObjectName(u"batch_label")
        self.batch_label.setGeometry(QRect(20, 10, 71, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 70, 49, 16))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(210, 170, 49, 16))
        self.save_box = QPushButton(self.centralwidget)
        self.save_box.setObjectName(u"save_box")
        self.save_box.setGeometry(QRect(380, 530, 171, 41))
        self.note_box = QTextEdit(self.centralwidget)
        self.note_box.setObjectName(u"note_box")
        self.note_box.setGeometry(QRect(270, 330, 251, 191))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 290, 101, 16))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 170, 101, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 40, 49, 16))
        self.honey_box = QDoubleSpinBox(self.centralwidget)
        self.honey_box.setObjectName(u"honey_box")
        self.honey_box.setGeometry(QRect(120, 170, 81, 22))
        self.honey_box.setMaximum(1000000.000000000000000)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 320, 101, 16))
        self.initial_brix = QDoubleSpinBox(self.centralwidget)
        self.initial_brix.setObjectName(u"initial_brix")
        self.initial_brix.setGeometry(QRect(120, 320, 81, 22))
        self.actual_brix = QDoubleSpinBox(self.centralwidget)
        self.actual_brix.setObjectName(u"actual_brix")
        self.actual_brix.setGeometry(QRect(120, 360, 81, 22))
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 360, 101, 16))
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 400, 151, 16))
        self.calculated_alcohol_concentration = QLabel(self.centralwidget)
        self.calculated_alcohol_concentration.setObjectName(u"calculated_alcohol_concentration")
        self.calculated_alcohol_concentration.setGeometry(QRect(80, 420, 71, 31))
        font = QFont()
        font.setPointSize(11)
        self.calculated_alcohol_concentration.setFont(font)
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(140, 420, 49, 16))
        SelectedRecipe.setCentralWidget(self.centralwidget)

        self.retranslateUi(SelectedRecipe)

        QMetaObject.connectSlotsByName(SelectedRecipe)
    # setupUi

    def retranslateUi(self, SelectedRecipe):
        SelectedRecipe.setWindowTitle(QCoreApplication.translate("SelectedRecipe", u"Modify Recipe", None))
        self.label_12.setText(QCoreApplication.translate("SelectedRecipe", u"Yeast", None))
        self.label_5.setText(QCoreApplication.translate("SelectedRecipe", u"Liters", None))
        self.label_4.setText(QCoreApplication.translate("SelectedRecipe", u"Volume", None))
        self.add_yeast_button.setText(QCoreApplication.translate("SelectedRecipe", u"Add New Yeast", None))
        self.fermaid_box.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SelectedRecipe", u"Residual Sugar (gr/L)", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SelectedRecipe", u"Dry", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SelectedRecipe", u"Off-Dry", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SelectedRecipe", u"Sweet", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SelectedRecipe", u"Dessert", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SelectedRecipe", u"0 - 10", None));
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SelectedRecipe", u"10 - 20", None));
        ___qtablewidgetitem7 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SelectedRecipe", u"20 - 40", None));
        ___qtablewidgetitem8 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SelectedRecipe", u"40 - 60", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.batch_label.setText(QCoreApplication.translate("SelectedRecipe", u"Batch n\u00b01", None))
        self.label_3.setText(QCoreApplication.translate("SelectedRecipe", u"Date :", None))
        self.label_11.setText(QCoreApplication.translate("SelectedRecipe", u"gr", None))
        self.save_box.setText(QCoreApplication.translate("SelectedRecipe", u"Modify the recipe", None))
        self.label_13.setText(QCoreApplication.translate("SelectedRecipe", u"Fermaid K", None))
        self.label_10.setText(QCoreApplication.translate("SelectedRecipe", u"Honey Quantity", None))
        self.label_2.setText(QCoreApplication.translate("SelectedRecipe", u"Name :", None))
        self.label_14.setText(QCoreApplication.translate("SelectedRecipe", u"Initial Brix", None))
        self.label_15.setText(QCoreApplication.translate("SelectedRecipe", u"Actual Brix", None))
        self.label_16.setText(QCoreApplication.translate("SelectedRecipe", u"Alcohol Concentration", None))
        self.calculated_alcohol_concentration.setText("")
        self.label_17.setText(QCoreApplication.translate("SelectedRecipe", u"\u00b0", None))
    # retranslateUi


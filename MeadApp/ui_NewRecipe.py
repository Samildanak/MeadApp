# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewRecipe.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDoubleSpinBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_NewRecipeWindow(object):
    def setupUi(self, NewRecipeWindow):
        if not NewRecipeWindow.objectName():
            NewRecipeWindow.setObjectName(u"NewRecipeWindow")
        NewRecipeWindow.resize(563, 600)
        self.centralwidget = QWidget(NewRecipeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.batch_label = QLabel(self.centralwidget)
        self.batch_label.setObjectName(u"batch_label")
        self.batch_label.setGeometry(QRect(20, 10, 71, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 40, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 70, 49, 16))
        self.date_box = QDateEdit(self.centralwidget)
        self.date_box.setObjectName(u"date_box")
        self.date_box.setGeometry(QRect(120, 70, 110, 22))
        self.date_box.setCalendarPopup(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 130, 49, 16))
        self.volume_box = QDoubleSpinBox(self.centralwidget)
        self.volume_box.setObjectName(u"volume_box")
        self.volume_box.setGeometry(QRect(120, 130, 81, 22))
        self.volume_box.setMaximum(10000000.000000000000000)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 130, 49, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 170, 49, 16))
        self.alcohol_box = QDoubleSpinBox(self.centralwidget)
        self.alcohol_box.setObjectName(u"alcohol_box")
        self.alcohol_box.setGeometry(QRect(120, 170, 81, 22))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 170, 101, 16))
        self.sugar_box = QDoubleSpinBox(self.centralwidget)
        self.sugar_box.setObjectName(u"sugar_box")
        self.sugar_box.setGeometry(QRect(120, 210, 81, 22))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 210, 49, 16))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 210, 101, 16))
        self.name_box = QLineEdit(self.centralwidget)
        self.name_box.setObjectName(u"name_box")
        self.name_box.setGeometry(QRect(120, 40, 411, 22))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 290, 101, 16))
        self.honey_box = QDoubleSpinBox(self.centralwidget)
        self.honey_box.setObjectName(u"honey_box")
        self.honey_box.setGeometry(QRect(120, 290, 81, 22))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(210, 290, 49, 16))
        self.honey_button = QPushButton(self.centralwidget)
        self.honey_button.setObjectName(u"honey_button")
        self.honey_button.setGeometry(QRect(80, 250, 131, 24))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 330, 101, 16))
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
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 370, 101, 16))
        self.fermaid_box = QCheckBox(self.centralwidget)
        self.fermaid_box.setObjectName(u"fermaid_box")
        self.fermaid_box.setGeometry(QRect(120, 370, 21, 20))
        self.save_box = QPushButton(self.centralwidget)
        self.save_box.setObjectName(u"save_box")
        self.save_box.setGeometry(QRect(380, 530, 171, 41))
        self.note_box = QTextEdit(self.centralwidget)
        self.note_box.setObjectName(u"note_box")
        self.note_box.setGeometry(QRect(270, 330, 251, 191))
        NewRecipeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(NewRecipeWindow)
        self.statusbar.setObjectName(u"statusbar")
        NewRecipeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewRecipeWindow)

        QMetaObject.connectSlotsByName(NewRecipeWindow)
    # setupUi

    def retranslateUi(self, NewRecipeWindow):
        NewRecipeWindow.setWindowTitle(QCoreApplication.translate("NewRecipeWindow", u"MainWindow", None))
        self.batch_label.setText(QCoreApplication.translate("NewRecipeWindow", u"Batch n\u00b01", None))
        self.label_2.setText(QCoreApplication.translate("NewRecipeWindow", u"Name :", None))
        self.label_3.setText(QCoreApplication.translate("NewRecipeWindow", u"Date :", None))
        self.label_4.setText(QCoreApplication.translate("NewRecipeWindow", u"Volume", None))
        self.label_5.setText(QCoreApplication.translate("NewRecipeWindow", u"Liters", None))
        self.label_6.setText(QCoreApplication.translate("NewRecipeWindow", u"\u00b0", None))
        self.label_7.setText(QCoreApplication.translate("NewRecipeWindow", u"Predicted Alcohol", None))
        self.label_8.setText(QCoreApplication.translate("NewRecipeWindow", u"gr/L", None))
        self.label_9.setText(QCoreApplication.translate("NewRecipeWindow", u"Residual Sugar", None))
        self.label_10.setText(QCoreApplication.translate("NewRecipeWindow", u"Honey Quantity", None))
        self.label_11.setText(QCoreApplication.translate("NewRecipeWindow", u"gr", None))
        self.honey_button.setText(QCoreApplication.translate("NewRecipeWindow", u"Calculate Honey", None))
        self.label_12.setText(QCoreApplication.translate("NewRecipeWindow", u"Yeast", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("NewRecipeWindow", u"Residual Sugar (gr/L)", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("NewRecipeWindow", u"Dry", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("NewRecipeWindow", u"Off-Dry", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("NewRecipeWindow", u"Sweet", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("NewRecipeWindow", u"Dessert", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("NewRecipeWindow", u"0 - 10", None));
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("NewRecipeWindow", u"10 - 20", None));
        ___qtablewidgetitem7 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("NewRecipeWindow", u"20 - 40", None));
        ___qtablewidgetitem8 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("NewRecipeWindow", u"40 - 60", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_13.setText(QCoreApplication.translate("NewRecipeWindow", u"Fermaid K", None))
        self.fermaid_box.setText("")
        self.save_box.setText(QCoreApplication.translate("NewRecipeWindow", u"Save Recipe", None))
    # retranslateUi


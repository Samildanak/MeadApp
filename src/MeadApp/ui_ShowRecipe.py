# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowRecipe.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractScrollArea, QApplication, QDialogButtonBox,
    QHeaderView, QMainWindow, QSizePolicy, QTableView,
    QWidget)

class Ui_ShowRecipeWindow(object):
    def setupUi(self, ShowRecipeWindow):
        if not ShowRecipeWindow.objectName():
            ShowRecipeWindow.setObjectName(u"ShowRecipeWindow")
        ShowRecipeWindow.resize(585, 600)
        icon = QIcon()
        icon.addFile(u"../Resources/meadappico_Uh1_icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ShowRecipeWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(ShowRecipeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ConfirmBox = QDialogButtonBox(self.centralwidget)
        self.ConfirmBox.setObjectName(u"ConfirmBox")
        self.ConfirmBox.setGeometry(QRect(450, 50, 111, 61))
        self.ConfirmBox.setOrientation(Qt.Orientation.Vertical)
        self.ConfirmBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Open)
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 20, 411, 551))
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableView.verticalHeader().setVisible(False)
        ShowRecipeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ShowRecipeWindow)

        QMetaObject.connectSlotsByName(ShowRecipeWindow)
    # setupUi

    def retranslateUi(self, ShowRecipeWindow):
        ShowRecipeWindow.setWindowTitle(QCoreApplication.translate("ShowRecipeWindow", u"Recipe List", None))
    # retranslateUi


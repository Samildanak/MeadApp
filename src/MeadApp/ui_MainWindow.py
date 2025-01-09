# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(357, 214)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionChange_Database_Configuration = QAction(MainWindow)
        self.actionChange_Database_Configuration.setObjectName(u"actionChange_Database_Configuration")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.newRecipeButton = QPushButton(self.centralwidget)
        self.newRecipeButton.setObjectName(u"newRecipeButton")
        self.newRecipeButton.setGeometry(QRect(110, 20, 111, 31))
        self.showRecipeButton = QPushButton(self.centralwidget)
        self.showRecipeButton.setObjectName(u"showRecipeButton")
        self.showRecipeButton.setGeometry(QRect(110, 80, 111, 31))
        self.connectionStatus = QLineEdit(self.centralwidget)
        self.connectionStatus.setObjectName(u"connectionStatus")
        self.connectionStatus.setEnabled(False)
        self.connectionStatus.setGeometry(QRect(220, 130, 113, 22))
        self.connectionStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 357, 22))
        self.menuDatabase = QMenu(self.menubar)
        self.menuDatabase.setObjectName(u"menuDatabase")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menuDatabase.addAction(self.actionConnect)
        self.menuDatabase.addAction(self.actionChange_Database_Configuration)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect...", None))
        self.actionChange_Database_Configuration.setText(QCoreApplication.translate("MainWindow", u"Change Database Configuration", None))
        self.newRecipeButton.setText(QCoreApplication.translate("MainWindow", u"New Recipe", None))
        self.showRecipeButton.setText(QCoreApplication.translate("MainWindow", u"Show Recipe", None))
        self.menuDatabase.setTitle(QCoreApplication.translate("MainWindow", u"Database", None))
    # retranslateUi


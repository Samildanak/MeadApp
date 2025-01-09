# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GetDatabasePath.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_GetDatabasePath(object):
    def setupUi(self, GetDatabasePath):
        if not GetDatabasePath.objectName():
            GetDatabasePath.setObjectName(u"GetDatabasePath")
        GetDatabasePath.resize(504, 263)
        self.stackedWidget = QStackedWidget(GetDatabasePath)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 20, 471, 191))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayoutWidget = QWidget(self.page)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 40, 461, 141))
        self.ServerInfo = QGridLayout(self.gridLayoutWidget)
        self.ServerInfo.setObjectName(u"ServerInfo")
        self.ServerInfo.setContentsMargins(0, 0, 9, 0)
        self.password = QLineEdit(self.gridLayoutWidget)
        self.password.setObjectName(u"password")
        self.password.setEnabled(True)

        self.ServerInfo.addWidget(self.password, 1, 1, 1, 1)

        self.username = QLineEdit(self.gridLayoutWidget)
        self.username.setObjectName(u"username")
        self.username.setEnabled(True)

        self.ServerInfo.addWidget(self.username, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.ServerInfo.addWidget(self.label, 0, 0, 1, 1)

        self.host = QLineEdit(self.gridLayoutWidget)
        self.host.setObjectName(u"host")
        self.host.setEnabled(True)

        self.ServerInfo.addWidget(self.host, 2, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.ServerInfo.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.ServerInfo.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.ServerInfo.addWidget(self.label_4, 3, 0, 1, 1)

        self.port = QLineEdit(self.gridLayoutWidget)
        self.port.setObjectName(u"port")
        self.port.setEnabled(True)

        self.ServerInfo.addWidget(self.port, 3, 1, 1, 1)

        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.password.raise_()
        self.host.raise_()
        self.port.raise_()
        self.username.raise_()
        self.label_info = QLabel(self.page)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(0, 0, 451, 41))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 381, 16))
        self.database_available = QComboBox(self.page_2)
        self.database_available.setObjectName(u"database_available")
        self.database_available.setGeometry(QRect(40, 70, 311, 22))
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 40, 131, 16))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 441, 151))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_7.setWordWrap(True)
        self.table_available = QListWidget(self.page_3)
        self.table_available.setObjectName(u"table_available")
        self.table_available.setGeometry(QRect(10, 60, 431, 121))
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayoutWidget = QWidget(GetDatabasePath)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(220, 200, 251, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.next = QPushButton(self.horizontalLayoutWidget)
        self.next.setObjectName(u"next")

        self.horizontalLayout.addWidget(self.next)

        self.cancel = QPushButton(self.horizontalLayoutWidget)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)


        self.retranslateUi(GetDatabasePath)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(GetDatabasePath)
    # setupUi

    def retranslateUi(self, GetDatabasePath):
        GetDatabasePath.setWindowTitle(QCoreApplication.translate("GetDatabasePath", u"Database Configuration", None))
        self.label.setText(QCoreApplication.translate("GetDatabasePath", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("GetDatabasePath", u"IP Address", None))
        self.label_2.setText(QCoreApplication.translate("GetDatabasePath", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("GetDatabasePath", u"Port", None))
        self.port.setText(QCoreApplication.translate("GetDatabasePath", u"3306", None))
        self.label_info.setText(QCoreApplication.translate("GetDatabasePath", u"Enter the configuration information of your SQL Server :", None))
        self.label_5.setText(QCoreApplication.translate("GetDatabasePath", u"Connection to server successful, please select a Database :", None))
        self.label_6.setText(QCoreApplication.translate("GetDatabasePath", u"Available Database :", None))
        self.label_7.setText(QCoreApplication.translate("GetDatabasePath", u"<html><head/><body><p>The connection to database is successful. If database doesn't contains table RECIPE and table YEAST_TYPE, these two tables will be created. Here the actual table on your database :</p><p><br/></p></body></html>", None))
        self.next.setText(QCoreApplication.translate("GetDatabasePath", u"Next", None))
        self.cancel.setText(QCoreApplication.translate("GetDatabasePath", u"Cancel", None))
    # retranslateUi


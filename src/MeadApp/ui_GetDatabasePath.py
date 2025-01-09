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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_GetDatabasePath(object):
    def setupUi(self, GetDatabasePath):
        if not GetDatabasePath.objectName():
            GetDatabasePath.setObjectName(u"GetDatabasePath")
        GetDatabasePath.resize(504, 324)
        self.buttonBox = QDialogButtonBox(GetDatabasePath)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(140, 280, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.jsonConfigExist = QRadioButton(GetDatabasePath)
        self.jsonConfigExist.setObjectName(u"jsonConfigExist")
        self.jsonConfigExist.setGeometry(QRect(20, 20, 591, 20))
        self.jsonConfigExist.setChecked(True)
        self.jsonConfigNotExist = QRadioButton(GetDatabasePath)
        self.jsonConfigNotExist.setObjectName(u"jsonConfigNotExist")
        self.jsonConfigNotExist.setGeometry(QRect(20, 90, 591, 20))
        self.pathLine = QLineEdit(GetDatabasePath)
        self.pathLine.setObjectName(u"pathLine")
        self.pathLine.setGeometry(QRect(20, 50, 361, 22))
        self.browse = QPushButton(GetDatabasePath)
        self.browse.setObjectName(u"browse")
        self.browse.setGeometry(QRect(400, 50, 75, 24))
        self.gridLayoutWidget = QWidget(GetDatabasePath)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 120, 461, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 9, 0)
        self.username = QLineEdit(self.gridLayoutWidget)
        self.username.setObjectName(u"username")
        self.username.setEnabled(False)

        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.password = QLineEdit(self.gridLayoutWidget)
        self.password.setObjectName(u"password")
        self.password.setEnabled(False)

        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)

        self.host = QLineEdit(self.gridLayoutWidget)
        self.host.setObjectName(u"host")
        self.host.setEnabled(False)

        self.gridLayout.addWidget(self.host, 2, 1, 1, 1)

        self.port = QLineEdit(self.gridLayoutWidget)
        self.port.setObjectName(u"port")
        self.port.setEnabled(False)

        self.gridLayout.addWidget(self.port, 3, 1, 1, 1)


        self.retranslateUi(GetDatabasePath)
        self.buttonBox.accepted.connect(GetDatabasePath.accept)
        self.buttonBox.rejected.connect(GetDatabasePath.reject)

        QMetaObject.connectSlotsByName(GetDatabasePath)
    # setupUi

    def retranslateUi(self, GetDatabasePath):
        GetDatabasePath.setWindowTitle(QCoreApplication.translate("GetDatabasePath", u"Dialog", None))
        self.jsonConfigExist.setText(QCoreApplication.translate("GetDatabasePath", u"I already have a Database config JSON File", None))
        self.jsonConfigNotExist.setText(QCoreApplication.translate("GetDatabasePath", u"I don't have a Database config JSON File", None))
        self.browse.setText(QCoreApplication.translate("GetDatabasePath", u"Browse...", None))
        self.label_2.setText(QCoreApplication.translate("GetDatabasePath", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("GetDatabasePath", u"IP Address", None))
        self.label_4.setText(QCoreApplication.translate("GetDatabasePath", u"Port", None))
        self.label.setText(QCoreApplication.translate("GetDatabasePath", u"Username", None))
    # retranslateUi


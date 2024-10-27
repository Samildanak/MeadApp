# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(438, 238)
        self.actionNew_Recipe = QAction(MainWindow)
        self.actionNew_Recipe.setObjectName(u"actionNew_Recipe")
        self.actionNew_Recipe.setMenuRole(QAction.MenuRole.NoRole)
        self.newRecipeButton = QPushButton(MainWindow)
        self.newRecipeButton.setObjectName(u"newRecipeButton")
        self.newRecipeButton.setGeometry(QRect(160, 60, 121, 41))
        self.showRecipeButton = QPushButton(MainWindow)
        self.showRecipeButton.setObjectName(u"showRecipeButton")
        self.showRecipeButton.setGeometry(QRect(160, 140, 121, 41))
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 210, 101, 20))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Widget", None))
        self.actionNew_Recipe.setText(QCoreApplication.translate("MainWindow", u"New Recipe", None))
#if QT_CONFIG(tooltip)
        self.actionNew_Recipe.setToolTip(QCoreApplication.translate("MainWindow", u"Open New Recipe Window", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNew_Recipe.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.newRecipeButton.setText(QCoreApplication.translate("MainWindow", u"New Recipe", None))
        self.showRecipeButton.setText(QCoreApplication.translate("MainWindow", u"Show Recipes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mead App V0.01", None))
    # retranslateUi


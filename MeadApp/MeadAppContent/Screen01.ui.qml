/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick
import QtQuick.Controls
import MeadApp

Rectangle {
    id: rectangle1
    width: 400
    height: 600

    color: Constants.backgroundColor

    Button {
        id: button
        x: 150
        y: 210
        text: qsTr("New Recipe")

        Connections {
            target: button
            onClicked: Qt.quit()
        }
    }

    Button {
        id: button1
        x: 150
        y: 329
        text: qsTr("Show Recipes")
    }
}

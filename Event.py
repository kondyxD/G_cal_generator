import sys

from PyQt5.QtCore import QUrl, pyqtProperty, pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQml import qmlRegisterType, QQmlComponent
from PyQt5.QtQuick import QQuickItem


class Widget(QQuickItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._name = "Value"
        print("New Widget handler created")

    nameChanged = pyqtSignal()

    @pyqtProperty('QString', notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        self.nameChanged.emit()

    @pyqtSlot(str, name="change")
    def change(self, value):
        print("Catched!!!!", value)
        self.name = "Ch-ch-ch-changes! " + value

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from API.GoogleCalAPI import GoogleCalAPI
from datetime import datetime


class Calendar(QObject):
    """docstring for Calendar."""

    def __init__(self):
        QObject.__init__(self)
        self.googleAPI = GoogleCalAPI()

    def formatDate(self, date):
        date = datetime.strptime(date, '%c %Z%z')
        date = date.strftime("%A %d")
        return date

    printedDate = pyqtSignal(str, arguments=['printDate'])
    loadedDate = pyqtSignal(str, arguments=['loadedDate'])
    loadedCredentials = pyqtSignal(str, arguments=['loadedCredentials'])

    @pyqtSlot(str)
    def printDate(self, date):
        date = self.formatDate(date)
        self.printedDate.emit(date)

    @pyqtSlot(str)
    def loadDate(self, text):
        today = datetime.today()
        today = today.strftime("%A %d")
        print(self.googleAPI.get_my_events(today))
        self.loadedDate.emit(today)

    @pyqtSlot(str)
    def loadCredentials(self, text):
        cal = self.googleAPI.get_my_calendars()
        email = cal["id"]
        today = datetime.today()
        today = today.strftime("%A %d")
        self.loadedCredentials.emit(email)

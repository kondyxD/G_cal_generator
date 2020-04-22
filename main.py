import sys
from Calendar import Calendar
from API.GoogleCalAPI import GoogleCalAPI
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine

app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon('resources/imgs/g_call.png'))

engine = QQmlApplicationEngine()
calendar = Calendar()
engine.rootContext().setContextProperty('calendarConn', calendar)
engine.load('main.qml')

engine.quit.connect(app.quit)
sys.exit(app.exec_())

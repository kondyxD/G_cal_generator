import sys

from Components.Calendar import Calendar
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine

app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon('resources/imgs/g_call.png'))

engine = QQmlApplicationEngine()
calendar = Calendar()
engine.rootContext().setContextProperty('calendarConn', calendar)
engine.load('QML/main.qml')

engine.quit.connect(app.quit)
sys.exit(app.exec_())
 

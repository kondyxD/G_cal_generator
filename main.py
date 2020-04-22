import sys
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine

app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon('resources/imgs/g_call.png'))

engine = QQmlApplicationEngine()
engine.load('resources/qml/main.qml')
engine.quit.connect(app.quit)

sys.exit(app.exec_())

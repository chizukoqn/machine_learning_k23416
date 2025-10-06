from PyQt6.QtWidgets import QApplication, QMainWindow

from MainwindowEx import MainwindowEx

app=QApplication([])
myWindow=MainwindowEx()
myWindow.setupUi(QMainWindow())
myWindow.connectMySQL()
myWindow.selectAllStudent()
myWindow.show()
app.exec()
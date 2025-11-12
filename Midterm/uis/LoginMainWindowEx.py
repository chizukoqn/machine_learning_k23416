from PyQt6.QtWidgets import QMessageBox, QMainWindow

from Midterm.connectors.employee_connector import EmployeeConnector
from Midterm.uis.EmployeeMainWindowEx import EmployeeMainWindowEx
from Midterm.uis.LoginMainWindow import Ui_MainWindow
from Midterm.uis.StatisticMainWindowEx import StatisticMainWindowEx


class LoginMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.count = 0
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)

    def process_login(self):
        email = self.lineEditEmail.text()
        pwd = self.lineEditPassword.text()
        ec = EmployeeConnector()
        ec.connect()
        em = ec.login(email, pwd)
        if em == None:
            self.count += 1
            if self.count < 4:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("Login Failed, please check your account again")
                msg.setWindowTitle("Login Failed")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("Login quá 3 lần, khóa login")
                msg.setWindowTitle("Login Failed")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec()
                self.MainWindow.close()
        else:
            self.count = 0
            if em.Role == "admin":
                self.qui_emp = EmployeeMainWindowEx()
                self.qui_emp.setupUi(QMainWindow())
                self.qui_emp.showWindow()
            elif em.Role == "reporter":
                self.qui_emp = StatisticMainWindowEx()
                self.qui_emp.setupUi(QMainWindow())
                self.qui_emp.showWindow()
            elif em.Role == "technical":
                self.qui_emp = TrainEx()
                self.qui_emp.setupUi(QMainWindow())
                self.qui_emp.showWindow()
            self.MainWindow.close()

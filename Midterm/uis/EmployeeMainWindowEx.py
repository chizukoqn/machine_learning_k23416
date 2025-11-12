from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow

from Midterm.connectors.employee_connector import EmployeeConnector
from Midterm.model.employee import Employee
from Midterm.uis.EmployeeMainWindow import Ui_MainWindow
from Midterm.uis.StatisticMainWindowEx import StatisticMainWindowEx


class EmployeeMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.ec = EmployeeConnector()
        self.ec.connect()
        self.is_completed = False
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.displayListEmployee()
        self.is_completed = True
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()
    def displayListEmployee(self):
        self.employee = self.ec.get_all_employee()
        #remove existing data
        self.tableWidgetEmployee.setRowCount(0)
        for emp in self.employee:
            # get the last row
            row = self.tableWidgetEmployee.rowCount()
            # insert a new row
            self.tableWidgetEmployee.insertRow(row)

            item_ID = QTableWidgetItem(str(emp.ID))
            self.tableWidgetEmployee.setItem(row,0, item_ID)

            item_name = QTableWidgetItem(str(emp.Name))
            self.tableWidgetEmployee.setItem(row, 1, item_name)

            item_email = QTableWidgetItem(str(emp.Email))
            self.tableWidgetEmployee.setItem(row, 2, item_email)

            item_role = QTableWidgetItem(str(emp.Role))
            self.tableWidgetEmployee.setItem(row, 3, item_role)

    def setupSignalAndSlot(self):
        self.pushButtonNew.clicked.connect(self.clearAll)
        self.tableWidgetEmployee.itemSelectionChanged.connect(self.show_detail)
        self.pushButtonSave.clicked.connect(self.SaveEmp)
        self.pushButtonUpdate.clicked.connect(self.Update_emp)
        self.pushButtonDeleted.clicked.connect(self.Deleted_emp)
        self.pushButtonStatic.clicked.connect(self.OpenStatic)
    def clearAll(self):
        self.lineEditEmpID.setText("")
        self.lineEditName.setText("")
        self.lineEditEmail.setText("")
        self.lineEditPassword.setText("")
        self.lineEditRole.setText("")
        self.lineEditName.setFocus()


    def show_detail(self):
        if self.is_completed == False:
            return

        row_index = self.tableWidgetEmployee.currentIndex()
        print("click", row_index.row())

        id = self.tableWidgetEmployee.item(row_index.row(), 0).text()
        print("emp id =",id)

        emp = self.ec.getDetailInfo(id)

        if emp != None:
            self.lineEditEmpID.setText(str(emp.ID))
            self.lineEditName.setText(emp.Name)
            self.lineEditEmail.setText(str(emp.Email))
            self.lineEditRole.setText(str(emp.Role))
            self.lineEditPassword.setText("")

    def SaveEmp(self):
        self.is_completed = False
        emp = Employee()
        emp.Name = self.lineEditName.text()
        emp.Role = self.lineEditRole.text()
        emp.Email = self.lineEditEmail.text()
        emp.Password = self.lineEditPassword.text()
        result = self.ec.insertOneEmployee(emp)
        if result > 0:
            self.displayListEmployee()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Lưu hong được bạn ơi ~~~")
            msg.setWindowTitle("Lưu lỗi tè le")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
        self.is_completed = True

    def Update_emp(self):
        self.is_completed = False
        emp = Employee()
        emp.ID = self.lineEditEmpID.text()
        emp.Name = self.lineEditName.text()
        emp.Role = self.lineEditRole.text()
        emp.Email = self.lineEditEmail.text()
        emp.Password = self.lineEditPassword.text()

        result = self.ec.updateOneEmployee(emp)
        if result > 0:
            self.displayListEmployee()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Không cập nhật được ~~~")
            msg.setWindowTitle("Lưu lỗi tè le")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
        self.is_completed = True

    def Deleted_emp(self):
        self.is_completed = False
        emp = Employee()
        emp.ID = self.lineEditEmpID.text()
        result = self.ec.deletedOneEmployee(emp)
        if result > 0:
            self.displayListEmployee()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Không xóa được ~~~")
            msg.setWindowTitle("Lưu lỗi tè le")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
        self.is_completed = True

    def OpenStatic(self):
        self.qui_emp = StatisticMainWindowEx()
        self.qui_emp.setupUi(QMainWindow())
        self.qui_emp.showWindow()
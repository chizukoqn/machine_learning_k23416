from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.model.employee import Employee
from retail_project.uis.EmployeeMainWindow import Ui_MainWindow


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
            if emp.IsDeleted == 1:
                item_ID.setBackground(Qt.GlobalColor.red)
            item_code = QTableWidgetItem(str(emp.EmployeeCode))
            self.tableWidgetEmployee.setItem(row, 1, item_code)

            item_name = QTableWidgetItem(str(emp.Name))
            self.tableWidgetEmployee.setItem(row, 2, item_name)

            item_phone = QTableWidgetItem(str(emp.Phone))
            self.tableWidgetEmployee.setItem(row, 3, item_phone)

            item_email = QTableWidgetItem(str(emp.Email))
            self.tableWidgetEmployee.setItem(row, 4, item_email)

    def setupSignalAndSlot(self):
        self.pushButtonNew.clicked.connect(self.clearAll)
        self.tableWidgetEmployee.itemSelectionChanged.connect(self.show_detail)
        self.pushButtonSave.clicked.connect(self.SaveEmp)
        self.pushButtonUpdate.clicked.connect(self.Update_emp)
        self.pushButtonDeleted.clicked.connect(self.Deleted_emp)
    def clearAll(self):
        self.lineEditEmpID.setText("")
        self.lineEditName.setText("")
        self.lineEditCode.setText("")
        self.lineEditEmail.setText("")
        self.lineEditPhone.setText("")
        self.lineEditPassword.setText("")
        self.lineEditCode.setFocus()

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
            self.lineEditCode.setText(str(emp.EmployeeCode))
            self.lineEditName.setText(emp.Name)
            self.lineEditPhone.setText(str(emp.Phone))
            self.lineEditEmail.setText(str(emp.Email))
            self.lineEditPassword.setText("")

            if emp.IsDeleted == 1:
                self.checkBoxIsDeleted.setChecked(True)
            else:
                self.checkBoxIsDeleted.setChecked(False)

    def SaveEmp(self):
        self.is_completed = False
        emp = Employee()
        emp.EmployeeCode = self.lineEditCode.text()
        emp.Name = self.lineEditName.text()
        emp.Phone = self.lineEditPhone.text()
        emp.Email = self.lineEditEmail.text()
        emp.Password = self.lineEditPassword.text()
        emp.IsDeleted = 0

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
        emp.EmployeeCode = self.lineEditCode.text()
        emp.Name = self.lineEditName.text()
        emp.Phone = self.lineEditPhone.text()
        emp.Email = self.lineEditEmail.text()
        emp.Password = self.lineEditPassword.text()
        if self.checkBoxIsDeleted.isChecked() == True:
            emp.IsDeleted = 1
        else:
            emp.IsDeleted = 0

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
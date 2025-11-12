from Midterm.connectors.connector import Connector
from Midterm.model.employee import Employee


class EmployeeConnector(Connector):
    def login(self, email, pwd):
        sql = "SELECT * FROM employee " \
              "where email= %s and password=%s"
        val = (email, pwd)

        dataset = self.fetchone(sql, val)
        if dataset == None:
            return None
        emp = Employee(dataset[0],
                       dataset[1],
                       dataset[2],
                       dataset[3],
                       dataset[4])
        return emp

    def get_all_employee(self):
        sql = "SELECT * FROM employee"
        datasets = self.fetchall(sql, None)
        # print(datasets)
        employee = []
        for dataset in datasets:
            emp = Employee(dataset[0],
                           dataset[1],
                           dataset[2],
                           dataset[3],
                           dataset[4])
            employee.append(emp)
        return employee

    def getDetailInfo(self, ID):
        sql = "SELECT * FROM employee " \
              "where EmployeeID = %s"
        val = (ID, )

        dataset = self.fetchone(sql, val)
        if dataset == None:
            return None
        emp = Employee(dataset[0],
                       dataset[1],
                       dataset[2],
                       dataset[3],
                       dataset[4])
        return emp

    def insertOneEmployee(self, emp):
        sql = "UPDATE `employee` " \
              "SET " \
              "`Name` = %s, " \
              "`Email` = %s, " \
              "`Password` = %s, " \
              "`Role` = %s " \
              "WHERE `EmployeeID` = %s; "\

        val = (emp.Name, emp.Email, emp.Password, emp.Role, emp.ID)
        result = self.insert_one(sql, val)
        return result

    def updateOneEmployee(self, emp):
        sql = "UPDATE `employee` "\
        "SET "\
        "`Name` = %s, "\
        "`Email` = %s, "\
        "`Password` = %s, "\
        "`Role` = %s "\
        "WHERE `EmployeeID` = %s; "\

        val = (emp.Name, emp.Email, emp.Password, emp.Role, emp.ID)
        result = self.insert_one(sql, val)
        return result

    def deletedOneEmployee(self, emp):
        sql = "DELETE FROM `employee` where EmployeeID = %s"
        val = (emp.ID, )
        result = self.insert_one(sql, val)
        return result

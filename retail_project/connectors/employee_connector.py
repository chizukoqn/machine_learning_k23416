from retail_project.connectors.connector import Connector
from retail_project.model.employee import Employee


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
                       dataset[4],
                       dataset[5],
                       dataset[6])
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
                           dataset[4],
                           dataset[5],
                           dataset[6])
            employee.append(emp)
        return employee

    def getDetailInfo(self, ID):
        sql = "SELECT * FROM employee " \
              "where ID = %s"
        val = (ID, )

        dataset = self.fetchone(sql, val)
        if dataset == None:
            return None
        emp = Employee(dataset[0],
                       dataset[1],
                       dataset[2],
                       dataset[3],
                       dataset[4],
                       dataset[5],
                       dataset[6])
        return emp

    def insertOneEmployee(self, emp):
        sql = "INSERT " \
        "INTO " \
        " `employee` " \
        "( " \
        "    `EmployeeCode`, " \
        "    `Name`, " \
        "    `Phone`, " \
        "    `Email`, " \
        "    `Password`, " \
        "    `IsDeleted`) " \
        "VALUES (%s, %s, %s, %s, %s, %s) "

        val = (emp.EmployeeCode, emp.Name, emp.Phone, emp.Email, emp.Password, emp.IsDeleted)
        result = self.insert_one(sql, val)
        return result

    def updateOneEmployee(self, emp):
        sql = "UPDATE `employee` "\
        "SET "\
        "`EmployeeCode` = %s, "\
        "`Name` = %s, "\
        "`Phone` = %s, "\
        "`Email` = %s, "\
        "`Password` = %s, "\
        "`IsDeleted` = %s "\
        "WHERE `ID` = %s; "\

        val = (emp.EmployeeCode, emp.Name, emp.Phone, emp.Email, emp.Password, emp.IsDeleted, emp.ID)
        result = self.insert_one(sql, val)
        return result
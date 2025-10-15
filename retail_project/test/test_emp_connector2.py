from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.model.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp = Employee()
emp.EmployeeCode = "EMP888"
emp.Name = "Manie"
emp.Phone = "03423523432"
emp.Email = "manie@gmail.com"
emp.Password = "123"
emp.IsDeleted = 0

result = ec.insertOneEmployee(emp)
if result> 0:
    print("yay")
else:
    print("cook")
from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.model.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp = Employee()
emp.ID = 7
emp.EmployeeCode = "EMP416"
emp.Name = "K23416"
emp.Phone = "03423523432"
emp.Email = "k23416@gmail.com"
emp.Password = "123"
emp.IsDeleted = 0

result = ec.updateOneEmployee(emp)
if result> 0:
    print("update ngon")
else:
    print("udate failed")
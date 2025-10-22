from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.model.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp = Employee()
emp.ID = 8

result = ec.deletedOneEmployee(emp)
if result> 0:
    print("update ngon")
else:
    print("udate failed")
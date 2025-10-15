from retail_project.connectors.employee_connector import EmployeeConnector

ec = EmployeeConnector()
ec.connect()
em = ec.login("putin@hotmail.com", "123")
if em == None:
    print("Login failed!")
else:
    print("Login successfull!")
    print(em)

#test get all emp
print("List All Emp")
ds = ec.get_all_employee()
print(ds)
for emp in ds:
    print(emp)

id = 3
emp = ec.getDetailInfo(id)
if emp == None:
    print("Không có nhân viên naào có mã =", id)
else:
    print("Có")
    print(emp)
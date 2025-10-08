import traceback
import mysql.connector

from retail_project.model.customer import Customer

server = "localhost"
port = 3306
database = "k23416_retail"
username = "root"
password="123456"
try:
    conn = mysql.connector.connect(
    host = server,
    port = port,
    database = database,
    user = username,
    password = password)
except:
    traceback.print_exc()

#Câu 1: Đăng nhập cho Customer
def login_customer(email, pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer " \
          "where email='"+email+"' and password='"+pwd+"'"

    cust = None

    cursor.execute(sql)

    dataset = cursor.fetchone() # tại chỉ 1 account
    if dataset != None:
        cust = Customer(dataset[0],dataset[1],dataset[2], dataset[3], dataset[4], dataset[5])
        # print("ID",dataset[0])
        # cust.ID, cust.Name, cust.Phone, cust.Email, cust.Password, cust.IsDeleted = dataset
    cursor.close()

    return cust

cust=login_customer("daodao@gmail.com","123")
if cust == None:
    print('login failed!')
else:
    print('login successful')
    print(cust)
import traceback
import mysql.connector

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
print("---Tiếp tục phần mềm---")
print("---CRUD---")

#Câu 1: Đăng nhập cho Customer
def login_customer(email, pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer " \
          "where email='"+email+"' and password='"+pwd+"'"
    print(sql)
    cursor.execute(sql)

    dataset = cursor.fetchone() # tại chỉ 1 account
    if dataset != None:
        print(dataset)
    else:
        print("login failed!")
    cursor.close()

login_customer("daodao@gmail.com","123")

def login_employee(email, pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM employee " \
          "where email= %s and password=%s"
    val = (email, pwd) #1 cái cũng phải ,
    cursor.execute(sql, val)

    dataset = cursor.fetchone() # tại chỉ 1 account
    if dataset != None:
        print(dataset)
    else:
        print("login failed!")
    cursor.close()

login_employee("kim@yahoo.com","123")
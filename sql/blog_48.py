import mysql.connector

server = "localhost"
port = 3306
database = "studentmanagement"
username = "root"
password="123456"

conn = mysql.connector.connect(
    host = server,
    port = port,
    database = database,
    user = username,
    password = password
)

print("(2.1) Truy vấn toàn bộ Sinh viên:")
cursor = conn.cursor()

sql="select * from student"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("-"*10)
print("(2.2) Truy vấn các Sinh viên có độ tuổi từ 22 tới 26:")
cursor = conn.cursor()
sql="SELECT * FROM student where Age>=22 and Age<=26"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("-"*10)
print("(2.3) Truy vấn toàn bộ sinh viên và sắp xếp theo tuổi tăng dần:")
cursor = conn.cursor()
sql="SELECT * FROM student " \
    "order by Age asc"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("-"*10)
print("(2.4) Truy vấn các Sinh viên có độ tuổi từ 22 tới 26 và sắp xếp theo tuổi giảm dần:")
cursor = conn.cursor()
sql="SELECT * FROM student " \
    "where Age>=22 and Age<=26 " \
    "order by Age desc "
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("-"*10)
print("(2.5) Truy vấn chi tiết thông tin Sinh viên khi biết Id:")
cursor = conn.cursor()
sql="SELECT * FROM student " \
    "where ID=1 "

cursor.execute(sql)

dataset=cursor.fetchone()
if dataset!=None:
    id,code,name,age,avatar,intro=dataset
    print("Id=",id)
    print("code=",code)
    print("name=",name)
    print("age=",age)

cursor.close()

print("-"*10)
print("(2.6) Truy vấn dạng phân trang Student:")
cursor = conn.cursor()
sql="SELECT * FROM student LIMIT 3 OFFSET 0"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("*** Truy vấn 3 dòng tiếp theo")
cursor = conn.cursor()
sql="SELECT * FROM student LIMIT 3 OFFSET 3"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("-"*10)
print("***Hiển thị 1 lần 3 dòng tới hết")
print("PAGING!!!!!")
cursor = conn.cursor()
sql="SELECT count(*) FROM student"
cursor.execute(sql)
dataset=cursor.fetchone()
rowcount=dataset[0]

limit=3
step=3
for offset in range(0,rowcount,step):
    sql=f"SELECT * FROM student LIMIT {limit} OFFSET {offset}"
    cursor.execute(sql)

    dataset=cursor.fetchall()
    align='{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code','Name',"Age"))
    for item in dataset:
        id=item[0]
        code=item[1]
        name=item[2]
        age=item[3]
        avatar=item[4]
        intro=item[5]
        print(align.format(id,code,name,age))

cursor.close()

cursor = conn.cursor()

print("")
print('-'*10)
print("(3.1) Thêm mới 1 Student")
sql = "insert into student (code, name, age) values (%s, %s, %s)"
val = ("sv07", "TDT", 45)

cursor.execute(sql, val)
conn.commit()
print(cursor.rowcount, " record inserted")

cursor.close()

print("")
print('-'*10)
print("(3.2) Thêm mới nhiều Student:")
cursor = conn.cursor()

sql="insert into student (CODE, NAME, AGE) values (%s,%s,%s)"

val=[
    ("sv08","Trần Quyết Chiến",19),
    ("sv09","Hồ Thắng",22),
    ("sv10","Hoàng Hà",25),
     ]

cursor.executemany(sql,val)

conn.commit()

print(cursor.rowcount," record inserted")

cursor.close()

print("")
print('-'*10)
print("(4.1) Cập nhật tên Sinh viên có Code=’sv09′ thành tên mới “Hoàng Lão Tà”")
cursor = conn.cursor()
sql="update student set name='Hoàng Lão Tà' where Code='sv09'"
cursor.execute(sql)

conn.commit()

print(cursor.rowcount," record(s) affected")

print("")
print('-'*10)
print("(4.2) Cập nhật tên Sinh viên có Code=’sv09′ thành tên mới “Hoàng Lão Tà” như viết dạng SQL Injection:")
cursor = conn.cursor()
sql="update student set name=%s where Code=%s"
val=[('Hoàng','sv09'),
     ('Thiên','sv10')]

cursor.executemany(sql,val)

conn.commit()

print(cursor.rowcount," record(s) affected")

print("")
print('-'*10)
print("(5.1) Xóa Student có ID=14")
sql="DELETE from student where ID=14"
cursor.execute(sql)

conn.commit()

print(cursor.rowcount," record(s) affected")

print("")
print('-'*10)
print("(5.2) Xóa Student có ID=13 với SQL Injection")
sql = "DELETE from student where ID=%s"
val = (13,)

cursor.execute(sql, val)

conn.commit()

print(cursor.rowcount," record(s) affected")
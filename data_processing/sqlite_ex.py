# trả về 1 df
# n customer tham gia vào thị trường nhiều nhất
# customerid    gias tri
import sqlite3
import pandas as pd

def find_top_customer(n):
    try:
        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
        cursor = sqliteConnection.cursor()
        print('DB Init')

        # write a query ad execute it with cursor
        n = int(n)
        query = f' SELECT c.CustomerId, SUM(i.Total) AS TotalAmount FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId GROUP BY c.CustomerId ORDER BY TotalAmount DESC LIMIT {n};'
        cursor.execute(query)

        # Fetch and output result
        column_names = [description[0] for description in cursor.description]
        df = pd.DataFrame(cursor.fetchall(), columns=column_names)
        print(df)
        # Close the cursor
        cursor.close()

    except sqlite3.Error as error:
        print('Error occurred - ', error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

n = int(input('nhập n: '))
print(find_top_customer(n))
import sqlite3
import pandas as pd

try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # write a query ad execute it with cursor
    query = ' SELECT * FROM InvoiceLine LIMIT 5;'
    cursor.execute(query)

    # Fetch and output result
    df = pd.DataFrame(cursor.fetchall())
    print(df)
    # Close the cursor
    cursor.close()

except sqlite3.Error as error:
    print('Error occurred - ', error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
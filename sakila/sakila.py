from flask import Flask
from flaskext.mysql import MySQL
import pandas as pd
app = Flask(__name__)


def getConnect(server, port, database, username, password):
    try:
        mysql = MySQL()
        # MySQL configurations
        app.config['MYSQL_DATABASE_HOST'] = server
        app.config['MYSQL_DATABASE_PORT'] = port
        app.config['MYSQL_DATABASE_DB'] = database
        app.config['MYSQL_DATABASE_USER'] = username
        app.config['MYSQL_DATABASE_PASSWORD'] = password
        mysql.init_app(app)
        conn = mysql.connect()
        return conn
    except mysql.connector.Error as e:
        print("Error = ", e)
    return None
def closeConnection(conn):
    if conn != None:
        conn.close()
def queryDataset(conn, sql):
    cursor = conn.cursor()

    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall())
    return df

conn = getConnect('localhost', 3306, 'sakila','root', '123456')

# Câu 1:
def customers_by_film(conn):
    sql1 = sql1 = "SELECT " \
           "f.film_id, " \
           "f.title AS film_title, " \
           "c.customer_id, " \
           "c.first_name, " \
           "c.last_name, " \
           "c.email, " \
           "r.rental_date, " \
           "r.return_date, " \
           "i.store_id " \
       "FROM film f " \
       "JOIN inventory i ON i.film_id = f.film_id " \
       "JOIN rental r ON r.inventory_id = i.inventory_id " \
       "JOIN customer c ON c.customer_id = r.customer_id " \
       "ORDER BY f.film_id, c.customer_id, r.rental_date"
    df1 = queryDataset(conn, sql1)
    return df1

print(customers_by_film(conn))

# Câu 2:
def customers_by_category(conn):
    sql2 = " SELECT DISTINCT " \
        "cat.category_id, " \
        "cat.name as category_name, " \
        "c.customer_id, " \
        "c.first_name, " \
        "c.last_name, " \
        "c.email " \
    "FROM category cat " \
    "JOIN film_category fc ON fc.category_id = cat.category_id " \
    "JOIN film f ON f.film_id = fc.film_id " \
    "JOIN inventory i ON i.film_id = f.film_id " \
    "JOIN rental r ON r.inventory_id = i.inventory_id " \
    "JOIN customer c ON c.customer_id = r.customer_id " \
    "ORDER BY cat.category_id, c.customer_id"
    df2 = queryDataset(conn, sql2)
    return df2

print(customers_by_category(conn))

# Câu 3
sql3 = "SELECT c.customer_id, " \
       "COUNT(r.rental_id) AS rental_count, " \
       "COUNT(DISTINCT i.film_id) AS distinct_films, " \
       "AVG(DATEDIFF(r.return_date, r.rental_date)) AS avg_rental_duration " \
    "FROM customer c " \
    "JOIN rental r ON c.customer_id = r.customer_id " \
    "JOIN inventory i ON r.inventory_id = i.inventory_id " \
    "GROUP BY c.customer_id"

df3 = queryDataset(conn, sql3)
df3.columns = ['CustomerId', 'Rental Count', 'Distinct Films', 'Avg Rental Duration']
print(df3.head())

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

columns = ['Rental Count', 'Distinct Films', 'Avg Rental Duration']
X = df3.loc[:, columns].values

# Dò số cụm tối ưu
def elbowMethod(df, columns):
    X = df.loc[:, columns].values
    inertia = []
    for n in range(1, 11):
        model = KMeans(n_clusters=n, init='k-means++', random_state=42)
        model.fit(X)
        inertia.append(model.inertia_)
    plt.figure(figsize=(10,5))
    plt.plot(np.arange(1, 11), inertia, 'o-')
    plt.xlabel('Số cụm (k)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal k')
    plt.show()

elbowMethod(df3, columns)

# Sau khi chọn số cụm
cluster = 4
kmeans = KMeans(n_clusters=cluster, init='k-means++', random_state=42)
labels = kmeans.fit_predict(X)
df3['Cluster'] = labels

print(df3.head())

plt.figure(figsize=(8,8))
sns.scatterplot(x='Rental Count', y='Distinct Films', hue='Cluster', data=df3, palette='Set2')
plt.title('Customer Clusters - Sakila')
plt.show()

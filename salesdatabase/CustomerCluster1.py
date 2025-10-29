from flask import Flask
from flaskext.mysql import MySQL
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from matplotlib.pyplot import margins
from sklearn.cluster import KMeans
import numpy as np
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

conn = getConnect('localhost', 3306, 'salesdatabase','root', '123456')

sql1 = "select * from customer"
df1 = queryDataset(conn, sql1)
# print(df1)

sql2 = "select distinct customer.CustomerId, Age, Annual_Income, Spending_Score " \
    "from customer, customer_spend_score " \
    "where customer.CustomerID = customer_spend_score.CustomerID"

df2 = queryDataset(conn, sql2)
df2.columns = ['CustomerId', 'Age', 'Annual Income', 'Spending Score']

# print(df2)
#
# print(df2.head())
#
# print(df2.describe())

def showHistogram(df, columns):
    plt.figure(1, figsize=(7, 8))
    n = 0
    for column in columns:
        n += 1
        plt.subplot(3, 1, n)
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        sns.distplot(df[column], bins=32)
        plt.title(f'Histogram of {column}')
    plt.show()

# showHistogram(df2, df2.columns[1:])

def elbowMethod(df, colunmsForElbow):
    X = df.loc[:, colunmsForElbow].values
    inertia = []
    for n in range(1, 11):
        model = KMeans(n_clusters=n,
                       init='k-means++',
                       max_iter=500,
                       random_state=42)
        model.fit(X)
        inertia.append(model.inertia_)

    plt.figure(1, figsize=(15, 6))
    plt.plot(np.arange(1, 11), inertia, 'o')
    plt.plot(np.arange(1, 11), inertia, '--', alpha=0.5)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Cluster sum of squared distances')
    plt.show()

columns=['Age', 'Spending Score']
# elbowMethod(df2, columns)

def runKMeans(X, cluster):
    model = KMeans(n_clusters=cluster,
                   init='k-means++',
                   max_iter=500,
                   random_state= 42)
    model.fit(X)
    labels = model.labels_
    centroids = model.cluster_centers_
    y_kmeans = model.fit_predict(X)
    return y_kmeans, centroids, labels
X = df2.loc[:, columns].values
cluster = 4
colors = ['red', 'green', 'blue', 'purple', 'black','pink','orange']

y_kmeans, centroids, labels = runKMeans(X, cluster)
# print(y_kmeans)
# print(centroids)
# print(labels)
# df2['cluster']=labels


def visualizeKMeans(X, y_kmeans, cluster, title, xlabel, ylabel, colors):
    plt.figure(figsize=(10,10))
    for i in range(cluster):
        plt.scatter(X[y_kmeans == i,0],
                    X[y_kmeans == i, 1],
                    s = 100,
                    c = colors[i],
                    label = 'Cluster %i'%(i+1))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

# visualizeKMeans(X, y_kmeans, cluster, "Clusters of Customers - Age X Spending Score", 'Age', "Spending Score", colors)

columns = ['Annual Income', 'Spending Score']
# elbowMethod(df2, columns)

X = df2.loc[:, columns].values
cluster = 5

y_kmeans, centroids, labels = runKMeans(X, cluster)

# print(y_kmeans)
# print(centroids)
# print(labels)
df2['cluster'] = labels

# visualizeKMeans(X, y_kmeans, cluster, "Clusters of Customers - Annual Incom X Spending Score", 'Annual Income', "Spending Score", colors)

columns = ['Age', 'Annual Income', 'Spending Score']
# elbowMethod(df2, columns)

X = df2.loc[:, columns].values
cluster = 6

y_kmeans, centroids, labels = runKMeans(X, cluster)

# print(y_kmeans)
# print(centroids)
# print(labels)
df2['cluster'] = labels

def visualize3DKmeans(df, columns, hover_data, cluster):
    fig = px.scatter_3d(df,
                        x = columns[0],
                        y = columns[1],
                        z = columns[2],
                        color = 'cluster',
                        hover_data= hover_data,
                        category_orders={'cluster': range(0, cluster)},
                        )
    fig.update_layout(margin=dict(l=0, r=0, b = 0, t = 0))
    fig.show()
hover_data = df2.columns
visualize3DKmeans(df2, columns, hover_data, cluster)

def showCustomerDetailsConsole(conn, df_clustered):
    cursor = conn.cursor()
    for cluster_id in sorted(df_clustered['cluster'].unique()):
        print(f"\n===== Cụm {cluster_id} =====")

        customer_ids = df_clustered[df_clustered['cluster'] == cluster_id]['CustomerId'].tolist()
        if not customer_ids:
            print("Không có khách hàng trong cụm này.")
            continue


        format_ids = ', '.join([str(i) for i in customer_ids])
        sql = f"SELECT * FROM customer WHERE CustomerId IN ({format_ids})"
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)

# Xuất ra console
showCustomerDetailsConsole(conn, df2)


from flask import render_template_string

@app.route('/clusters')
def showCustomerDetailsWeb():
    cursor = conn.cursor()
    cluster_data = {}

    for cluster_id in sorted(df2['cluster'].unique()):
        customer_ids = df2[df2['cluster'] == cluster_id]['CustomerId'].tolist()
        if not customer_ids:
            continue
        format_ids = ', '.join([str(i) for i in customer_ids])
        sql = f"SELECT * FROM customer WHERE CustomerId IN ({format_ids})"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        df_customers = pd.DataFrame(rows, columns=cols)
        cluster_data[cluster_id] = df_customers.to_html(index=False, classes='table table-bordered table-striped')

    html_template = """
    <html>
    <head>
        <title>Customer Clusters</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
    </head>
    <body class="p-4">
        <h2 class="mb-4">Danh sách chi tiết Customer theo từng cụm</h2>
        {% for cluster_id, table_html in cluster_data.items() %}
            <h4 class="mt-4">Cụm {{ cluster_id }}</h4>
            {{ table_html|safe }}
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html_template, cluster_data=cluster_data)
import webbrowser
from threading import Timer

if __name__ == '__main__':
    url = "http://127.0.0.1:5000/clusters"
    print(f"\nFlask app is running at {url}")

    def open_browser():
        webbrowser.open_new(url)

    Timer(1, open_browser).start()  # mở sau 1 giây

    app.run(debug=False)  # tắt debug để tránh reload 2 lần


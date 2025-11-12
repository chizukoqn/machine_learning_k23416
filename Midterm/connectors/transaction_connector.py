from Midterm.connectors.connector import Connector
import pandas as pd

class TransactionConnector(Connector):
    def clean_data(self):
        """Làm sạch dữ liệu (bỏ trùng ID, missing)"""
        sql = "SELECT * FROM transaction"
        df = pd.read_sql(sql, self.conn)
        df = df.drop_duplicates(subset=["Id"], keep="first")
        df = df.dropna(subset=["InvoiceNo", "CustomerID", "Quantity", "UnitPrice"])
        df["Total"] = df["Quantity"] * df["UnitPrice"]
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
        df = df.dropna(subset=["InvoiceDate"])
        return df

    def get_invoice_max(self):
        df = self.clean_data()
        max_row = df.groupby("InvoiceNo")["Total"].sum().reset_index().sort_values(by="Total", ascending=False).head(1)
        return max_row.iloc[0].to_dict()

    def get_top_customers(self, t1, t2, n=5):
        df = self.clean_data()
        df_filtered = df[(df["InvoiceDate"] >= t1) & (df["InvoiceDate"] <= t2)]
        top_customers = (
            df_filtered.groupby("CustomerID")["Total"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
            .reset_index()
        )
        return top_customers

    def get_chart_data(self):
        df = self.clean_data()
        df["Year"] = df["InvoiceDate"].dt.year
        chart_data = df.groupby(["Country", "Year"])["Total"].sum().reset_index()
        return chart_data

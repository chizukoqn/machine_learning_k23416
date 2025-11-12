import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from datetime import datetime
from Midterm.uis.StatisticMainWindow import Ui_MainWindow

class StatisticMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.btnInvoiceMax.clicked.connect(self.show_invoice_max)
        self.btnTopCustomer.clicked.connect(self.show_top_customer)
        self.btnChart.clicked.connect(self.show_chart)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Hạng mục", "Kết quả"])
        self.showWindow()

    def showWindow(self):
        self.MainWindow.show()

    # ----------- Helper functions -----------
    def load_data(self):
        """Đọc dữ liệu từ SQLite và làm sạch"""
        try:
            conn = sqlite3.connect("transaction.db")
            df = pd.read_sql_query("SELECT * FROM transaction", conn)
            conn.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể đọc dữ liệu: {e}")
            return None

        # Làm sạch dữ liệu
        df = df.drop_duplicates(subset=["Id"], keep="first")
        df = df.dropna(subset=["InvoiceNo", "CustomerID", "Quantity", "UnitPrice"])
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
        df["Total"] = df["Quantity"] * df["UnitPrice"]
        return df

    def show_table(self, data_dict):
        """Hiển thị kết quả lên bảng"""
        self.tableWidget.setRowCount(len(data_dict))
        for i, (key, val) in enumerate(data_dict.items()):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(key)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(val)))

    # ----------- 1️⃣ Invoice có trị giá lớn nhất -----------
    def show_invoice_max(self):
        df = self.load_data()
        if df is None or df.empty:
            QMessageBox.warning(None, "Cảnh báo", "Không có dữ liệu hợp lệ.")
            return
        invoice_sum = df.groupby("InvoiceNo")["Total"].sum().reset_index()
        max_row = invoice_sum.loc[invoice_sum["Total"].idxmax()]
        result = {
            "InvoiceNo": int(max_row["InvoiceNo"]),
            "Tổng giá trị": round(max_row["Total"], 2)
        }
        self.show_table(result)

    # ----------- 2️⃣ Top N Customer theo khoảng thời gian -----------
    def show_top_customer(self):
        df = self.load_data()
        if df is None or df.empty:
            return
        t1 = self.dateEditT1.date().toString("yyyy-MM-dd")
        t2 = self.dateEditT2.date().toString("yyyy-MM-dd")
        n = self.spinBoxN.value()

        try:
            t1 = pd.to_datetime(t1)
            t2 = pd.to_datetime(t2)
        except:
            QMessageBox.warning(None, "Lỗi", "Ngày không hợp lệ.")
            return

        df_filtered = df[(df["InvoiceDate"] >= t1) & (df["InvoiceDate"] <= t2)]
        top_customers = (
            df_filtered.groupby("CustomerID")["Total"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
            .reset_index()
        )

        data_dict = {str(row.CustomerID): round(row.Total, 2) for _, row in top_customers.iterrows()}
        self.show_table(data_dict)

    # ----------- 3️⃣ Biểu đồ Chart phân bố theo năm & quốc gia -----------
    def show_chart(self):
        df = self.load_data()
        if df is None or df.empty:
            return
        df["Year"] = df["InvoiceDate"].dt.year
        chart_data = df.groupby(["Country", "Year"])["Total"].sum().reset_index()

        pivot = chart_data.pivot(index="Year", columns="Country", values="Total").fillna(0)
        pivot.plot(kind="bar", figsize=(10, 6))
        plt.title("Phân bố doanh thu theo năm và quốc gia")
        plt.ylabel("Tổng giá trị")
        plt.xlabel("Năm")
        plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.tight_layout()
        plt.show()

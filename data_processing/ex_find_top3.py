# đầu vào: 1 df
# Đầu ra: top 3 sp bán ra nhưng có gias trị lớn nhất

import pandas as pd

def find_top_3_product(df):
    #tổng giá trị từng đơn hàng
    product_total = df.groupby('ProductID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())

    product_sorted = product_total.sort_values(ascending=False)
    return product_sorted.head(3)

df = pd.read_csv('../dataset/SalesTransactions/SalesTransactions.csv')
result = find_top_3_product(df)
print(result)
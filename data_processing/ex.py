import pandas as pd


def find_order_with_range(df, minValue, maxValue):
    #tổng giá trị từng đơn hàng
    order_total = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())

    #lọc đơn hàng trong range
    order_with_range = order_total[(order_total >= minValue) & (order_total <= maxValue)]

    #danh sách các mã đơn hàng khng trùng nhau
    unique_orders = df[df['OrderID'].isin(order_with_range.index)]['OrderID'].drop_duplicates().tolist()

    return unique_orders

df = pd.read_csv('../dataset/SalesTransactions/SalesTransactions.csv')
minValue = float(input("Nhập giá trị min: "))
maxValue = float(input("Nhập giá trị max: "))
result = find_order_with_range(df, minValue, maxValue)
print('Danh sách các hóa đơn trong phạm vi giá trị từ', minValue, 'đến', maxValue, ' là:', result)
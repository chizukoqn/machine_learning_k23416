import pandas as pd

"""
-DataFrame => df
-Tổng Giá Trị Min =>minValue
-Tổng Giá Trị Max =>maxValue
-SortType=>True/False
-Trả về danh sách các hóa đơn (mã hóa đơn + tổng giá trị ) mà tổng trị giá của nó nằm trong [minValue …maxValue] và sắp xếp theo SortType
"""

def find_order_with_range_and_sort(df, minValue, maxValue, SortType):
    #tổng giá trị từng đơn hàng
    order_total = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())

    #lọc đơn hàng trong range
    order_with_range = order_total[(order_total >= minValue) & (order_total <= maxValue)]

    order_sorted = order_with_range.sort_values(ascending=SortType)
    return order_sorted

df = pd.read_csv('../dataset/SalesTransactions/SalesTransactions.csv')
minValue = float(input("Nhập giá trị min: "))
maxValue = float(input("Nhập giá trị max: "))
SortType = input('Bạn có muốn sắp xếp tăng dần không? y/n ')
if SortType == 'y':
    SortType = True
result = find_order_with_range_and_sort(df, minValue, maxValue, SortType)
print('Danh sách các hóa đơn trong phạm vi giá trị từ', minValue, 'đến', maxValue, 'và có sắp xếp là:', result)
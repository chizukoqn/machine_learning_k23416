from numpy import nan as NA
import pandas as pd

# Lọc dữ liệu bị thiếu (Filtering Out Missing Data)
data = pd.DataFrame([[1., 6.5, 3],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)
cleaned = data.dropna()
print(cleaned) #loại hết các dòng có NA
print("-"*10)
cleaned2 = data.dropna(how='all')
print(cleaned2) #lọai dòng mà tất cả phần tử đều là NA
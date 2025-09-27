from numpy import nan as NA
import pandas as pd

#Điền dữ liệu còn thiếu(Filling In Missing Data)
data = pd.DataFrame([[1., 6.5, 3],
                     [2., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.],
                     [6.,8.,9.]])
print(data)
print("-"*10)
cleaned = data.fillna(data.mean())
print(cleaned) #Thay NA bằng mean(trung bình) giá trị theo cột
#Ví dụ cột đầu tiên có (1 + 2 + 6)/3 = 3
# -> Các NA còn lại đều thay bằng 3
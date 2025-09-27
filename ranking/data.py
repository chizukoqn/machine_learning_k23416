import pandas as pd
import random

# Các thuộc tính
colors = ["đen", "trắng", "xanh", "bạc", "vàng"]
storages = ["64GB", "128GB", "256GB"]
types = ["smartphone", "điện thoại gập", "điện thoại phổ thông"]

# Một số truy vấn giả lập
queries = [
    "mua smartphone pin trâu",
    "điện thoại gập sang trọng",
    "điện thoại phổ thông giá rẻ",
    "smartphone chơi game cấu hình mạnh"
]

data = []
for i in range(40):
    q = random.choice(queries)          # chọn 1 query
    c = random.choice(colors)           # màu
    s = random.choice(storages)         # bộ nhớ
    t = random.choice(types)            # loại
    doc = f"{t} {c} {s}"                # tài liệu mô tả sp
    rel = random.randint(0, 3)          # nhãn relevance (0: không liên quan, 3: rất liên quan)
    data.append([q, c, s, t, doc, rel])

# Xuất ra CSV
df = pd.DataFrame(data, columns=["truy_van", "mau", "bo_nho", "loai", "doc", "relevance"])
df.to_csv("ranking_phone.csv", index=False, encoding="utf-8-sig")

print("File ranking_phone.csv đã tạo:", len(df), "dòng")
print(df.head(10))

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load data
df = pd.read_csv("ranking_phone.csv")

# Chọn các cột đặc trưng
X_raw = df[["mau", "bo_nho", "loai"]]
y = df["relevance"]

# One-hot encode
enc = OneHotEncoder()
X = enc.fit_transform(X_raw)

# Train/test split
train_size = int(0.7 * len(df))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Hồi quy
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("=== Pointwise (Điện thoại) ===")
print("MSE:", mean_squared_error(y_test, y_pred))
print("Dự đoán:", [round(float(v), 2) for v in y_pred])
print("Thực tế:", y_test.tolist())

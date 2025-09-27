import pandas as pd
import itertools
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from scipy.sparse import vstack

# Load data
df = pd.read_csv("ranking_phone.csv")  # đổi tên file cho khớp
X_raw = df[["mau", "bo_nho", "loai"]]  # sửa cho dataset điện thoại
y_all = df["relevance"].values

# One-hot encode
enc = OneHotEncoder()
X_all = enc.fit_transform(X_raw)

pairs_X, pairs_y = [], []

# Tạo cặp trong từng query
for q in df["truy_van"].unique():
    sub = df[df["truy_van"] == q]
    for (i, j) in itertools.combinations(sub.index, 2):
        if y_all[i] == y_all[j]:
            continue
        label = 1 if y_all[i] > y_all[j] else 0
        diff = X_all[i] - X_all[j]   # so sánh sự khác biệt giữa 2 sản phẩm
        pairs_X.append(diff)
        pairs_y.append(label)

pairs_X = vstack(pairs_X)

# Train/test split
train_size = int(0.7 * len(pairs_y))
X_train, X_test = pairs_X[:train_size], pairs_X[train_size:]
y_train, y_test = pairs_y[:train_size], pairs_y[train_size:]

# Train Logistic Regression
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("=== Pairwise (Điện thoại) ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Số cặp test:", len(y_test))

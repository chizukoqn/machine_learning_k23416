import math
import matplotlib as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error

x1=np.array([[0.76, 4.25, 5.71, 3.58, 0.45, 0.13, 1., 0.76, 7.56, 0.76, 0.42, 2.93, 5.64, 3.93, 0.5, 0.2, 1.09, 1.95, 3.81, 5.41,
]]).T
x2=np.array([[7.01,14.45,42.28,11.13,3.,63.46,48.25,24.8,13.85,50.46,3.1,
11.21,18.11,21.56,11.2,7.62,22.54,44.38,5.5,11.73,]]).T
x3=np.array([[0.94,0.84,0.83,0.24,0.48,0.18,0.35,0.34,0.55,0.43,0.94,0.53,0.09,0.43,0.79,0.33,0.94,0.9,0.61,0.29]]).T
y=np.array([[33.52,42.89,12.04,6.91,6.57,2.07,4.18,58.45,29.64,48.87,
33.75,0.04,16.75,4.63,61.69,24.55,32.9,9.23,11.4,27.64]]).T
X = np.concatenate([x1, x2, x3], axis=1)
regr = linear_model.LinearRegression(fit_intercept=True)
regr.fit(X, y)
ypred=regr.predict(X)
r2 = r2_score(y, ypred)
mse = mean_squared_error(y, ypred)
rmse=math.sqrt(mse)

print("Coeficient :", regr.coef_)
print("Interception:", regr.intercept_)
print(f"R^2 score   : {r2:.4f}")
print(f"MSE         : {mse:.4f}")
print(f"RMSE        : {rmse:.4f}")
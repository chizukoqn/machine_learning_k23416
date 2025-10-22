import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

x = np.array([[73.5,75,76.5,79,81.5,82.5,84,85,86.5,87.5,89,90,91.5,]]).T
y = np.array([[1.49,1.5,1.51,1.54,1.58,1.59,1.6,1.62,1.63,1.64,1.66,1.67,1.68]]).T
X = np.concatenate([x], axis = 1)

def calculateb1b0(x,y):
    xbar = np.mean(x)
    ybar = np.mean(y)
    x2bar = np.mean( x**2)
    xybar = np.mean( x*y)

    b1 = (xbar * ybar - xybar) / (xbar ** 2 - (x2bar))
    b0 = ybar - b1 * xbar
    return b1,b0

b1, b0 = calculateb1b0(x,y)
print("b1", b1)
print("b0", b0)

regr = linear_model.LinearRegression(fit_intercept=True)

regr.fit(X,y)

print("Coeficient: ", regr.coef_)
print('Interception: ',regr.intercept_)

ypred = regr.predict(X)


def showGraph(x,y_act,ypred, title = "", xlabel = "", ylabel =""):
    plt.figure(figsize=(14,8))
    plt.plot(x,y_act, 'r-o', label = "price actual")
    plt.plot(x, ypred, '--', label = "price predict")
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y_act)
    y_max = np.max(y_act)

    ybar = np.mean(y_act)

    plt.axhline(ybar, linestyle='--', linewidth=4, label = 'mean actual' )
    plt.axis([x_min*0.95, x_max*1.05, y_min*0.95, y_max*1.05])
    plt.xlabel(xlabel, fontsize = 16)
    plt.ylabel(ylabel, fontsize = 16)
    plt.text(x_min, ybar *1.01, "mean actual", fontsize = 16)
    plt.legend(fontsize=15)
    plt.title(title,fontsize=20)
    plt.show()

showGraph(x,y,ypred,
          title = 'Dự báo Giá nhà theo diện tích',
          xlabel= 'Diện tích (m2)',
          ylabel = 'Giá nhà (tỷ VND)')
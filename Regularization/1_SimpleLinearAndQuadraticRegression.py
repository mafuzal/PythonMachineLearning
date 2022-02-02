# %%  Importing the librariers 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

# %%  Importing and preparing the dataset 
df = pd.read_csv("ManualLRDS.csv")
df.head()
x_Test_Data = 3.5
y_Test_Data = 1.4
# %%
#Training we calculate beta 
x = df['x']
xVec = X=(np.column_stack((np.ones(np.size(x)),x)))
yVec = df['y']
X_Transpose_Vec = np.transpose(xVec)
Beta_Part1 = np.dot(X_Transpose_Vec,xVec)
Beta_Part1 = np.linalg.inv(Beta_Part1)
Beta_Part2 = np.dot(X_Transpose_Vec,yVec)
Beta = np.dot(Beta_Part1,Beta_Part2)
print('Beta = ',Beta)
# %% Prediction 
x_predict = np.array([[1,x_Test_Data]])
y_hat = np.dot(x_predict,Beta)
print('Prediction:Y_Hat = ',y_hat)
sum_Squares = (y_Test_Data - y_hat)**2
print('SE = ',sum_Squares)
# %% Collect Y-Hats 
collectY_Hats= []
for i in range(len(yVec)):
    collectY_Hats.append(np.dot(xVec[i],Beta))

# %% Linear Regression Plot 
plt.scatter(x, yVec, color='red',label='Training Data')
plt.plot(x, collectY_Hats, label='Prediction Curve' )
plt.plot(x_Test_Data,y_Test_Data,'ko',label='Test Data') 
plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.title('Linear Regression Asignment 1 - 5a')
plt.legend(['Prediction Curve','Test Data','Training Data'],loc='lower right')
plt.grid()
plt.show()

# %% Convert Linear Regression Model to Polynomial Regression
#Data Preparation
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X_Array = np.array(x)[:, np.newaxis]
Y_Array = np.array(yVec)

lr = LinearRegression()
pr = LinearRegression()
quadratic = PolynomialFeatures(degree=2)
X_quad = quadratic.fit_transform(X_Array)

# %% fit quadratic features
pr.fit(X_quad, Y_Array)
X_fit = np.arange(1,5,2)[:, np.newaxis]
y_quad_fit = pr.predict(quadratic.fit_transform(X_fit))

# %% plot Quadratic Regression Results
plt.plot(x, collectY_Hats, label='Linear Regression' )
plt.plot(X_fit, y_quad_fit,label='Quadratic Fit')
plt.scatter(x, yVec, color='red',label='Training Data')
plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.title('Quadratic Regression Asignment 1 - 5b')
plt.legend(['Linear Regression','Quadratic Fit','Training Data'],loc='lower right')
plt.grid()
plt.show()



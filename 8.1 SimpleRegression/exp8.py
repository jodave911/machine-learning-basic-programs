import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
dataset.head()
X = dataset.iloc[:, :-1].values  
y = dataset.iloc[:,1].values  

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/3,random_state=0)

regressor = LinearRegression()
regressor.fit(X_train,y_train) 
y_pred = regressor.predict(X_test) 
y_pred
y_test

plt.scatter(X_train, y_train, color='red') 
plt.plot(X_train, regressor.predict(X_train), color='blue') 
plt.title("Salary vs Experience (Training set)") 
plt.xlabel("Years of experience") 
plt.ylabel("Salaries") 
plt.show() 
plt.scatter(X_test, y_test, color='red') 
plt.plot(X_train, regressor.predict(X_train), color='blue') 
plt.title("Salary vs Experience (Testing set)")
plt.xlabel("Years of experience") 
plt.ylabel("Salaries") 
plt.show() 

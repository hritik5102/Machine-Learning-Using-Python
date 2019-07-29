import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split

data = pd.read_csv("headbrain6.csv")
#print(data.head())

x = data.iloc[:,2:3].values
y = data.iloc[:,3:4].values

print(x.head())

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=1/4,random_state=0)

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(x_train,y_train)



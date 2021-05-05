from patsy import dmatrix
import statsmodels.api as sm
import statsmodels.formula.api as smf
from math import sqrt
from sklearn.metrics import mean_squared_error
# import modules
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt 

# read data_set
data = pd.read_csv("learnt_index_rand.csv")

data.head()

data_x = data['key']
data_y = data['index']

# Dividing data into train and validation datasets
from sklearn.model_selection import train_test_split
train_x, valid_x, train_y, valid_y = train_test_split(data_x, data_y, test_size=0.33, random_state = 1)

# Visualize the relationship b/w key and index
import matplotlib.pyplot as plt
#plt.scatter(train_x, train_y, facecolor='None', edgecolor='k', alpha=0.3)
#plt.show()

# Generating cubic spline with 3 knots at 25, 40 and 60
transformed_x = dmatrix("bs(train, knots=(25,40,60), degree=3, include_intercept=False)", {"train": train_x},return_type='dataframe')

# Fitting Generalised linear model on transformed dataset
fit1 = sm.GLM(train_y, transformed_x).fit()

# Predictions on both splines
pred1 = fit1.predict(dmatrix("bs(valid, knots=(25,40,60), include_intercept=False)", {"valid": valid_x}, return_type='dataframe'))
pred2 = fit2.predict(dmatrix("bs(valid, knots=(25,40,50,65),degree =3, include_intercept=False)", {"valid": valid_x}, return_type='dataframe'))

# Calculating RMSE values
rms1 = sqrt(mean_squared_error(valid_y, pred1))
print(rms1)

# We will plot the graph for 70 observations only
#CHANGE
xp = np.linspace(valid_x.min(),valid_x.max(),1000)

# Make some predictions
pred1 = fit1.predict(dmatrix("bs(xp, knots=(25,40,60), include_intercept=False)", {"xp": xp}, return_type='dataframe'))

# Plot the splines and error bands
plt.scatter(data.key, data.index, facecolor='None', edgecolor='k', alpha=0.1)
plt.plot(xp, pred1, label='Specifying degree =3 with 3 knots')
plt.legend()
plt.xlim(15,85)
plt.ylim(0,350)
plt.xlabel('key')
plt.ylabel('index')
plt.show()

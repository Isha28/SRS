import numpy as np
import matplotlib.pyplot as plt
import pwlf
import pandas as pd
import random
from math import sqrt
from sklearn.metrics import mean_squared_error

data = pd.read_csv("learnt_index_rand.csv")
data.head()

x = data['key']
y = data['index']

#x = [i+1 for i in xrange(100000)]
#y = [j+random.randint(100000,300000) for j in xrange(100000)]
#y = [j+100000 for j in xrange(100000)]

#print "Isha"
#print y

#x = np.array(x) 
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
#y = np.array(y)
#[5, 7, 9, 11, 13, 15, 28, 42, 56, 70,
#              84, 98, 112, 126, 140])

my_pwlf = pwlf.PiecewiseLinFit(x, y)
breaks = my_pwlf.fit(3)
#print(breaks)

x_hat = np.linspace(x.min(), x.max(), 1000)
y_hat = my_pwlf.predict(x_hat)

plt.figure()
plt.plot(x, y, 'o')
plt.plot(x_hat, y_hat, '-')
plt.show()

#print "Actual"
#print y
#print "Predicted"
#print y_hat

rms1 = sqrt(mean_squared_error(y, y_hat))
print("RMSE VALUE")
print(rms1)

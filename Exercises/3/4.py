import matplotlib.pyplot as plt
import numpy as np

# ridge_regression
def ridge_regression_error(y_pred, y, labmda, m):
   sum1 = sum2 = 0
   for i in range(len(y)):
      sum1 += (y_pred[i] - y[i])**2
   for i in range(len(y)):
      sum2 += labmda * (m**2)
   return sum1 + sum2

# simple_regression
def simple_regression_error(y_pred, y):
   sum = 0
   for i in range(len(y)):
      sum += (y_pred[i] - y[i])**2
   return sum

# Data
x_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_data = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]
x = np.array([x_data]).reshape(len(x_data), 1)
y = np.array([y_data]).reshape(len(y_data), 1)

# Train Phase
phi_train = np.concatenate((np.ones((len(x),1)),x),axis=1)
        
# estimating coefficients 
theta = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(phi_train),phi_train)), np.transpose(phi_train)),y)

# predicted response vector  
y_pred = np.matmul(phi_train, theta)

y_error = simple_regression_error(y_pred, y)
print("simple_regression_error: ", y_error)

y_error2 = ridge_regression_error(y_pred, y, 0.5, 0.5)
print("ridge_regression_error: ", y_error2)

# Plot outputs
plt.scatter(x, y,  color='black', label="Real data")
plt.plot(x, y_pred, color='blue', linewidth=3, label="Prediction Line")
plt.legend()
plt.show()
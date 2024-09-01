# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Implementing of F(X) function
def F(X):
    # X[0]: x1 , X[1]: x2
    return np.power(X[0],2) + (4*np.power(X[1],2)) - (4*X[0]) - (8*X[1])

# Creating 2D-meshgrid space for x1 and x2 dimensions 
start, stop, n_values = -20, 20, 100
x1 = np.linspace(start, stop, n_values)
x2 = np.linspace(start, stop, n_values)
X1, X2 = np.meshgrid(x1, x2)
  
# Calculating the value of F(X) function for 2D-meshgrid space as Y
Y = F([X1, X2])
print("Global-minimum of F(x) function for 2D-meshgrid space is: ", np.amin(Y))

# Drawing contour levels on plot
cp = plt.contourf(X1, X2, Y)
plt.colorbar(cp)

# Other settings on plot
plt.tight_layout()
plt.vlines(0, start, stop, color="black", linestyle="dashed") 
plt.hlines(0, start, stop, color="black", linestyle="dashed")
plt.title('Contour Plot') 
plt.xlabel('x1') 
plt.ylabel('x2') 

# Showing results
plt.tight_layout()
plt.show() 
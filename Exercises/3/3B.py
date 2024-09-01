# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import numdifftools as nd

# Implementing of F(X) function
def F(X):
    # X[0]: x1 , X[1]: x2
    return np.power(X[0],2) + (4*np.power(X[1],2)) - (4*X[0]) - (8*X[1])

# creating 2D-meshgrid space for x1 and x2 borders
start, stop, n_values = -1, 6, 100
x1 = np.linspace(start, stop, n_values)
x2 = np.linspace(start, stop, n_values)
X1, X2 = np.meshgrid(x1, x2)  

# Calculating the value of F(X) function for 2D-meshgrid space as Y
Y = F([X1, X2])

# Drawing contour levels on plot
cp = plt.contourf(X1, X2, Y)
plt.colorbar(cp)

# Other settings on plot
plt.tight_layout()
plt.vlines(0, start, stop, color="black", linestyle="dashed") 
plt.hlines(0, start, stop, color="black", linestyle="dashed")
plt.title('Gradient Descent on Contour Plot') 
plt.xlabel('x1') 
plt.ylabel('x2') 

#########################################################################################
# ==> Gradient Descent <==
# Gradient Descent is an iterative optimiZation algorithm, used to find the minimum value
# for a function. The general idea is to initialize the parameters to random values, and
# then take small steps in the direction of the “slope” at each iteration. 
# - source: https://www.geeksforgeeks.org/optimization-techniques-for-gradient-descent/
#########################################################################################
alpha = 0.01                        # learning rate
startPoint = [2, 2]                 # start point 

x1_start = startPoint[0]            # x1 for start point 
x2_start = startPoint[1]            # x2 for start point 
y_start = F([x1_start, x2_start])   # result of F(X) in start points [x1_start , x2_start]
plt.scatter(x1_start, x2_start, c='r', s=5)

result_string = "learning rate = " + str(alpha) +\
                "\nstart point = " + str([x1_start, x2_start]) +\
                "\n\nresults: \n"

# Start
print("==> Start Running Gradient Descent Algorithm")
tmp_nIteration = 0
while True:
    gradient_F = nd.Gradient(F)([x1_start, x2_start])

    tmp_x1 = x1_start + alpha * (-gradient_F[0])
    tmp_x2 = x2_start + alpha * (-gradient_F[1])
    tmp_y = F([tmp_x1, tmp_x2])
    
    result_string += str(tmp_nIteration+1) + ": " + str([tmp_x1, tmp_x2]) + " = " + str(tmp_y) + "\n"
    plt.scatter(tmp_x1, tmp_x2, c='r', s=5)
    
    # Convergence condition
    if abs(tmp_x1 - x1_start) == 0 and abs(tmp_x2 - x2_start) == 0:
        break
    
    x1_start = tmp_x1
    x2_start = tmp_x2
    y_start = tmp_y
    tmp_nIteration += 1 

# Finished
print("==> Gradient Descent Algorithm Finished")

# Writing results in text file
f = open("results/3B_result" + str([startPoint[0], startPoint[1]]) + ".txt", "w")
f.write(result_string)
f.close()

# Showing results
plt.tight_layout()
plt.show()
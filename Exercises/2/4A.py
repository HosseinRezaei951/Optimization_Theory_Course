# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import numdifftools as nd

# Implementing of F(X) function
def F(X):
    # X[0]: x1 , X[1]: x2
    return -np.cos(X[0])*np.cos(X[1])*np.exp(-np.power((X[0]-np.pi),2)-np.power((X[1]-np.pi),2))

# creating 2D-meshgrid space for x1 and x2 borders
start, stop, n_values = -2, 5, 100
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
plt.title('Contour Plot') 
plt.xlabel('x1') 
plt.ylabel('x2') 

#########################################################################################
# ==> Newton Method <==
#########################################################################################
alpha = 0.1                         # learning rate
startPoint = [0.75, -1.25]          # start point 

x1_start = startPoint[0]            # x1 for start point 
x2_start = startPoint[1]            # x2 for start point 
y_start = F([x1_start, x2_start])   # result of F(X) in start points [x1_start , x2_start]
plt.scatter(x1_start, x2_start, c='r', s=5)

result_string = "learning rate = " + str(alpha) +\
                "\nstart point = " + str([x1_start, x2_start]) +\
                "\n\nresults: \n"

# Start
print("==> Start Running Newton Method Algorithm")
tmp_nIteration = 0
while True:
    hessianMatrix_F = nd.Hessian(F)([x1_start, x2_start])
    inverse_hessianMatrix_F = np.linalg.inv(hessianMatrix_F)
    gradient_F = nd.Gradient(F)([x1_start, x2_start])
    P = -np.matmul(inverse_hessianMatrix_F, gradient_F)

    tmp_x1 = x1_start + alpha * P[0]
    tmp_x2 = x2_start + alpha * P[1]
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
print("==> Newton Method Algorithm Finished")

# Writing results in text file
f = open("results/4A_result" + str([startPoint[0], startPoint[1]]) + ".txt", "w")
f.write(result_string)
f.close()

# Showing results
plt.tight_layout()
plt.show()
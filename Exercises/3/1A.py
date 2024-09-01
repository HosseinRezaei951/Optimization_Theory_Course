# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import numdifftools as nd
np.seterr(divide='ignore', invalid='ignore')

# Implementing of F(X) function
def F(X):
    # X[0]: x1 , X[1]: x2
    return (10 * np.power(X[0],2)) + (np.power(X[1],2))

# Creating 2D-meshgrid space for x1 and x2 dimensions 
n_values = 100
x1 = np.linspace(-0.2, 0.2, n_values)
x2 = np.linspace(-0.2, 1.2, n_values)
X1, X2 = np.meshgrid(x1, x2)
  
# Calculating the value of F(X) function for 2D-meshgrid space as Y
Y = F([X1, X2])

# Drawing contour levels on plot
cp = plt.contourf(X1, X2, Y)
plt.colorbar(cp)

# Other settings on plot
plt.tight_layout()
plt.hlines(0, -0.2, 0.2, color="black", linestyle="dashed")
plt.vlines(0, -0.2, 1.2, color="black", linestyle="dashed") 
plt.title('Contour Plot') 
plt.xlabel('x1') 
plt.ylabel('x2') 

#########################################################################################
# ==> Newton Method(MR-1) <==
#########################################################################################
alpha = 0.1                         # learning rate
startPoint = [0.1, 1]               # start point 
x1_start = startPoint[0]            # x1 for start point 
x2_start = startPoint[1]            # x2 for start point 
y_start = F([x1_start, x2_start])   # result of F(X) in start points [x1_start , x2_start]
x1_list = []
x2_list = []
x1_list.append(x1_start)
x2_list.append(x2_start)

result_string = "learning rate = " + str(alpha) +\
                "\nstart point = " + str([x1_start, x2_start]) +\
                "\n\nresults: \n"

# Start
print("==> Start Running Newton Method(MR-1) Algorithm")
tmp_nIteration = 1

# first iteration
gradient = np.array([nd.Gradient(F)([x1_start, x2_start])]).T
H = nd.Hessian(F)([x1_start, x2_start])
H = np.linalg.inv(H)
P = -np.matmul(H, gradient)

# print("gradient=", gradient, gradient.shape, "\n")
# print("H=", H, H.shape, "\n")
# print("P=", P, P.shape, "\n")
# input()

tmp_x1 = x1_start + (alpha * P[0,0])
tmp_x2 = x2_start + (alpha * P[1,0])
tmp_y = F([tmp_x1, tmp_x2])

# Convergence condition
if abs(tmp_y - y_start) < 1e-6:
    # Finished
    print("==> Newton Method(MR-1) Algorithm Finished")

    plt.plot(x1_list, x2_list, 'o-r', ms=3)

    # Writing results in text file
    f = open("results/1A_result" + str([startPoint[0], startPoint[1]]) + ".txt", "w")
    f.write(result_string)
    f.close()

    # Showing results
    plt.tight_layout()
    plt.show() 
    exit() 

S = np.array([[tmp_x1 - x1_start, tmp_x2 - x2_start]]).T
Y = np.array([nd.Gradient(F)([tmp_x1, tmp_x2])]).T - gradient

x1_start = tmp_x1
x2_start = tmp_x2
y_start = F([x1_start, x2_start])
x1_list.append(x1_start)
x2_list.append(x2_start)
result_string += str(tmp_nIteration) + ": " + str([x1_start, x2_start]) + " = " + str(y_start) + "\n"
tmp_nIteration += 1

# iteration loop
while tmp_nIteration < 1000:
    
    gradient = np.array([nd.Gradient(F)([x1_start, x2_start])]).T
    PART1 = S-np.matmul(H,Y)
    H = H + (np.matmul(PART1, PART1.T)/np.matmul(PART1.T, Y))
    P = -np.matmul(H, gradient) 
    
    # print("gradient=", gradient, gradient.shape, "\n")
    # print("H=", H, H.shape, "\n")
    # print("P=", P, P.shape, "\n")
    # input()
    
    tmp_x1 = x1_start + alpha * P[0,0]
    tmp_x2 = x2_start + alpha * P[1,0]
    tmp_y = F([tmp_x1, tmp_x2])
 
    # Convergence condition
    if abs(tmp_y - y_start) < 1e-6:
        break
    
    S = np.array([[tmp_x1 - x1_start, tmp_x2 - x2_start]]).T
    Y = np.array([nd.Gradient(F)([tmp_x1, tmp_x2])]).T - gradient

    x1_start = tmp_x1
    x2_start = tmp_x2
    y_start = F([x1_start, x2_start])
    x1_list.append(x1_start)
    x2_list.append(x2_start)
    result_string += str(tmp_nIteration) + ": " + str([x1_start, x2_start]) + " = " + str(y_start) + "\n"
    tmp_nIteration += 1


# Finished
print("==> Newton Method(MR-1) Algorithm Finished")

plt.plot(x1_list, x2_list, 'o-r', ms=3)

# Writing results in text file
f = open("results/1A_result" + str([startPoint[0], startPoint[1]]) + ".txt", "w")
f.write(result_string)
f.close()

# Showing results
plt.tight_layout()
plt.show() 
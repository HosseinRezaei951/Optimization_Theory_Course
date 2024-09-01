# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import numdifftools as nd
np.seterr(divide='ignore', invalid='ignore')

# Implementing of F(X) function
def F(X):
    # X[0]: x1 , X[1]: x2
    return (np.power((1-X[0]),2)) + (10*(np.power((X[1]-np.power(X[0], 2)),2)))

# Creating 2D-meshgrid space for x1 and x2 dimensions 
start, stop, n_values = -6, 6, 100
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
# ==> Start trust_region (Cauchy Point Method) <==
#########################################################################################
startPoint = [5, 5]                 # start point 
y_start = F(startPoint)             # result of F(X) in start points [x1_start , x2_start]
x1_list = []
x2_list = []
x1_list.append(startPoint[0])
x2_list.append(startPoint[1])

result_string = "start point = " + str(startPoint) +\
                "\n\nresults: \n"



def cauchy_point(x, b_matrix, delta):
    g = np.array([nd.Gradient(F)(x)]).T
    gT_b_g = np.dot(np.dot(g.T, b_matrix), g)
    gT_g = np.dot(g.T, g)
    g_norm = np.linalg.norm(g, 1)  

    if gT_b_g > 0 and abs(gT_g / gT_b_g) * g_norm < delta:
        alpha = gT_g / gT_b_g
    else:
        alpha = delta / g_norm
    return -alpha * g


def approximate_model_generator(x, b_matrix):
    g = np.array([nd.Gradient(F)(x)]).T
    return lambda p: F(x) + np.dot(p.T, g) + 0.5 * np.dot(np.dot(p.T, b_matrix), p)


max_steps = 10000
rho_tolerance = 1/1e-6
delta_hat = 1.5
eta = 1 / 5
equality_tolerance = 1e-6

def trust_region(x, result_string, subproblem_solver):
    delta = delta_hat/2
    rho = rho_tolerance
    initial_x = x
    plot_y = []
    step = 0

    # Start
    print("==> Start trust_region (Cauchy Point Method) Algorithm")
    while step < max_steps and abs(rho) <= rho_tolerance:
        b_matrix = nd.Hessian(F)(x)  # use hessian matrix as Bk
        p = subproblem_solver(x, b_matrix, delta)
        approximate_model = approximate_model_generator(x, b_matrix)
        delta_f = F(x) - F(x + (p.T)[0])
        delta_m = approximate_model(np.zeros(np.shape(x)[0])) - approximate_model(p)
        rho = (delta_f / delta_m)[0][0]
        if rho < 0.25:
            delta = 0.25 * delta
        else:
            if rho > 0.75 and np.linalg.norm(p, 1) == delta:
                delta = min(2 * delta, delta_hat)

        if rho > eta:
            x = x + (p.T)[0]
            x1_list.append(x[0])
            x2_list.append(x[1])
            y_start = F(x)   
            result_string += str(step) + ": " + str(x) + " = " + str(y_start) + "\n"
        
        step += 1
        
    # Finished
    print("==> Ftrust_region (Cauchy Point Method) Algorithm Finished")
    return x, result_string

Results, result_string = trust_region(startPoint, result_string, cauchy_point)
print('Results:', Results)

plt.plot(x1_list, x2_list, 'o-r', ms=3)

# Writing results in text file
f = open("results/2(cauchy_point)_result" + str(startPoint) + ".txt", "w")
f.write(result_string)
f.close()

# Showing results
plt.tight_layout()
plt.show() 
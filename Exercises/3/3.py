import numpy as np
from autograd import grad
import numdifftools as nd
from scipy.optimize import fsolve, zeros
import warnings
warnings.filterwarnings('ignore', 'The iteration is not making good progress')

def objective(X):
    x, y = X
    return -(x * y)

def cons1(X):
    x, y = X
    return (20 * x) + (15 * y) - 30

def cons2(X):
    x, y = X
    return (0.25 * (x**2)) + (y**2) - 1

def cons3(X):
    x = X
    return x

def cons4(X):
    x = X
    return x - 3

def cons5(X):
    y = X
    return y

def cons6(X):
    y = X
    return y - 3


def F(L):
    'Augmented Lagrange function'
    x, y, _lambda1, _lambda2, _lambda3, _lambda4, _lambda5, _lambda6 = L
    return objective([x, y]) - _lambda1 * cons1([x, y]) - _lambda2 * cons2([x, y]) - _lambda3 * cons3(x) - _lambda4 * cons4(x) - _lambda5 * cons5(y) - _lambda6 * cons6(y)

# Gradients of the Lagrange function
dfdL = grad(F, 0)

# Find L that returns all zeros in this function.
def obj(L):
    x, y, _lambda1, _lambda2, _lambda3, _lambda4, _lambda5, _lambda6= L
    dFdx, dFdy, dFdlam1, dFdlam2, dFdlam3, dFdlam4, dFdlam5, dFdlam6= dfdL(L)
    return [dFdx, dFdy, cons1([x, y]), cons2([x, y]), cons3(x), cons4(x), cons5(y), cons6(y)]


x, y, _lam1, _lam2, _lam3, _lam4, _lam5, _lam6 = fsolve(obj, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

result_string = f'The answer is at {x, y} \n' +\
    f'_lambda1= {_lam1} \n' +\
    f'_lambda2= {_lam2} \n' +\
    f'_lambda3= {_lam3} \n' +\
    f'_lambda4= {_lam4} \n' +\
    f'_lambda5= {_lam5} \n' +\
    f'_lambda6= {_lam6} \n'


Zero_Mat = np.full((6, 6), 0)

gradient_cons1 = np.array([nd.Gradient(cons1)([x, y])]).T 
gradient_cons2 = np.array([nd.Gradient(cons2)([x, y])]).T 
gradient_consS = np.concatenate((gradient_cons1, gradient_cons2),axis=1)

gradient_cons3 = np.array([nd.Gradient(cons3)([x])]).T 
gradient_cons3 = np.concatenate(([gradient_cons3], [[0]]))

gradient_consS = np.concatenate((gradient_consS, gradient_cons3),axis=1)

gradient_cons4 = np.array([nd.Gradient(cons4)([x])]).T 
gradient_cons4 = np.concatenate(([gradient_cons4], [[0]]))
gradient_consS = np.concatenate((gradient_consS, gradient_cons4),axis=1)

gradient_cons5 = np.array([nd.Gradient(cons5)([y])]).T 
gradient_cons5 = np.concatenate(([[0]], [gradient_cons5]))
gradient_consS = np.concatenate((gradient_consS, gradient_cons5),axis=1)

gradient_cons6 = np.array([nd.Gradient(cons6)([y])]).T 
gradient_cons6 = np.concatenate(([[0]], [gradient_cons6]))
gradient_consS_Mat = np.concatenate((gradient_consS, gradient_cons6),axis=1).T

H_L_Mat = nd.Hessian(objective)([x, y])

Marginal_H_Up = np.concatenate((Zero_Mat, gradient_consS_Mat),axis=1)
Marginal_H_Down = np.concatenate((gradient_consS_Mat.T, H_L_Mat),axis=1)
Marginal_H = np.concatenate((Marginal_H_Up, Marginal_H_Down))


result_string += "\nMarginal Hessian Matris is: \n" + str(Marginal_H)
result_string += "\nMarginal Hessian Matris determinant= " + str(np.linalg.det(Marginal_H)) + "\n"



# Writing results in text file
f = open("results/3_result.txt", "w")
f.write(result_string)
f.close()

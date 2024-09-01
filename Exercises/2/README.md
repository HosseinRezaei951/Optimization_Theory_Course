# Advanced Optimization Techniques: Gradient Descent, Newton's Method, and Hybrid Approaches

## Overview

This assignment focuses on implementing and analyzing advanced optimization techniques. The primary algorithms covered include Gradient Descent, Newton's Method, and a combination of both for solving specific optimization problems. These methods are applied to carefully designed functions with visualizations to help understand their convergence and behavior.

## Project Structure

The project includes the following key Python scripts:

- **3A.py**: Contour plot visualization for a quadratic function.
- **3B.py**: Implementation of the Gradient Descent algorithm.
- **3D.py**: Implementation of Newton's Method for optimization.
- **4A.py, 4B.py, 4C.py**: Different approaches to applying Newton's Method and a combined method of Newton's and Gradient Descent.
- **3_(3D_Plot).py & 4_(3D_Plot).py**: Scripts for generating 3D plots to visualize the functions being optimized.

## Optimization Techniques and Question Details

### Question 3

This question deals with a quadratic function \( f(\mathbf{x}) = x_1^2 + 4x_2^2 - 4x_1 - 8x_2 \) and involves multiple parts:

- **3A.py**: This script generates a contour plot of the given quadratic function. Contour plots are essential in visualizing the function's level curves and identifying the minimum point visually. The global minimum can be observed in the contour plot below:

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/master/Exercises/2/results/3A_contour_plot.png)

- **3B.py**: This part applies the Gradient Descent algorithm to the quadratic function starting from different initial points. Gradient Descent iteratively updates the current point in the direction of the steepest descent, guided by the negative gradient. The script visualizes the path taken by the algorithm as it converges to the minimum. For example, the following plot shows the convergence path starting from the initial point \([2, 2]^T\):

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/2/results/3B_gradient_descen[2,%202].png)

- **3D.py**: In this part, Newton's Method is used to find the minimum of the quadratic function. Newton's Method leverages the second derivative (Hessian matrix) to account for the curvature, often leading to faster convergence compared to Gradient Descent. Below is a plot that demonstrates the convergence path when starting from the initial point \([0, 0]^T\):

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/2/results/3D_newton_method[0,%200].png)

### Question 4

This question explores a non-linear function \( f(\mathbf{x}) = -\cos(x_1)\cos(x_2)\exp[-(x_1-\pi)^2 - (x_2-\pi)^2] \) with a known global minimum at \( (\pi, \pi) \). The tasks involve applying Newton's Method, a combined Newton-Gradient Descent method, and Newton's Modified Method to solve the problem:

- **4A.py**: This script uses Newton's Method starting from an initial point \( x_0 = [0.75, -1.25]^T \). Given the non-linear nature of the function, the script examines how Newton's Method behaves when initialized away from the global minimum. The contour plot below visualizes the search path as the algorithm converges:

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/2/results/4A_newton_method[0.75,%20-1.25].png)

- **4B.py**: Newton's Method is applied again, but this time starting from \( x_0 = [0, 0]^T \). The script explores how starting from a different initial point affects convergence and whether Newton's Method successfully reaches the global minimum or gets stuck in a local minimum:

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/2/results/4B_newton_method[0,%200].png)

- **4C.py**: A hybrid approach is implemented here, where the algorithm starts with Newton's Method but switches to Gradient Descent if Newton's Method encounters issues (e.g., if the Hessian is not positive definite). This combined strategy ensures robust convergence:

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/2/results/4C_newton_method[0,%200].png)

## How to Use

### Running the Scripts

1. **Gradient Descent (Question 3B)**: 
   - Run `3B.py` to see the implementation and visualization of Gradient Descent on the quadratic function.
   - The script will show how the algorithm iteratively converges to the function's minimum from different initial points.

2. **Newton's Method (Questions 3D, 4A, 4B)**:
   - Run `3D.py` for the quadratic function and `4A.py` or `4B.py` for the non-linear function.
   - These scripts visualize how Newton's Method performs on different functions and initial points, showing the path of convergence or divergence.

3. **Combined Method (Question 4C)**:
   - Run `4C.py` to observe how the combination of Newton's Method and Gradient Descent handles the non-linear optimization problem.
   - This script is particularly useful for understanding the robustness of hybrid optimization strategies, especially when Newton's Method alone is insufficient.

## Conclusion

This assignment provides a practical exploration of advanced optimization techniques, demonstrating their application through Python scripts. The visualizations help in understanding the strengths and limitations of each method, particularly in how they converge to the function's minimum. Use these scripts to further explore the behavior of these algorithms and their applications in optimization problems.

Feel free to modify the scripts to experiment with different initial points, learning rates, or even different functions to deepen your understanding of optimization theory.

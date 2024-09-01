# Advanced Optimization Techniques Assignment

## Overview

This assignment explores various advanced optimization techniques, focusing on methods such as quasi-Newton methods (MR-1, DFP, BFGS), the Fletcher-Reeves gradient method, trust-region methods (Cauchy Point and Dog Leg), and constrained optimization using KKT conditions. The assignment also includes a practical implementation of linear and Ridge regression, emphasizing the optimization aspects of these models.

## Project Structure

The project is structured into the following Python scripts, each addressing specific parts of the assignment:

- **Sub-directory: results**
  - Contains the results of each algorithm in the form of `.png`, `.txt`, and `.html` files for visualizations and textual output.

- **1A.py**: Implementation of the MR-1 quasi-Newton method.
- **1B.py**: Implementation of the DFP quasi-Newton method.
- **1C.py**: Implementation of the BFGS quasi-Newton method.
- **1D.py**: Implementation of the Fletcher-Reeves gradient method.
- **1_(3D_Plot).py**: 3D visualization of the function from question 1.
- **2(cauchy_point).py**: Implementation of the trust-region method using the Cauchy Point.
- **2(dog_leg).py**: Implementation of the trust-region method using the Dog Leg method.
- **2_(3D_Plot).py**: 3D visualization of the function from question 2.
- **3.py**: Constrained optimization using KKT conditions.
- **3B.py**: Implementation of Gradient Descent for question 3.
- **4.py**: Implementation of linear and Ridge regression.

## Assignment Breakdown

### Question 1: Quasi-Newton Methods and Gradient Method

In this question, we apply various quasi-Newton methods and the Fletcher-Reeves gradient method to minimize the function \( f(\mathbit{x}) = 10x_1^2 + x_2^2 \).

#### 1A: MR-1 Quasi-Newton Method

- **Algorithm**: MR-1 (Modified Rank-1) updates the Hessian matrix iteratively to find the minimum of the function.
- **Starting Point**: \( \mathbit{x}_0 = [0.1, 1]^T \).
- **Results**: The path of convergence is plotted, showing how the method progresses towards the minimum.

Example result visualization:

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/3/results/1A_result%5B0.1,%201%5D.png)

#### 1B: DFP Quasi-Newton Method

- **Algorithm**: DFP (Davidon-Fletcher-Powell) method, another quasi-Newton method, updates the inverse Hessian matrix.
- **Starting Point**: \( \mathbit{x}_0 = [0.1, 1]^T \).
- **Results**: The contour plot and convergence path are visualized.

Example result visualization:

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/3/results/1B_result%5B0.1,%201%5D.png)

#### 1C: BFGS Quasi-Newton Method

- **Algorithm**: BFGS (Broyden-Fletcher-Goldfarb-Shanno) method is a widely used quasi-Newton method that updates the Hessian matrix.
- **Starting Point**: \( \mathbit{x}_0 = [0.1, 1]^T \).
- **Results**: Visualizes the BFGS method's convergence.

Example result visualization:

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/3/results/1C_result%5B0.1,%201%5D.png)

#### 1D: Fletcher-Reeves Gradient Method

- **Algorithm**: The Fletcher-Reeves method is a type of conjugate gradient method that adjusts the search direction to find the minimum efficiently.
- **Starting Point**: \( \mathbit{x}_0 = [0.1, 1]^T \).
- **Results**: The method's convergence path is plotted and analyzed.

Example result visualization:

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/3/results/1D_result%5B0.1,%201%5D.png)

#### 3D Plot Visualization

- **Script**: `1_(3D_Plot).py`
- **Purpose**: Provides a 3D visualization of the function \( f(\mathbit{x}) = 10x_1^2 + x_2^2 \).
  
Example 3D plot:
![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/3/results/1_(3D_Plot).png)

### Question 2: Trust-Region Methods

This question explores the application of trust-region methods, particularly the Cauchy Point and Dog Leg methods, to solve the Rosenbrock function optimization problem \( f(x, y) = (1-x)^2 + 10(y-x^2)^2 \).

#### Cauchy Point Method

- **Algorithm**: This method finds an approximate solution to the trust-region subproblem by calculating a point on the boundary of the trust region in the direction of the steepest descent.
- **Starting Point**: \( \mathbit{x}_0 = [5, 5]^T \).
- **Results**: Visualization of the method's convergence.

Example result visualization:

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/3/results/2(cauchy_point).png)

#### Dog Leg Method

- **Algorithm**: The Dog Leg method combines the steepest descent and quasi-Newton directions to find an optimal point within the trust region.
- **Starting Point**: \( \mathbit{x}_0 = [5, 5]^T \).
- **Results**: Shows how the method navigates through the search space.

Example result visualization:

![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/3/results/2(dog_leg).png)

#### 3D Plot Visualization

- **Script**: `2_(3D_Plot).py`
- **Purpose**: 3D visualization of the Rosenbrock function for better understanding of the optimization landscape.

Example 3D plot:
![alt text](https://github.com/HosseinRezaei951/Optimization_Theory_Course/blob/main/Exercises/3/results/2_(3D_Plot).png)

### Question 3: Constrained Optimization Using KKT Conditions

In this question, we apply the Karush-Kuhn-Tucker (KKT) conditions to find the optimum of the function \( f = -xy \) under several constraints.

- **Script**: `3.py`
- **Objective**: Solve the constrained optimization problem and verify the results using the KKT conditions.
- **Results**: The results include the optimal point and the evaluation of the Marginal Hessian matrix for second-order conditions.

### Question 4: Linear and Ridge Regression

This question involves implementing linear regression and Ridge regression, highlighting the optimization aspect of fitting the models.

- **Script**: `4.py`
- **Objective**: Implement linear regression and Ridge regression and compare the error metrics of both methods.
- **Results**: The results include the error calculations for both methods, demonstrating the impact of the Ridge penalty on model fitting.

## How to Use

### Running the Scripts

1. **Quasi-Newton Methods and Gradient Method (Question 1)**:
   - Run `1A.py`, `1B.py`, `1C.py`, or `1D.py` depending on the method you want to execute.
   - The script will output a contour plot showing the path of the optimization algorithm.

2. **Trust-Region Methods (Question 2)**:
   - Run `2(cauchy_point).py` or `2(dog_leg).py` to observe how the methods perform on the Rosenbrock function.
   - The results will be visualized in a contour plot.

3. **Constrained Optimization (Question 3)**:
   - Run `3.py` to solve the optimization problem using KKT conditions.

4. **Linear and Ridge Regression (Question 4)**:
   - Run `4.py` to fit a linear model to the data and observe the effect of Ridge regression.

## Conclusion

This assignment provides a deep dive into advanced optimization techniques, with practical implementations and visualizations to understand each method's strengths and limitations. The scripts and visual outputs help in analyzing how these optimization methods work and their applications in different scenarios.

Feel free to experiment with the code by changing parameters or initial points to explore the behavior of these algorithms further.
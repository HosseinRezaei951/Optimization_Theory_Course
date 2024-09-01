# Optimization Theory Course

Welcome to the Optimization Theory Course repository. This collection of assignments covers a range of advanced optimization techniques, including matrix operations, orthogonalization methods, gradient descent, Newton's methods, quasi-Newton methods, trust-region methods, and regression techniques. The course materials include Python scripts and data files for hands-on practice and analysis.

## Directory Structure

### Exercises

The `Exercises` directory contains three subdirectories, each focusing on different optimization and matrix operation topics.

#### Exercise 1: Matrix Operations and Orthogonalization

This exercise delves into fundamental matrix operations and orthogonalization techniques:

- **Data Directory**:
  - **mat1.txt**, **mat2.txt**: Sample matrices for various operations.
  - **V1.txt**, **V2.txt**: Matrices used for the Gram-Schmidt process.

- **Scripts**:
  - **GramSchmidt.py**: Implements the Gram-Schmidt orthogonalization process.
  - **Kronecker_KhatriRao_Hadamard.py**: Performs Hadamard, Kronecker, and Khatri-Rao products.
  - **Random_Matrix_Generator.py**: Generates random matrices with specified dimensions and value ranges.

#### Exercise 2: Gradient Descent and Newton's Method

This exercise explores advanced optimization techniques, including Gradient Descent and Newton's Method, with a focus on visualizations and convergence behavior:

- **Scripts**:
  - **3A.py**: Generates a contour plot for a quadratic function.
  - **3B.py**: Implements Gradient Descent with visualizations of convergence paths.
  - **3D.py**: Applies Newton's Method and visualizes its convergence.
  - **4A.py, 4B.py, 4C.py**: Various approaches to applying Newton's Method and hybrid strategies combining Newton's and Gradient Descent methods.
  - **3_(3D_Plot).py & 4_(3D_Plot).py**: Scripts for generating 3D plots of the functions being optimized.

#### Exercise 3: Quasi-Newton Methods and Trust-Region Methods

This exercise involves implementing and analyzing various quasi-Newton and trust-region methods, including constrained optimization and regression techniques:

- **Scripts**:
  - **1A.py, 1B.py, 1C.py, 1D.py**: Implementations of MR-1, DFP, BFGS quasi-Newton methods, and the Fletcher-Reeves gradient method.
  - **1_(3D_Plot).py**: Provides a 3D plot for visualization.
  - **2(cauchy_point).py, 2(dog_leg).py**: Trust-region methods using Cauchy Point and Dog Leg techniques.
  - **2_(3D_Plot).py**: 3D visualization of the Rosenbrock function.
  - **3.py**: Constrained optimization using KKT conditions.
  - **4.py**: Implementation of linear and Ridge regression.

## How to Use

### Running the Scripts

1. **Matrix Operations and Orthogonalization (Exercise 1)**:
   - Run `GramSchmidt.py`, `Kronecker_KhatriRao_Hadamard.py`, or `Random_Matrix_Generator.py` to perform various matrix operations and orthogonalization tasks.

2. **Gradient Descent and Newton's Method (Exercise 2)**:
   - Execute `3A.py`, `3B.py`, `3D.py`, `4A.py`, `4B.py`, or `4C.py` to explore different optimization techniques and their visualizations.
   - Use `3_(3D_Plot).py` and `4_(3D_Plot).py` for 3D plots.

3. **Quasi-Newton and Trust-Region Methods (Exercise 3)**:
   - Run `1A.py`, `1B.py`, `1C.py`, `1D.py`, `2(cauchy_point).py`, `2(dog_leg).py`, and `3.py` for various optimization methods.
   - Check `4.py` for regression implementation.

## Conclusion

This course provides a comprehensive exploration of optimization techniques and matrix operations, featuring practical Python implementations and visualizations. Use these materials to deepen your understanding of optimization theory and gain hands-on experience with different methods.

Feel free to modify the scripts and experiment with various parameters and functions to further enhance your learning experience.

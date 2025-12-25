# Import NumPy library and give it a short name 'np'
import numpy as np

# --------------------------------------------------
# 1. Creating a 1D Array
# --------------------------------------------------

# Create a 1D NumPy array
A = np.array([1, 2, 3, 4, 5])

# Print array
print("Array A:", A)

# Shape of array (number of rows and columns)
print("Shape:", A.shape)

# Number of dimensions of array
print("Dimensions:", A.ndim)

# Total number of elements
print("Size:", A.size)

# Data type of elements
print("Data Type:", A.dtype)

# Memory size of one element (in bytes)
print("Item Size:", A.itemsize)

# --------------------------------------------------
# 2. Creating 2D Arrays


# First 2D array
A1 = np.array([[1, 2, 3],
               [4, 5, 6]])

print("\nArray A1:\n", A1)

# Second 2D array
A2 = np.array([[6, 9, 3],
               [5, 2, 8]])

print("Array A2:\n", A2)

# --------------------------------------------------
# 3. Arithmetic Operations
# --------------------------------------------------

# Addition of arrays
Add = np.add(A1, A2)
print("\nAddition:\n", Add)

# Subtraction of arrays
Sub = np.subtract(A1, A2)
print("Subtraction:\n", Sub)

# Division of arrays
Div = np.divide(A1, A2)
print("Division:\n", Div)

# Multiplication of arrays
Mul = np.multiply(A1, A2)
print("Multiplication:\n", Mul)

# Modulus operation (remainder after division)
Mod = np.mod(A1, A2)
print("Modulus:\n", Mod)

# Remainder operation
Rem = np.remainder(A1, A2)
print("Remainder:\n", Rem)

# Power operation (A1 raised to power A2)
Pow = np.power(A1, A2)
print("Power:\n", Pow)

# Absolute value of array elements
Abs = np.absolute(Sub)
print("Absolute Value:\n", Abs)

# --------------------------------------------------
# 4. Mathematical Functions
# --------------------------------------------------

# Sum of all elements in A1
print("\nSum of A1:", np.sum(A1))

# Square root of elements in A1
print("Square Root of A1:\n", np.sqrt(A1))

# --------------------------------------------------
# 5. Matrix Multiplication using dot()
# --------------------------------------------------

# Create two 2x2 matrices
B1 = np.array([[1, 2],
               [3, 4]])

B2 = np.array([[1, 2],
               [3, 4]])

# Matrix multiplication
Dot_Mul = np.dot(B1, B2)
print("\nMatrix Multiplication:\n", Dot_Mul)

# --------------------------------------------------
# EXTRA EXAMPLE 1: Mean, Max, Min
# --------------------------------------------------

C = np.array([10, 20, 30, 40, 50])

# Calculate mean
print("\nMean:", np.mean(C))

# Find maximum value
print("Maximum:", np.max(C))

# Find minimum value
print("Minimum:", np.min(C))

# --------------------------------------------------
# EXTRA EXAMPLE 2: Reshape and Transpose
# --------------------------------------------------

# Create a 1D array
D = np.array([1, 2, 3, 4, 5, 6])

# Reshape array into 2x3 matrix
D_reshape = D.reshape(2, 3)
print("\nReshaped Array:\n", D_reshape)

# Transpose of matrix
D_transpose = D_reshape.T
print("Transpose:\n", D_transpose)

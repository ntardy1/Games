'''
Order of Operations
1) Make the numerical algorithm
2) Deal with output
'''

# Libraries
import os

# Variables
operationNumbers = []
operations = range(4)

# Algorithm
os.system('cls')

target = int(input('Please enter the target number: '))

givens = input('Please enter the given numbers: ').split()
givens = [int(num) for num in givens]

# Creating a 3D matrix
columns = len(givens)
for num in givens:
    operationNumbers.append([0]*len(operations))
    columns -= 1
    for given in givens:
        operationNumbers[givens.index(num)][givens.index(given)] = [0]*columns

# Filling the 3D matrix
rows = operations
columns = len(givens)
for matrix in operationNumbers:
    for row in rows:
        if (row == 0): # Addition
            matrix[row] = [givens[operationNumbers.index(matrix)] + givens[column] for column in range(columns)]
            matrix[row].remove(givens[operationNumbers.index(matrix)] + givens[operationNumbers.index(matrix)])
        elif (row == 1): # Subtraction
            matrix[row] = [givens[operationNumbers.index(matrix)] - givens[column] if givens[operationNumbers.index(matrix)] - givens[column] >= 0 else 0 for column in range(columns)]
            matrix[row].remove(0)
        elif (row == 2): # Multiplication
            matrix[row] = [givens[operationNumbers.index(matrix)] * givens[column] for column in range(columns)]
            matrix[row].remove(givens[operationNumbers.index(matrix)] * givens[operationNumbers.index(matrix)])
        elif (row == 3):
            matrix[row] = [givens[operationNumbers.index(matrix)] / givens[column] if givens[operationNumbers.index(matrix)] % givens[column] == 0 else 0 for column in range(columns)]
            matrix[row].remove(1)
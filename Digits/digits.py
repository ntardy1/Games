'''
Order of Operations
1) Make the numerical algorithm
2) Deal with output
'''

# Libraries
import os

# Variables
firstTensor = []
tempFirstTensor = []
operations = list(range(4))
result = False

# Functions
    
# Function to see if any of the remaining givens can be combined with a current number to make the target
# or if the current number is equal to the target
def check(remainingGivens, currentNumber, target):
    if (currentNumber == target):
        return True
    for given in remainingGivens:
        if (given + currentNumber == target):
            return True
        if (given - currentNumber == target):
            return True
        if (given * currentNumber == target):
            return True
        if (currentNumber != 0 and given / currentNumber == target):
            return True
    return False

# Function to remove a matrix from a tensor and check if that was the last matrix
def removeAndCheck(tensor, matrix, remainingGivens, currentNumber, target):
    tensor.remove(matrix)
    if (len(tensor) == 0):
        result = check(remainingGivens, currentNumber, target)
        return result
    return False

# Algorithm
os.system('cls')

target = int(input('Please enter the target number: '))

givens = input('Please enter the given numbers: ').split()
givens = [int(num) for num in givens]

# Creating the first tensor
columns = len(givens)
for num in givens:
    firstTensor.append([0]*(len(operations)+1))
    columns -= 1
    for operation in operations:
        firstTensor[givens.index(num)][operations.index(operation)] = [0]*columns

# Filling the first tensor
rows = operations
columns = len(givens)
for matrix in firstTensor:
    for row in rows:
        if (row == 0): # Adding a row of the other given numbers for future reference
            matrix[row] = [num for num in givens]
            matrix[row].remove(givens[firstTensor.index(matrix)])
        if (row == 1): # Addition
            matrix[row] = [givens[firstTensor.index(matrix)] + givens[column] for column in range(columns)]
            matrix[row].remove(givens[firstTensor.index(matrix)] + givens[firstTensor.index(matrix)])
        elif (row == 2): # Subtraction
            matrix[row] = [givens[firstTensor.index(matrix)] - givens[column] if givens[firstTensor.index(matrix)] - givens[column] >= 0 else 0 for column in range(columns)]
            matrix[row].remove(0)
        elif (row == 3): # Multiplication
            matrix[row] = [givens[firstTensor.index(matrix)] * givens[column] for column in range(columns)]
            matrix[row].remove(givens[firstTensor.index(matrix)] * givens[firstTensor.index(matrix)])
        elif (row == 4): # Division
            matrix[row] = [givens[firstTensor.index(matrix)] / givens[column] if givens[firstTensor.index(matrix)] % givens[column] == 0 else 0 for column in range(columns)]
            matrix[row].remove(1)

tempFirstTensor = list(firstTensor) # Creating a tensor that will be iteratively modified
tempGivens_1 = list(givens) # Creating a list of the givens that will be iteratively modified

# Testing all first-step operations
columns = len(givens)
for matrix_1 in firstTensor: # Iterating through to get the first number (that is the result of a previous operation)
    columns -= 1
    tempGivens_1 = list(givens)
    tempFirstTensor = list(firstTensor)
    tempFirstTensor.remove(matrix_1) # Removing the current matrix
    tempGivens_1.remove(tempGivens_1[firstTensor.index(matrix_1)]) # Removing the first number used from tempGivens_1
    for operation in operations: # Going through each row of the current matrix_1
        for column in range(columns): # Going through each column of the current matrix_1
            firstNumberUsed = givens[firstTensor.index(matrix_1)] # Keeping track of the first number used for the first operation
            secondNumberUsed = matrix_1[0][column] # Keeping track of the second number used for the first operation
            tempGivens_1.remove(secondNumberUsed)
            firstNumber = matrix_1[operation][column] # +1 because the first row is just the givens
            result = check(tempGivens_1, firstNumber, target)
            if (result):
                break
            for matrix_2 in tempFirstTensor: # Removing the matrix that corresponds to the second number used
                tempFirstTensor.remove(matrix_2) if all(secondNumberUsed != num for num in matrix_2[0]) else None
                break
            tempGivens_1.insert(column, secondNumberUsed) # Replacing the second number used
            tempFirstTensor.insert(tempGivens_1.index(secondNumberUsed), matrix_2) # Replacing the matrix corresponding to the second number used
        if (result):
            break
    if (result):
        break

if (result):
    print('Success')
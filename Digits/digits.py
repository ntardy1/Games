'''
Order of Operations
1) Make the numerical algorithm
2) Deal with output
'''

# Libraries
import os

# Variables
numbers = list(range(6))
operations = list(range(4))
firstTensor = []
tempFirstTensor = []
result = False
newGivens = []

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

# Function to create a tensor
def createTensor(givens, operations, tensor):
    tempOperations = list(operations)
    tempOperations.append(tempOperations[len(tempOperations) - 1]+1)
    columns = len(givens) - 1
    for num in givens:
        tensor.append([0]*(len(tempOperations)))
        for operation in tempOperations:
            tensor[givens.index(num)][tempOperations.index(operation)] = [0]*columns
    return tensor

# Function to fill a tensor
def fillTensor(tensor, givens, operations):
    rows = list(operations)
    rows.append(4)
    columns = len(givens)
    for matrix in tensor:
        for row in rows:
            if (row == 0): # Adding a row of the other given numbers for future reference
                matrix[row] = [num for num in givens]
                matrix[row].remove(givens[tensor.index(matrix)])
            if (row == 1): # Addition
                matrix[row] = [givens[tensor.index(matrix)] + givens[column] for column in range(columns)]
                matrix[row].remove(givens[tensor.index(matrix)] + givens[tensor.index(matrix)])
            elif (row == 2): # Subtraction
                matrix[row] = [givens[tensor.index(matrix)] - givens[column] if givens[tensor.index(matrix)] - givens[column] >= 0 else 0 for column in range(columns)]
                matrix[row].remove(0)
            elif (row == 3): # Multiplication
                matrix[row] = [givens[tensor.index(matrix)] * givens[column] for column in range(columns)]
                matrix[row].remove(givens[tensor.index(matrix)] * givens[tensor.index(matrix)])
            elif (row == 4): # Division
                for column in range(columns-1):
                    if (givens[tensor.index(matrix)] % givens[column] == 0 and givens[column] != 0):
                        matrix[row][column] = givens[tensor.index(matrix)] / givens[column]
                    else:
                        matrix[row][column] = 0
                matrix[row].remove(1) if any(num == 1 for num in matrix[row]) else None
    return tensor

# Algorithm
os.system('cls')

target = int(input('Please enter the target number: '))

givens = input('Please enter the given numbers: ').split()
givens = [int(num) for num in givens]

# Creating the first tensor
firstTensor = createTensor(givens, operations, [])

# Filling the first tensor
firstTensor = fillTensor(firstTensor, givens, operations)

tempFirstTensor = list(firstTensor) # Creating a tensor that will be iteratively modified
tempGivens_1 = list(givens) # Creating a list of the givens that will be iteratively modified

# Testing all first-step operations
columns = len(givens)
for matrix_1 in firstTensor: # Iterating through to get the first number (that is the result of a previous operation)
    columns -= 1

# Obtaining (and testing) a first-step operation
for matrix_1 in firstTensor: # Iterating through to get the first number (that is the result of a previous operation)
    columns_1 = len(givens) - 1
    tempGivens_1 = list(givens)
    tempFirstTensor = list(firstTensor)
    tempFirstTensor.remove(matrix_1) # Removing the current matrix
    tempGivens_1.remove(tempGivens_1[firstTensor.index(matrix_1)]) # Removing the first number used from tempGivens_1
    for operation in operations: # Going through each row of the current matrix_1
        for column in list(range(columns_1)): # Going through each column of the current matrix_1
            newGivens = [] # Resetting the newGivens list
            firstNumberUsed = givens[firstTensor.index(matrix_1)] # Keeping track of the first number used for the first operation
            secondNumberUsed = matrix_1[0][column] # Keeping track of the second number used for the first operation
            tempGivens_1.remove(secondNumberUsed)
            firstNumber = matrix_1[operation+1][column] # +1 because the first row is just the givens
            newGivens.append(firstNumber) # Adding the first number (from computations) to the newGivens list
            result = check(tempGivens_1, firstNumber, target) # Essentially checking if the puzzle is two-operation solvable
            if (result):
                break
            for matrix_2 in tempFirstTensor: # Removing the matrix that corresponds to the second number used
                if all(secondNumberUsed != num for num in matrix_2[0]):
                    tempFirstTensor.remove(matrix_2)
                    break
            # Obtaining a second step operation
            for matrix_3 in tempFirstTensor: # Iterating through to get the second number (that is the result of a previous operation)
                columns_2 = len(givens) - 1
                tempGivens_2 = list(tempGivens_1)
                tempSecondTensor = list(tempFirstTensor)
                tempSecondTensor.remove(matrix_3)
                tempGivens_2.remove(tempGivens_2[tempFirstTensor.index(matrix_3)])
                for operation_2 in operations: # Going through each row of the current matrix_3
                    for column_2 in list(range(columns_2)): # Going through each column of the current matrix_3
                        firstNumberUsed_1 = tempGivens_1[tempFirstTensor.index(matrix_3)] # Keeping track of the first number used in the second operation
                        if any(givens[column_2] == num for num in tempGivens_1):
                            secondNumberUsed_1 = matrix_3[0][column_2] # Keeping track of the second number used in the second operation
                        else:
                            continue
                        tempGivens_2.remove(secondNumberUsed_1)
                        secondNumber = matrix_3[operation_2+1][column_2] # +1 because the first row is just the givens
                        newGivens.append(secondNumber)
                        for matrix_4 in tempSecondTensor: # Removing the matrix that corresponds to the second number used
                            if all(secondNumberUsed_1 != num for num in matrix_4[0]):
                                tempSecondTensor.remove(matrix_4)
                                break
                        # Obtaining a third step operation
                        for matrix_5 in tempSecondTensor: # Iterating through to get the second number (that is the result of a previous operation)
                            columns_3 = len(givens) - 1
                            tempGivens_3 = list(tempGivens_2)
                            tempThirdTensor = list(tempSecondTensor)
                            tempThirdTensor.remove(matrix_5)
                            tempGivens_3.remove(tempGivens_2[tempSecondTensor.index(matrix_5)])
                            for operation_3 in operations: # Going through each row of the current matrix_5
                                for column_3 in list(range(columns_3)): # Going through each column of the current matrix_5
                                    firstNumberUsed_2 = tempGivens_2[tempSecondTensor.index(matrix_5)]
                                    secondNumberUsed_2 = tempGivens_3[0] # Keeping track of the second number used in the third operation
                                    tempGivens_3.remove(secondNumberUsed_2)
                                    thirdNumber = matrix_5[operation_2+1][column_3] # +1 because the first row is just the givens
                                    newGivens.append(thirdNumber)
                                    for matrix_6 in tempThirdTensor: # Removing the matrix that corresponds to the second number used
                                        if all(secondNumberUsed_2 != num for num in matrix_6[0]):
                                            tempThirdTensor.remove(matrix_6)
                                            break
                                    # Performing the "second stage" of operations
                                    secondTensor = createTensor(newGivens, operations, [])
                                    print(f"New Givens: {newGivens}")
                                    secondTensor = fillTensor(secondTensor, newGivens, operations)
                                    for matrix_1_1 in secondTensor: # Iterating through each number in the newGivens list
                                        columns_1_1 = len(newGivens) - 1
                                        tempNewGivens = list(newGivens)
                                        tempFirstTensor_1 = list(secondTensor)
                                        tempFirstTensor_1.remove(matrix_1_1) # Removing the current matrix
                                        tempNewGivens.remove(tempNewGivens[secondTensor.index(matrix_1_1)]) # Removing the first number used from tempNewGivens
                                        for operation in operations: # Going through each row of the current matrix_1_1
                                            for column_1_1 in list(range(columns_1_1)): # Going through each column of the current matrix_1_1
                                                newGivens_1 = [] # Resetting the newGivens_1 list
                                                firstNumberUsed_1_1 = newGivens[secondTensor.index(matrix_1_1)] # Keeping track of the first number used for the first operation of the second stage
                                                secondNumberUsed_1_1 = matrix_1_1[0][column_1_1] # Keepging track of the second number used in the first operation of the second stage
                                                tempNewGivens.remove(secondNumberUsed_1_1)
                                                firstNumber_1 = matrix_1_1[operation+1][column_1_1] # +1 because the first row is just givens
                                                newGivens_1.append(firstNumber_1)
                                                result = check(tempNewGivens, firstNumber_1, target)
                                                if (result):
                                                    break
                                                tempNewGivens.insert(column_1_1, secondNumberUsed_1_1)
                                            if (result):
                                                break
                                        if (result):
                                            break
                                    if (result):
                                        break
                                    tempGivens_3.insert(tempSecondTensor.index(matrix_5), secondNumberUsed_2)
                                    tempThirdTensor.insert(tempGivens_3.index(secondNumberUsed_2), matrix_6)
                                    newGivens.remove(thirdNumber)
                                if (result):
                                    break
                            if (result):
                                break
                        if (result):
                            break
                        newGivens.remove(secondNumber)
                        tempGivens_2.insert(tempFirstTensor.index(matrix_3), secondNumberUsed_1)
                        tempSecondTensor.insert(tempGivens_2.index(secondNumberUsed_1), matrix_4)
                    if (result):
                        break
                if (result):
                    break
            if (result):
                break
            newGivens.remove(firstNumber)
            tempGivens_1.insert(column, secondNumberUsed) # Replacing the second number used
            tempFirstTensor.insert(tempGivens_1.index(secondNumberUsed), matrix_2) # Replacing the matrix corresponding to the second number used
        if (result):
            break
    if (result):
        break

if (result):
    print('Success')
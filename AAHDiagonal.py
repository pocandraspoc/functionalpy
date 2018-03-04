import sys
import numpy as np


Matrix = np.random.randint(0,10,49).reshape(7,7)

def sumMainDiag(inputMatrix):
	sumMainDiag = 0
	rowsNum = inputMatrix.shape[0]
	for rows in range(rowsNum):
		sumMainDiag = sumMainDiag + inputMatrix[rows][rows]
	return sumMainDiag

def sumSideDiag(inputMatrix):
	sumSideDiag = 0
	rowsNum = inputMatrix.shape[0]
	colsNum = inputMatrix.shape[1]
	for rows in range(rowsNum):
		sumSideDiag = sumSideDiag + inputMatrix[rows][colsNum-rows-1]
	return sumSideDiag

def myRes(self):
	sMainDiag = sumMainDiag(Matrix)
	sSideDiag = sumSideDiag(Matrix)
	result = abs((sMainDiag-sSideDiag))
	return result

print(Matrix)
print(sumMainDiag(Matrix))
print(sumSideDiag(Matrix))
print(Matrix[4][4])
print("The result is: ", myRes(Matrix))
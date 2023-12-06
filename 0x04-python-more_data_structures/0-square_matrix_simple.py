#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    reponse = [[0] * len(row) for row in matrix]
    for i in range(len(matrix)):
       for j in range(len(matrix[i])):
         reponse[i][j] = matrix[i][j] ** 2
    return reponse
   

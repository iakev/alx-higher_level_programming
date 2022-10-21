#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix 'matrix'
    with a divisor 'div'
    """

    new_matrix = matrix[:]
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of "
                "integers/floats")
            new_matrix[i][j] = round((matrix[i][j]/div),2)
    return new_matrix

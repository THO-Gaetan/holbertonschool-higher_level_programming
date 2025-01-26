#!/usr/bin/python3
"""Module containing matrix_divided function"""


def matrix_divided(matrix, div):
    """Function to return all number from matrix divided by div,
      rounded at 2 number max"""
    # if the matrix is not a list of list then raise a TypeError
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(err_msg)
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(err_msg)
    # if all the row in the matrix doesn't have the same size raise a TypeError
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # if div is not an int or a float raise a TypeError
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # div must not be 0 or else raise a ZeroDivisionError
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # return the result of num / div for each number in the matrix
    return [[round(num / div, 2) for num in row] for row in matrix]

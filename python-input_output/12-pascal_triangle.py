#!/usr/bin/python3
"""Module that defines a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
        Each inner list is a row of the triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

#!/usr/bin/python3

"""
Defines pascal_triangle function
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """

    if n <= 0:
        return list()

    triangles = []
    for line in range(0, n):
        tmp = []
        for i in range(0, line + 1):
            tmp.append(magic(line, i))
        triangles.append(tmp)
    return triangles


def magic(n, k):
    """
    Function magic
    """

    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res *= (n - i)
        res = res // (i + 1)
    return res

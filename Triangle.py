# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of the squares of two sides equals the square of the third side,
        then return 'Right'
    """

    # verify that all 3 inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # require that the input values be > 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # the sum of any two sides must be greater than the third side
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a == b and b == c:
        return 'Equilateral'
    elif (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'

# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # Right triangle tests
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right', '8,15,17 is a Right triangle')

    # Equilateral triangle tests
    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 should be Equilateral')

    # Isoceles triangle tests
    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2,2,3 should be Isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isoceles', '3,2,2 should be Isoceles')

    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isoceles', '2,3,2 should be Isoceles')

    # Scalene triangle tests
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3,4,6 should be Scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 should be Scalene')

    # Invalid input tests
    def testInvalidZeroA(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', '0,1,1 should be InvalidInput')

    def testInvalidZeroB(self):
        self.assertEqual(classifyTriangle(1, 0, 1), 'InvalidInput', '1,0,1 should be InvalidInput')

    def testInvalidZeroC(self):
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', '1,1,0 should be InvalidInput')

    def testInvalidNegativeA(self):
        self.assertEqual(classifyTriangle(-1, 2, 2), 'InvalidInput', '-1,2,2 should be InvalidInput')

    def testInvalidNegativeB(self):
        self.assertEqual(classifyTriangle(2, -1, 2), 'InvalidInput', '2,-1,2 should be InvalidInput')

    def testInvalidNegativeC(self):
        self.assertEqual(classifyTriangle(2, 2, -1), 'InvalidInput', '2,2,-1 should be InvalidInput')

    def testInvalidTooLargeA(self):
        self.assertEqual(classifyTriangle(201, 2, 2), 'InvalidInput', '201,2,2 should be InvalidInput')

    def testInvalidTooLargeB(self):
        self.assertEqual(classifyTriangle(2, 201, 2), 'InvalidInput', '2,201,2 should be InvalidInput')

    def testInvalidTooLargeC(self):
        self.assertEqual(classifyTriangle(2, 2, 201), 'InvalidInput', '2,2,201 should be InvalidInput')

    def testInvalidFloatA(self):
        self.assertEqual(classifyTriangle(2.5, 2, 2), 'InvalidInput', '2.5,2,2 should be InvalidInput')

    def testInvalidFloatB(self):
        self.assertEqual(classifyTriangle(2, 2.5, 2), 'InvalidInput', '2,2.5,2 should be InvalidInput')

    def testInvalidFloatC(self):
        self.assertEqual(classifyTriangle(2, 2, 2.5), 'InvalidInput', '2,2,2.5 should be InvalidInput')

    # Not a triangle tests
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 should be NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1,1,3 should be NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(2, 5, 2), 'NotATriangle', '2,5,2 should be NotATriangle')

    def testNotATriangleD(self):
        self.assertEqual(classifyTriangle(5, 1, 1), 'NotATriangle', '5,1,1 should be NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

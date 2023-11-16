#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        test_polynomial.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试polynomial.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/11/08     revise
# ------------------------------------------------------------------

# 导包 =============================================================
import unittest

import numpy as np

from .polynomial import polynomial, Polynomial


# ==================================================================
class TestPolynomial(unittest.TestCase):
    """
    测试polynomial.py。
    """

    # --------------------------------------------------------------------
    def setUp(self):
        """
        Hook method for setting up the test fixture before exercising it.
        """
        print("\n\n-----------------------------------------------------")

    def tearDown(self):
        """
        Hook method for deconstructing the test fixture after testing it.
        """
        print("-----------------------------------------------------")

    @classmethod
    def setUpClass(cls):
        """
        Hook method for setting up class fixture before running tests in the class.
        """
        print("\n\n=======================================================")

    @classmethod
    def tearDownClass(cls):
        """
        Hook method for deconstructing the class fixture after running all tests in the class.
        """
        print("=======================================================")

    # --------------------------------------------------------------------
    def test_polynomial(self):
        print(polynomial(2, 1))
        print(polynomial((2,), 1))
        print(polynomial((2, 2), 1))
        print(polynomial((2, 3), 1))
        self.assertEquals(1, polynomial(2, 1))
        self.assertTrue(np.array_equal(np.array([1]), polynomial((2,), 1)))
        self.assertTrue(np.array_equal(np.array([1, 1]), polynomial((2, 2), 1)))
        self.assertTrue(np.array_equal(np.array([1, 1, 1]), polynomial((2, 3, 4), 1)))

        print(polynomial(2, 1, 1))
        print(polynomial((2,), 1, 1))
        print(polynomial((2, 2), 1, 1))
        print(polynomial((2, 3), 1, 1))
        self.assertEquals(3, polynomial(2, 1, 1))
        self.assertTrue(np.array_equal(np.array([3]), polynomial((2,), 1, 1)))
        self.assertTrue(np.array_equal(np.array([3, 3]), polynomial((2, 2), 1, 1)))
        self.assertTrue(np.array_equal(np.array([3, 4]), polynomial((2, 3), 1, 1)))

        print(polynomial(3, 1, 23, 4, 5, 6, 8, 7, 8))
        print(polynomial((3,), 1, 23, 4, 5, 6, 8, 7, 8))
        print(polynomial((4, 5), 1, 23, 4, 5, 6, 8, 7, 8))
        print(polynomial((4, 5, 6, 7, 8), 1, 23, 4, 5, 6, 8, 7, 8))
        print(polynomial((3, 6, 8, 9, 10), 1, 23, 4, 5, 6, 8, 7, 8))

    # noinspection PyUnresolvedReferences
    def test_Polynomial(self):
        p1 = Polynomial(1, 2, 3, 4)

        print(p1.degree)
        print(p1.num_args)
        print(p1.a0)
        print(p1.a1)
        print(p1.a2)
        print(p1.a3)

        print(p1(3))
        print(p1((3,)))
        print(p1((4, 5)))
        print(p1((4, 5, 6, 7, 8)))
        print(p1((3, 6, 8, 9, 10)))

        print(p1.name)
        print(p1.x_interval)


if __name__ == '__main__':
    unittest.main()

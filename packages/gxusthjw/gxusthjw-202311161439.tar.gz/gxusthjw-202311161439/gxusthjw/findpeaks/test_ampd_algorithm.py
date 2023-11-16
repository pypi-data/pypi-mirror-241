#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        test_ampd_algorithm.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试ampd_algorithm.py。
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
import matplotlib.pyplot as plt

from .ampd_algorithm import ampd, ampd_wangjy


# ==================================================================
class TestAmpdAlgorithm(unittest.TestCase):
    """
    测试ampd_algorithm.py。
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
    def test_ampd_wangjy(self):
        n = 80
        x = np.linspace(0, 200, n)
        y = 2 * np.cos(2 * np.pi * 300 * x) \
            + 5 * np.sin(2 * np.pi * 100 * x) \
            + 4 * np.random.randn(n)
        plt.plot(x, y)
        px = ampd_wangjy(y)
        plt.scatter(x[px], y[px], color="red")
        plt.show()
        print(type(px))
        print(px)

    def test_ampd(self):
        n = 80
        x = np.linspace(0, 200, n)
        y = 2 * np.cos(2 * np.pi * 300 * x) \
            + 5 * np.sin(2 * np.pi * 100 * x) \
            + 4 * np.random.randn(n)
        plt.plot(x, y)
        px = ampd(y)
        plt.scatter(x[px], y[px], color="red")
        plt.show()
        print(type(px))
        print(px)


if __name__ == '__main__':
    unittest.main()

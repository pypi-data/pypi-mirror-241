#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        test_fitting_statistics.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试fitting_statistics.py。
#                   Outer Parameters: xxxxxxx
# Class List:       TestFittingStatistics -- 测试`FittingStatistics`类。
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/15     revise
# ------------------------------------------------------------------

# 导包 =============================================================
import os
import unittest
import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import ExponentialModel, GaussianModel

from .fitting_statistics import FittingStatistics


# 定义 =============================================================

class TestFittingStatistics(unittest.TestCase):
    """
    测试`FittingStatistics`类。
    """

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

    # noinspection DuplicatedCode
    def test_statistics(self):
        """
        测试统计量。
        """
        # <examples/doc_nistgauss2.py>
        this_file = os.path.abspath(os.path.dirname(__file__))
        this_path, _ = os.path.split(this_file)
        test_file = os.path.join(this_file, 'test_data/fitting_statistics/NIST_Gauss2.dat')
        print(this_file)
        print(this_path)
        print(test_file)
        dat = np.loadtxt(test_file)
        x = dat[:, 1]
        y = dat[:, 0]

        exp_mod = ExponentialModel(prefix='exp_')
        gauss1 = GaussianModel(prefix='g1_')
        gauss2 = GaussianModel(prefix='g2_')

        def index_of(arrval, value):
            """Return index of array *at or below* value."""
            if value < min(arrval):
                return 0
            return max(np.where(arrval <= value)[0])

        ix1 = index_of(x, 75)
        ix2 = index_of(x, 135)
        ix3 = index_of(x, 175)

        pars1 = exp_mod.guess(y[:ix1], x=x[:ix1])
        pars2 = gauss1.guess(y[ix1:ix2], x=x[ix1:ix2])
        pars3 = gauss2.guess(y[ix2:ix3], x=x[ix2:ix3])

        pars = pars1 + pars2 + pars3
        mod = gauss1 + gauss2 + exp_mod

        out = mod.fit(y, pars, x=x)

        print(out.fit_report(min_correl=0.5))

        plt.plot(x, y)
        plt.plot(x, out.init_fit, '--', label='initial fit')
        plt.plot(x, out.best_fit, '-', label='best fit')
        plt.legend()
        plt.show()

        fs = FittingStatistics(y, out.best_fit, out.nvarys, x)

        self.assertEqual(fs.rsquared, out.rsquared)
        print("fs.rsquared={},out.rsquared={}".format(fs.rsquared, out.rsquared))
        print("fs.r2:{}".format(fs.r2))
        self.assertEqual(fs.chisqr, out.chisqr)
        print("fs.chisqr={},out.chisqr={}".format(fs.chisqr, out.chisqr))
        self.assertEqual(fs.aic, out.aic)
        print("fs.aic={},out.aic={}".format(fs.aic, out.aic))
        self.assertEqual(fs.bic, out.bic)
        print("fs.bic={},out.bic={}".format(fs.bic, out.bic))
        self.assertEqual(fs.redchi, out.redchi)
        print("fs.redchi={},out.redchi={}".format(fs.redchi, out.redchi))


if __name__ == '__main__':
    unittest.main()

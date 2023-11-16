#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        test_smoothing_zhxyao.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试smoothing_zhxyao.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/11/03     revise
# ------------------------------------------------------------------
# 导包 =============================================================
import os
import unittest
import numpy as np
from pygxusthjw.commons import read_txt
from .smoothing_zhxyao import smoothing_zhxyao
import matplotlib.pyplot as plt


# ==================================================================
class TestSmoothingZhxyao(unittest.TestCase):
    """
    测试xxxx.py。
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

    def test_smoothing_zhxyao(self):
        this_path = os.path.abspath(os.path.dirname(__file__))
        test_data_folder = "test_data"
        test_data_path = os.path.join(this_path, test_data_folder)
        test_data_2h_name = '2h.txt'
        test_data_8h_name = '8h.txt'
        test_data_2h_file = os.path.join(test_data_path, test_data_2h_name)
        test_data_8h_file = os.path.join(test_data_path, test_data_8h_name)

        data_2h = read_txt(test_data_2h_file, sep=None, skiprows=0, cols={0: 'Angle', 1: 'Psd'},
                           encoding='UTF16', res_type='data_frame')
        print(data_2h)
        data_8h = read_txt(test_data_8h_file, sep=",", skiprows=0, cols={0: 'Angle', 1: 'Psd'},
                           encoding='GBK', res_type='data_frame')
        print(data_8h)
        print(np.array(data_2h['Psd']))
        res_dict = smoothing_zhxyao(np.array(data_2h['Psd'], dtype=np.float64),
                                    peak_width_start=100,
                                    )
        print(res_dict[1])
        print(res_dict[2])
        print(res_dict[3])
        plt.plot(np.array(data_2h['Angle']), np.array(data_2h['Psd']), label='Raw')
        plt.plot(np.array(data_2h['Angle']), res_dict[0], label='Smoothing')
        plt.show()


if __name__ == '__main__':
    unittest.main()

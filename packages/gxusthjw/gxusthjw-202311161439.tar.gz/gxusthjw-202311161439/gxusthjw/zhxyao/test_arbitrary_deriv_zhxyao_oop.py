#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        test_arbitrary_deriv_zhxyao_oop.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试arbitrary_deriv_zhxyao_oop.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/20     revise
# ------------------------------------------------------------------
# 导包 =============================================================
import os.path
import unittest

from .arbitrary_deriv_zhxyao_oop import *

from pygxusthjw.commons import read_txt


# ==================================================================


class TestArbitraryDerivZhxyaoOop(unittest.TestCase):
    """
    测试arbitrary_deriv_zhxyao_oop.py。
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

    def test_QuasiSechEnvelope(self):
        func = QuasiSechEnvelope()
        print(func.object_id)
        func2 = QuasiSechEnvelope()
        print(func2.object_id)
        func3 = QuasiSechEnvelope()
        print(func3.object_id)
        func4 = QuasiSechEnvelope()
        print(func4.object_id)

        this_file_path, _ = os.path.split(os.path.abspath(__file__))

        func.reviews(np.arange(0, 20, 0.001),
                     is_data_out=True, is_fig_out=True,
                     data_outpath=os.path.join(this_file_path, "test_out"),
                     fig_outpath=os.path.join(this_file_path, "test_out"),
                     is_print_data=True, is_plot=True, is_show_fig=True)
        func2.reviews(np.arange(0, 20, 0.001), peak_width=100,
                      is_data_out=True, is_fig_out=True,
                      data_outpath=os.path.join(this_file_path, "test_out"),
                      fig_outpath=os.path.join(this_file_path, "test_out"),
                      fig_outfile_name="a",
                      is_print_data=True, is_plot=True, is_show_fig=True)
        func3.reviews(np.arange(0, 20, 0.001), peak_width=100, peak_steepness=10,
                      is_data_out=True, is_fig_out=True,
                      data_outpath=os.path.join(this_file_path, "test_out"),
                      fig_outpath=os.path.join(this_file_path, "test_out"),
                      label_text="ddd",
                      is_print_data=True, is_plot=True, is_show_fig=True)

    def test_GeneralPeakEnvelope(self):
        func = GeneralPeakEnvelope()
        print(func.object_id)
        func2 = GeneralPeakEnvelope()
        print(func2.object_id)
        func3 = GeneralPeakEnvelope()
        print(func3.object_id)
        func4 = GeneralPeakEnvelope()
        print(func4.object_id)

        this_file_path, _ = os.path.split(os.path.abspath(__file__))

        func.reviews(np.arange(0, 20, 0.001),
                     is_data_out=True, is_fig_out=True,
                     data_outpath=os.path.join(this_file_path, "test_out"),
                     fig_outpath=os.path.join(this_file_path, "test_out"),
                     is_print_data=True, is_plot=True, is_show_fig=True)
        func2.reviews(np.arange(0, 20, 0.001), peak_width=100,
                      is_data_out=True, is_fig_out=True,
                      data_outpath=os.path.join(this_file_path, "test_out"),
                      fig_outpath=os.path.join(this_file_path, "test_out"),
                      fig_outfile_name="a",
                      is_print_data=True, is_plot=True, is_show_fig=True)
        func3.reviews(np.arange(0, 20, 0.001), peak_width=100, peak_steepness=10,
                      is_data_out=True, is_fig_out=True,
                      data_outpath=os.path.join(this_file_path, "test_out"),
                      fig_outpath=os.path.join(this_file_path, "test_out"),
                      label_text="ddd",
                      is_print_data=True, is_plot=True, is_show_fig=True)

    def test_ArbitraryOrderDerivative(self):
        this_path = os.path.abspath(os.path.dirname(__file__))
        mat_path = os.path.join(this_path, "matlab_zhxyao")
        shf1_file = os.path.join(mat_path, 'SHf1.csv')
        shf1 = read_txt(shf1_file, skiprows=0, cols={0: 'shf1'}, res_type='data_frame')
        shf1_numpy = np.array(shf1['shf1'], dtype=np.float64)
        print(shf1_numpy)

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

        r_arange = (0, 20, 0.0001)
        r_len = int((r_arange[1] - r_arange[0]) / r_arange[2]) + 1
        r_values = np.linspace(r_arange[0], r_arange[1], r_len,
                               endpoint=True, dtype=np.float64)

        deriv = ArbitraryOrderDerivative(envelope=QuasiSechEnvelope(250, 5))
        res = deriv.deriv(data_2h['Psd'], deriv_order=2, r_values=r_values,
                          is_plot=True, is_show_fig=True)

        shfd_2h_file = os.path.join(mat_path, 'SHfd_2h.csv')
        shfd_2h_data = read_txt(shfd_2h_file, skiprows=0, cols={0: 'shfd_2h'}, res_type='data_frame')
        shfd_2h_numpy = np.array(shfd_2h_data['shfd_2h'], dtype=np.float64)
        print("shfd_2h_numpy:{}".format(shfd_2h_numpy))
        print("data_2h_s[0]:{}".format(res.get_col('s')))

        plt.plot(shfd_2h_numpy)
        plt.plot(res.get_col('s'))
        plt.show()

        self.assertTrue(np.allclose(shfd_2h_numpy, res.get_col('s'), rtol=0, atol=1e-5))


if __name__ == '__main__':
    unittest.main()

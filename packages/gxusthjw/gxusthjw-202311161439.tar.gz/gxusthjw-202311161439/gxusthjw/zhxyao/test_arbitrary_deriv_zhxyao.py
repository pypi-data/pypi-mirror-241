#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        test_arbitrary_deriv_zhxyao.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试arbitrary_deriv_zhxyao.py。
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
import os
import unittest
import numpy as np
from ..commons import read_txt
import matplotlib.pyplot as plt
from .arbitrary_deriv_zhxyao import (deriv_gl_zhxyao, sech,
                                     sech_numpy, quasi_sech,
                                     quasi_sech_ifft0,
                                     quasi_sech_ifft,
                                     deriv_quasi_sech0,
                                     deriv_quasi_sech,
                                     deriv_quasi_sech0_reviews,
                                     deriv_quasi_sech_reviews)

from scipy.fft import fft, fftshift


# ==================================================================


class TestArbitraryDerivZhxyao(unittest.TestCase):
    """
    测试arbitrary_deriv_zhxyao.py。
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

    def test_deriv_gl_zhxyao(self):
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float64)
        y = np.sin(x)
        v = 2
        res = deriv_gl_zhxyao(y, v)
        print(res)
        matlab_res = np.array([0.841470984807897, -0.773644542790111,
                               -0.836003860783600, -0.129745084601981,
                               0.695800724012585, 0.881630555819423,
                               0.256893320453502, -0.604030449013122,
                               -0.909611409286218, - 0.378899834749501])
        print(matlab_res)
        self.assertTrue(np.allclose(res, matlab_res, rtol=0, atol=1e-15))

        v = 4
        res = deriv_gl_zhxyao(y, v)
        matlab_res = np.array([0.841470984807897, -2.456586512405904,
                               1.552756209604519, 0.768618094175107,
                               0.119287032432947, -0.639715976807728,
                               -0.810567067172758, -0.236186534100704,
                               0.555342809193529, 0.836292534809812])
        print(res)
        print(matlab_res)
        self.assertTrue(np.allclose(res, matlab_res, rtol=0, atol=1e-15))

        v = 8
        res = deriv_gl_zhxyao(y, v)
        matlab_res = np.array([0.841470984807897, -5.822470451637490,
                               16.427928168075514, -23.547809757909981,
                               17.029168947791149, -5.172766892312850,
                               0.942302867559928, -0.540744161812722,
                               -0.685162517776352, -0.199645614685219])
        print(res)
        print(matlab_res)
        self.assertTrue(np.allclose(res, matlab_res, rtol=0, atol=1e-12))

    def test_sech(self):
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y = np.sin(x)
        res = sech(y)
        res2 = sech_numpy(y)
        mat_sech = np.array([0.727047269818797, 0.693148436379773,
                             0.990124533179941, 0.769049102857867,
                             0.668405967924652, 0.962194282940023,
                             0.817199777488825, 0.653312278636619,
                             0.920700462711772, 0.868307805730772])
        print(res)
        print(res2)
        print(mat_sech)
        self.assertTrue(np.allclose(res, mat_sech, rtol=0, atol=1e-15))
        self.assertTrue(np.allclose(res2, mat_sech, rtol=0, atol=1e-15))
        self.assertTrue(np.allclose(res, res2))

        y = (np.sin(x) + np.cos(x) + np.tan(x)) ** 5
        res = sech(y)
        res2 = sech_numpy(y)
        mat_sech = np.array([0.000000000000000, 0.000001907091248,
                             0.668952426160539, 0.999999470665475,
                             0, 0.999959560947206, 0.000000000000000,
                             0, 0.758005217097327, 0.977507532590036])
        print(res)
        print(res2)
        print(mat_sech)
        self.assertTrue(np.allclose(res, mat_sech, rtol=0, atol=1e-15))
        self.assertTrue(np.allclose(res2, mat_sech, rtol=0, atol=1e-15))
        self.assertTrue(np.allclose(res, res2))

    def test_quasi_sech(self):
        r = np.linspace(0, 20, 200001,
                        endpoint=True, dtype=np.float64)
        qs = quasi_sech(r, 246, 2)
        _, igg1, _ = quasi_sech_ifft0(246, 2)
        _, igg2, _ = quasi_sech_ifft(246, 2)

        print(qs)
        print(igg1)
        print(igg2)

    def test_quasi_sech_ifft_zhxyao(self):
        tc1, igg1, r_values1 = quasi_sech_ifft0(246, 2)
        tc2, igg2, r_values2 = quasi_sech_ifft(246, 2)
        self.assertTrue(np.allclose(tc1, tc2, rtol=0, atol=0))
        self.assertTrue(np.allclose(igg1, igg2, rtol=0, atol=0))
        self.assertTrue(np.allclose(r_values1, r_values2, rtol=0, atol=0))

        this_path = os.path.abspath(os.path.dirname(__file__))
        mat_path = os.path.join(this_path, "matlab_zhxyao")
        data_file = os.path.join(mat_path, "Sechpf.csv")
        mat_data = read_txt(data_file, sep=',', skiprows=1,
                            cols={0: "res_246_2", 1: "res_1246_2", 2: "res_200_5"},
                            res_type='data_frame')

        res0, _, _ = quasi_sech_ifft0(246, 2)
        res1, _, _ = quasi_sech_ifft0(1246, 2)
        res2, _, _ = quasi_sech_ifft0(200, 5)

        res0_a, _, _ = quasi_sech_ifft(246, 2)
        res1_a, _, _ = quasi_sech_ifft(1246, 2)
        res2_a, _, _ = quasi_sech_ifft(200, 5)

        print(np.array(mat_data["res_246_2"]))
        print(res0)
        print(res0_a)
        self.assertTrue(np.allclose(np.array(mat_data["res_246_2"]), res0, rtol=0, atol=1e-15))
        self.assertTrue(np.allclose(np.array(mat_data["res_246_2"]), res0_a, rtol=0, atol=1e-15))
        print(len(np.array(mat_data["res_246_2"])))
        print(len(res0))
        print(len(res0_a))

        print(np.array(mat_data["res_1246_2"]))
        print(res1)
        print(res1_a)
        self.assertTrue(np.allclose(np.array(mat_data["res_1246_2"]), res1, rtol=0, atol=1e-12))
        self.assertTrue(np.allclose(np.array(mat_data["res_1246_2"]), res1_a, rtol=0, atol=1e-12))
        print(len(np.array(mat_data["res_1246_2"])))
        print(len(res1))
        print(len(res1_a))

        print(np.array(mat_data["res_200_5"]))
        print(res2)
        print(res2_a)
        self.assertTrue(np.allclose(np.array(mat_data["res_200_5"]), res2, rtol=0, atol=1e-12))
        self.assertTrue(np.allclose(np.array(mat_data["res_200_5"]), res2_a, rtol=0, atol=1e-12))
        print(len(np.array(mat_data["res_200_5"])))
        print(len(res2))
        print(len(res2_a))

    def test_deriv_quasi_sech0_zhxyao(self):
        this_path = os.path.abspath(os.path.dirname(__file__))
        mat_path = os.path.join(this_path, "matlab_zhxyao")
        shf1_file = os.path.join(mat_path, 'SHf1.csv')
        shf1 = read_txt(shf1_file, skiprows=0, cols={0: 'shf1'}, res_type='data_frame')
        shf1_numpy = np.array(shf1['shf1'], dtype=np.float64)
        print(shf1_numpy)
        x = np.linspace(1, 50, 100)
        y = np.sin(x)
        b = 300
        p = 2
        v = 2
        s = deriv_quasi_sech0(y, v, b, p)
        s1 = deriv_quasi_sech(y, v, b, p)
        print(shf1_numpy)
        print(s[0])
        print(s1[0])

        plt.plot(shf1_numpy, label='shf1_numpy')
        plt.plot(s[0], label='s[0]')
        plt.plot(s1[0], label='s1[0]')
        plt.legend(loc='best')
        plt.show()

        self.assertTrue(np.allclose(s[0], s1[0], rtol=0, atol=1e-15))
        self.assertTrue(np.allclose(shf1_numpy, s1[0], rtol=0, atol=1e-8))
        self.assertTrue(np.allclose(s[0], shf1_numpy, rtol=0, atol=1e-8))

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

        data_2h_s = deriv_quasi_sech0(data_2h['Psd'], v, 250, 5)
        data_2h_s1 = deriv_quasi_sech(data_2h['Psd'], v, 250, 5)
        data_8h_s = deriv_quasi_sech0(data_8h['Psd'], v, 250, 8)
        data_8h_s1 = deriv_quasi_sech(data_8h['Psd'], v, 250, 8)
        print(data_2h_s)
        print(data_8h_s)

        print(data_2h_s1)
        print(data_8h_s1)

        shfd_2h_file = os.path.join(mat_path, 'SHfd_2h.csv')
        shfd_2h_data = read_txt(shfd_2h_file, skiprows=0, cols={0: 'shfd_2h'}, res_type='data_frame')
        shfd_2h_numpy = np.array(shfd_2h_data['shfd_2h'], dtype=np.float64)
        print("shfd_2h_numpy:{}".format(shfd_2h_numpy))
        print("data_2h_s[0]:{}".format(data_2h_s[0]))
        print("data_2h_s1[0]:{}".format(data_2h_s1[0]))

        plt.plot(data_2h_s[0], label='data_2h_s')
        plt.plot(data_2h_s1[0], label='data_2h_s1')
        plt.plot(shfd_2h_numpy, label='shfd_2h_numpy')
        plt.legend(loc='best')
        plt.show()

        self.assertTrue(np.allclose(data_2h_s[0], data_2h_s1[0], rtol=0, atol=1e-15))
        self.assertTrue(np.allclose(shfd_2h_numpy, data_2h_s1[0], rtol=0, atol=1e-5))
        self.assertTrue(np.allclose(data_2h_s[0], shfd_2h_numpy, rtol=0, atol=1e-5))

        shfd_8h_file = os.path.join(mat_path, 'SHfd_8h.csv')
        shfd_8h_data = read_txt(shfd_8h_file, skiprows=0, cols={0: 'shfd_8h'}, res_type='data_frame')
        shfd_8h_numpy = np.array(shfd_8h_data['shfd_8h'], dtype=np.float64)
        print("shfd_8h_numpy:{}".format(shfd_8h_numpy))
        print("data_8h_s[0]:{}".format(data_8h_s[0]))
        print("data_8h_s1[0]:{}".format(data_8h_s1[0]))

        plt.plot(data_8h_s[0], label='data_8h_s')
        plt.plot(data_8h_s1[0], label='data_8h_s1')
        plt.plot(shfd_8h_numpy, label='shfd_8h_numpy')
        plt.legend(loc='best')
        plt.show()

        self.assertTrue(np.allclose(data_8h_s[0], data_8h_s1[0], rtol=0, atol=1e-15))
        self.assertTrue(np.allclose(shfd_8h_numpy, data_8h_s1[0], rtol=0, atol=1e-5))
        self.assertTrue(np.allclose(data_8h_s[0], shfd_8h_numpy, rtol=0, atol=1e-5))

    def test_deriv_quasi_sech_zhxyao_summary(self):
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

        data_outpath = os.path.join(this_path, "test_out")
        data_2h_s = deriv_quasi_sech0_reviews(data_2h['Psd'], 2,
                                              250, 5,
                                              is_data_out=True, data_outpath=data_outpath,
                                              data_outfile_name="data_2h",
                                              is_print_data=True, is_plot=True,
                                              is_fig_out=True, fig_outpath=data_outpath,
                                              is_show_fig=True, data_name="data_2h")

        data_2h_s1 = deriv_quasi_sech_reviews(data_2h['Psd'], 2,
                                              250, 5,
                                              is_data_out=True, data_outpath=data_outpath,
                                              data_outfile_name="data_2h",
                                              is_print_data=True, is_plot=True,
                                              is_fig_out=True, fig_outpath=data_outpath,
                                              is_show_fig=True, data_name="data_2hs")
        print(data_2h_s)
        print(data_2h_s1)

    def test_frequency_spectrogram(self):
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

        numpy_2h = np.array(data_2h['Psd'])
        numpy_2h_len = len(numpy_2h)
        fft_2h = np.abs(fftshift(fft(numpy_2h)))
        fft_2h = fft_2h[(numpy_2h_len // 2) + 1:]
        fft_2h = fft_2h / np.max(fft_2h)
        x = np.linspace(0, numpy_2h_len // 2, len(fft_2h), endpoint=True) / (numpy_2h_len // 2)
        plt.plot(x[:50], quasi_sech(x, 300, 1.8)[:50])
        plt.plot(x[:50], fft_2h[:50])
        plt.show()


if __name__ == '__main__':
    unittest.main()

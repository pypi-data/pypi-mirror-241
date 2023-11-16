#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        test_bruker.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 测试bruker.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/11/05     revise
# ------------------------------------------------------------------
# 导包 =============================================================
import os
import unittest
import nmrglue as ng
import nmrglue.fileio.fileiobase
from .bruker import (read_bruker_fid, read_bruker_pdata,
                     get_spectrum_from_bruker_pdata)
import matplotlib.pyplot as plt


# ==================================================================
class TestBruker(unittest.TestCase):
    """
    测试bruker.py。
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

    def test_read_bruker_fid(self):
        # --------------------------------------------------------
        this_file = __file__
        print("this file: %s" % this_file)
        this_file_path, this_file_name = os.path.split(this_file)
        print('this file name: %s' % this_file_name)
        print('this_file_path: %s' % this_file_path)
        # --------------------------------------------------------
        test_data_folder = "test_data"
        test_data_folder_path = os.path.join(this_file_path, test_data_folder)

        test_data_names = ['CP SanYuan-1# 8.5k',
                           'CP SanYuan-2# 8.5k',
                           'CP SanYuan-3# 8.5k',
                           'CP SanYuan-4# 8.5k']
        # --------------------------------------------------------
        test_data_no = 0
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        dic0, data0 = read_bruker_fid(test_data_path)
        print(len(data0))
        test_data_no = 1
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        dic1, data1 = read_bruker_fid(test_data_path)
        print(len(data1))
        test_data_no = 2
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        dic2, data2 = read_bruker_fid(test_data_path)
        print(len(data2))
        test_data_no = 3
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        dic3, data3 = read_bruker_fid(test_data_path)
        print(len(data3))
        # 画图 -----------------------------------------------------
        plt.plot(data0)
        plt.plot(data1)
        plt.plot(data2)
        plt.plot(data3)
        # plt.xlim([0, 250])
        # plt.xlabel('')
        plt.title('bruker.read_pdata vs bruker.read, note ppm axis')
        plt.show()

        # remove the digital filter, this data is from an analog spectrometer.
        # data = ng.bruker.remove_digital_filter(dic, data)

        # process the spectrum
        data1 = ng.proc_base.ls(data1, 1)  # left shift
        data1 = ng.proc_base.gm(data1, g2=1 / 2.8e3)  # To match proc data...
        data1 = ng.proc_base.zf_size(data1, 1024 * 32)  # zero fill
        data1 = ng.proc_base.fft_positive(data1)  # FT
        data1 = ng.proc_base.ps(data1, p0=93)  # phase is 180 off Bruker
        data1 = ng.proc_base.di(data1)  # discard

        udic1 = ng.bruker.guess_udic(dic1, data1)
        uc1 = ng.fileio.fileiobase.uc_from_udic(udic1)
        ppm_scale1 = uc1.ppm_scale()

        plt.plot(ppm_scale1, data1)
        # plt.xlim([0, 250])
        # plt.xlabel('')
        plt.title('bruker.read_pdata vs bruker.read, note ppm axis')
        plt.show()

    def test_read_bruker_pdata(self):
        # --------------------------------------------------------
        this_file = __file__
        print("this file: %s" % this_file)
        this_file_path, this_file_name = os.path.split(this_file)
        print('this file name: %s' % this_file_name)
        print('this_file_path: %s' % this_file_path)
        # --------------------------------------------------------

        test_data_folder = "test_data"
        test_data_folder_path = os.path.join(this_file_path, test_data_folder)

        test_data_names = ['CP SanYuan-1# 8.5k',
                           'CP SanYuan-2# 8.5k',
                           'CP SanYuan-3# 8.5k',
                           'CP SanYuan-4# 8.5k']
        # --------------------------------------------------------
        test_data_no = 0
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        dic0, data0 = read_bruker_pdata(test_data_path)
        print(len(data0))
        test_data_no = 1
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        dic1, data1 = read_bruker_pdata(test_data_path)
        print(len(data1))
        test_data_no = 2
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        dic2, data2 = read_bruker_pdata(test_data_path)
        print(len(data2))
        test_data_no = 3
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        dic3, data3 = read_bruker_pdata(test_data_path)
        print(len(data3))
        # 画图 -----------------------------------------------------
        plt.plot(data0)
        plt.plot(data1)
        plt.plot(data2)
        plt.plot(data3)
        # plt.xlim([0, 250])
        # plt.xlabel('')
        plt.title('bruker.read_pdata vs bruker.read, note ppm axis')
        plt.show()

    def test_get_spectrum_from_bruker_pdata(self):
        # --------------------------------------------------------
        this_file = __file__
        print("this file: %s" % this_file)
        this_file_path, this_file_name = os.path.split(this_file)
        print('this file name: %s' % this_file_name)
        print('this_file_path: %s' % this_file_path)
        # --------------------------------------------------------

        test_data_folder = "test_data"
        test_data_folder_path = os.path.join(this_file_path, test_data_folder)

        test_data_names = ['CP SanYuan-1# 8.5k',
                           'CP SanYuan-2# 8.5k',
                           'CP SanYuan-3# 8.5k',
                           'CP SanYuan-4# 8.5k']
        # --------------------------------------------------------
        test_data_no = 0
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        ppm_scale0, data0 = get_spectrum_from_bruker_pdata(test_data_path)

        test_data_no = 1
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        ppm_scale1, data1 = get_spectrum_from_bruker_pdata(test_data_path)

        test_data_no = 2
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        ppm_scale2, data2 = get_spectrum_from_bruker_pdata(test_data_path)

        test_data_no = 3
        test_data_path = os.path.join(test_data_folder_path, test_data_names[test_data_no])
        ppm_scale3, data3 = get_spectrum_from_bruker_pdata(test_data_path)
        # 画图 -----------------------------------------------------
        plt.plot(ppm_scale0, data0)
        plt.plot(ppm_scale1, data1)
        plt.plot(ppm_scale2, data2)
        plt.plot(ppm_scale3, data3)
        # plt.xlim([0, 250])
        plt.xlabel('Carbon 13 Chemical shift (ppm from neat TMS)')
        plt.title('bruker.read_pdata vs bruker.read, note ppm axis')
        plt.show()


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        bruker.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 用于处理bruker的NMR数据。
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
import os.path
import nmrglue as ng
import nmrglue.fileio.fileiobase


# ==================================================================

def read_bruker_fid(data_path: str):
    """
    读取bruker的fid数据。

    bruker数据的路径，不包含“1”，例如:

        "\test_data\CP SanYuan-1# 8.5k"

        "\test_data\CP SanYuan-2# 8.5k"

        "\test_data\CP SanYuan-3# 8.5k"

        "\test_data\CP SanYuan-4# 8.5k"

    :param data_path: bruker数据的路径。
    :return: (dic, data)
    """
    # "data/bruker_exp/"
    return ng.bruker.read(dir=os.path.join(data_path, "1"))


def read_bruker_pdata(data_dir, scale_data=True):
    """
    读取bruker的pdata数据（pdata数据是预处理数据,pre-procced data）。

    bruker数据的路径，不包含“1”，例如:

        "\test_data\CP SanYuan-1# 8.5k"

        "\test_data\CP SanYuan-2# 8.5k"

        "\test_data\CP SanYuan-3# 8.5k"

        "\test_data\CP SanYuan-4# 8.5k"

    :param data_dir: bruker数据的路径。
    :param scale_data: ng.bruker.read_pdata所需的参数。
    :return: (dic, data)
    """
    data_dir = os.path.join(data_dir, "1\\pdata\\1")
    return ng.bruker.read_pdata(data_dir, scale_data=scale_data)


def get_spectrum_from_bruker_pdata(data_dir, scale_data=True):
    """
    从bruker的pdata数据获取NMR谱。

    bruker数据的路径，不包含“1”，例如:

        "\test_data\CP SanYuan-1# 8.5k"

        "\test_data\CP SanYuan-2# 8.5k"

        "\test_data\CP SanYuan-3# 8.5k"

        "\test_data\CP SanYuan-4# 8.5k"

    :param data_dir: bruker数据的路径。
    :param scale_data: ng.bruker.read_pdata所需的参数。
    :return: (ppm_scale, data)
    """
    # From pre-procced data.
    dic, data = read_bruker_pdata(data_dir, scale_data=scale_data)
    udic = ng.bruker.guess_udic(dic, data)
    uc = ng.fileio.fileiobase.uc_from_udic(udic)
    ppm_scale = uc.ppm_scale()
    return ppm_scale, data


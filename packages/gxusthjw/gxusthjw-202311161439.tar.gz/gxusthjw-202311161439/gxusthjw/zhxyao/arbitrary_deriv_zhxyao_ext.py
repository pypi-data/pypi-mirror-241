#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        arbitrary_deriv_zhxyao_ext.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 对带有噪音的数据进行任意阶求导的扩展算法。
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
from typing import Tuple

import numpy as np
import numpy.typing as npt
from scipy.optimize import leastsq
from .arbitrary_deriv_zhxyao import (quasi_sech_ifft0,
                                     quasi_sech_ifft,
                                     deriv_quasi_sech0,
                                     deriv_quasi_sech,
                                     deriv_quasi_sech0_reviews,
                                     deriv_quasi_sech_reviews)
from ..commons import FittingStatistics


# ==================================================================
def deriv_quasi_sech0_with_fit_steepness(data_y: npt.ArrayLike,
                                         peak_width: float = 20,
                                         peak_steepness_init: float = 1):
    """
    基于`deriv_quasi_sech0`方法，拟合得到指定peak_width的最优peak_steepness。

    :param data_y: 原数据。
    :param peak_width: 拟双曲正割函数的参数peak_width，称为“峰宽”。
    :param peak_steepness_init: 拟双曲正割函数的参数peak_steepness的初始值。
    :return: (peak_steepness_fitted, fs.rsquared)
    """
    data_y = np.array(data_y, dtype=np.float64, copy=True)

    # 拟合peak_steepness值 ----------------------------------------
    def loss_func(peak_steepness_arg):
        smoothing_y = deriv_quasi_sech0(data_y, 0,
                                        peak_width,
                                        peak_steepness_arg)
        ret = data_y - smoothing_y
        return ret

    peak_steepness_lsq_res = leastsq(loss_func, x0=np.array([peak_steepness_init]))
    peak_steepness_fitted = (peak_steepness_lsq_res[0][0]).tolist()

    t_fitted = deriv_quasi_sech0(data_y, 0,
                                 peak_width,
                                 peak_steepness_fitted)
    # 拟合优度 ----------------------------------------
    fs = FittingStatistics(data_y, t_fitted, nvars_fitted=1)

    return peak_steepness_fitted, fs.rsquared


def deriv_quasi_sech0_search(data_y: npt.ArrayLike,
                             peak_width_range: Tuple[float, float, float] = (10, 1000, 2),
                             peak_steepness_init: float = 1):
    """
    对一定范围内的peak_width，计算其对应的最佳peak_steepness值。

    :param data_y: 原数据。
    :param peak_width_range: 峰宽范围。
    :param peak_steepness_init: 拟双曲正割函数的参数peak_steepness的初始值。
    :return:
    """
    peak_width_values = []
    peak_steepness_fitted_values = []
    fs_rsquared_values = []
    for peak_width in np.arange(*peak_width_range):
        res = deriv_quasi_sech0_with_fit_steepness(data_y,
                                                   peak_width,
                                                   peak_steepness_init)
        peak_width_values.append(peak_width)
        peak_steepness_fitted_values.append(res[0])
        fs_rsquared_values.append(res[1])

    data_dict = {'peak_width_values': peak_width_values,
                 'peak_steepness_values': peak_steepness_fitted_values,
                 'fs_rsquared_values': fs_rsquared_values}
    return data_dict

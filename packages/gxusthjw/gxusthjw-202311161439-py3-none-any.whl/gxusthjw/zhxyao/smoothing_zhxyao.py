#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        smoothing_zhxyao.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 依据‘zhxyao’的数据平滑算法。
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
from typing import Tuple, Optional

import numpy as np
import numpy.typing as npt
from scipy.optimize import leastsq

from ..commons import FittingStatistics
from .arbitrary_deriv_zhxyao import deriv_quasi_sech0


# ==================================================================

def smoothing_zhxyao(data_y: npt.NDArray[np.float64],
                     peak_width_start: float = 10,
                     peak_width_step: float = 1,
                     peak_width_iterations: int = 100,
                     init_peak_steepness: float = 1,
                     r_squared_criteria: float = 0.999,
                     min_peak_steepness_criteria: float = 0.5
                     ) -> Optional[Tuple[npt.NDArray[np.float64], float, float, float]]:
    peak_widths = [peak_width_start + i * peak_width_step for i in range(peak_width_iterations)]
    for peak_width in peak_widths:
        def loss_func(peak_steepness_arg):
            smoothing_y = deriv_quasi_sech0(data_y,
                                            0,
                                            peak_width,
                                            peak_steepness_arg)[0]
            ret = data_y - smoothing_y
            return ret

        # noinspection PyTypeChecker
        peak_steepness_lsq_res = leastsq(loss_func, init_peak_steepness)
        peak_steepness_fitted: float = (peak_steepness_lsq_res[0][0]).tolist()
        # noinspection PyTypeChecker
        data_fitted = deriv_quasi_sech0(data_y, 0,
                                        peak_width,
                                        peak_steepness_fitted)[0]
        # 拟合优度 ----------------------------------------
        fs = FittingStatistics(data_y, data_fitted, nvars_fitted=1)

        r_squared = fs.rsquared
        print("peak_width={},peak_steepness_fitted={},r2={}".format(peak_width,
                                                                    peak_steepness_fitted,
                                                                    r_squared))

        if (r_squared <= r_squared_criteria and
                peak_steepness_fitted >= min_peak_steepness_criteria):
            return data_fitted, peak_width, peak_steepness_fitted, r_squared
    return None

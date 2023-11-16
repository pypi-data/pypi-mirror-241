#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        ma_utils.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 处理ma数据的工具函数。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/11/04     revise
# ------------------------------------------------------------------
# 导包 ==============================================================
import os
from typing import Union, Tuple, Callable

import numpy as np
import numpy.typing as npt
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


# 定义 ==============================================================

# noinspection DuplicatedCode
def strain_calibrate(strain: npt.NDArray[np.float64],
                     time: Union[Tuple[float, float], None, npt.NDArray[np.float64]] = None,
                     **kwargs) -> \
        Tuple[npt.NDArray[np.float64], float, Callable[[npt.NDArray[np.float64]], npt.NDArray[np.float64]]]:
    """
    校准应变数据，并计算应变速率。

        可选关键字参数：

            1. is_data_out：指示是否输出数据。

            2. outfile_name:指定输出数据的文件名。

            3. data_outpath：指定输出数据的路径。

            4. is_print_data：指示是否打印数据。

            5. is_plot: 指示是否绘图。

            6. is_fig_out：指示是否输出绘图。

            7. fig_outfile_name：指定输出绘图的文件名称。

            8. fig_outpath：指定输出绘图的路径。

            9. is_show_fig: 指示是否显示绘图。

            10. data_name: 指定数据名。

            11. is_alignment0: 指示是否将数据对齐至0点。

    :param strain: 原始应变数据。
    :param time: 应变时间。
    :param kwargs: 其他可选关键字参数。
    :return: (校准后的应变数据，应变速率)。
    """
    # 数据准备 -------------------------------------------------------
    strain_len = len(strain)
    if time is None:
        time = np.arange(strain_len)

    if isinstance(time, tuple):
        stop = time[0]
        num = time[1]
        time = np.linspace(start=0, stop=stop, num=num, endpoint=True)
    # 数据运算 -------------------------------------------------------
    time_data = np.column_stack((time,))
    time_data = sm.add_constant(time_data)
    resrlm = sm.RLM(strain, time_data).fit()
    fit_values = resrlm.fittedvalues
    strain_rate = resrlm.params[1]

    strain_func: Callable[[npt.NDArray[np.float64]], npt.NDArray[np.float64]] = \
        lambda x: resrlm.params[0] + x * strain_rate

    if 'is_alignment0' in kwargs and kwargs['is_alignment0']:
        fit_values = fit_values - fit_values[0]
        time = time - time[0]
    # 保存数据 ------------------------------------------------------
    if 'is_data_out' in kwargs and kwargs['is_data_out']:
        data_name = "data"
        if 'data_name' in kwargs and kwargs['data_name'] is not None:
            data_name = kwargs['data_name']
        data = pd.DataFrame({'{}_time'.format(data_name): time,
                             '{}_strain'.format(data_name): fit_values})

        # 数据文件名。
        outfile_name = "{}_{}".format(data_name, strain_rate)
        if 'outfile_name' in kwargs and kwargs['outfile_name'] is not None:
            outfile_name = kwargs['outfile_name']

        # 数据输出路径。
        data_outpath = os.path.abspath(os.path.dirname(__file__))
        if 'data_outpath' in kwargs and kwargs['data_outpath'] is not None:
            data_outpath = kwargs['data_outpath']

        if not os.path.exists(data_outpath):
            os.makedirs(data_outpath, exist_ok=True)

        data_outfile = os.path.join(
            data_outpath, "{}.csv".format(outfile_name))
        data.to_csv(data_outfile, index=False)

        # print数据 ---------------------------------------
        if 'is_print_data' in kwargs and kwargs['is_print_data']:
            # 设置pandas显示所有列
            pd.set_option('display.max_columns', None)
            # 设置pandas显示所有行
            pd.set_option('display.max_rows', None)
            # 设置pandas显示所有字符
            pd.set_option('display.max_colwidth', None)
            print("data:\n{}".format(data))
        # ------------------------------------------------

    if 'is_plot' in kwargs and kwargs['is_plot']:
        # 绘图时显示中文。
        plt.rcParams['font.family'] = 'SimHei'
        plt.rcParams['axes.unicode_minus'] = False

        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111)
        ax.plot(time, strain, "o", label="Raw data")
        ax.plot(time, resrlm.fittedvalues, "g.-",
                label="RLM calibrate data")
        ax.legend(loc="best")

        if 'is_fig_out' in kwargs and kwargs['is_fig_out']:
            data_name = "data"
            if 'data_name' in kwargs:
                if kwargs['data_name'] is not None:
                    data_name = kwargs['data_name']
            fig_outfile_name = "{}_{}".format(data_name, strain_rate)

            if 'fig_outfile_name' in kwargs and kwargs['fig_outfile_name'] is not None:
                fig_outfile_name = kwargs['fig_outfile_name']

            fig_outpath = os.path.abspath(os.path.dirname(__file__))
            if 'fig_outpath' in kwargs and kwargs['fig_outpath'] is not None:
                fig_outpath = kwargs['fig_outpath']

            if not os.path.exists(fig_outpath):
                os.makedirs(fig_outpath, exist_ok=True)

            fig_outfile = os.path.join(
                fig_outpath, "{}.png".format(fig_outfile_name))
            plt.savefig(fig_outfile)

        if 'is_show_fig' in kwargs and kwargs['is_show_fig']:
            plt.show()

    return fit_values, strain_rate, strain_func

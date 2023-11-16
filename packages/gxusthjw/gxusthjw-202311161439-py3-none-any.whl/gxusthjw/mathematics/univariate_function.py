#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        univariate_function.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 定义"单变量函数对象"。
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
# 导包 ==============================================================
from abc import ABCMeta, abstractmethod
from typing import Union

from .function_object import FunctionObject
import os
import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd


# 定义 ==============================================================

class UnivariateFunction(FunctionObject, metaclass=ABCMeta):
    """
    类`UnivariateFunction`表征“单变量函数对象”。

    继承此类的子类意味着其是单变量函数对象。
    """

    @abstractmethod
    def value(self, x: Union[float, int], *args, **kwargs) -> Union[float, int]:
        """
        计算函数的值。

        :param x: 自变量。
        :param args: 可选参数。
        :param kwargs: 可选关键字参数。
        :return: 函数值。
        """
        pass

    def values(self, x: npt.ArrayLike, *args, **kwargs) -> npt.NDArray:
        """
        计算指定自变量`x`的函数值。
        要求自变量`x`为存储int型或float型数值的npt.ArrayLike对象。

        :param x: 自变量，存储int型或float型数值的npt.ArrayLike对象。
        :return: 函数的值，存储int型或float型数值的numpy.ndarray对象。
        """
        return np.array([self.value(xi) for xi in x], *args, **kwargs)

    @abstractmethod
    def values_array(self, x: npt.ArrayLike, *args, **kwargs) -> npt.NDArray:
        """
        计算指定自变量`x`的函数值。
        要求自变量`x`为存储int型或float型数值的npt.ArrayLike对象。

        :param x: 自变量，存储int型或float型数值的npt.ArrayLike对象。
        :return: 函数的值，存储int型或float型数值的numpy.ndarray对象。
        """
        pass

    def values_arange(self, start, end, step=1) -> npt.NDArray:
        """
        先利用numpy.arange(start, end, step)方法生成自变量`x`，
        然后，调用`self.values_array(x)`方法计算自变量`x`的函数值。
        注意：生成的自变量区间为：[start,end），其中，step为区间内生成自变量值的步长。

        :param start: 自变量区间的起点（包含）。
        :param end: 自变量区间的终点（不包含，但一些特殊的情况可能会包含）。
        :param step: 在自变量区间内生成自变量值的步长。
        :return: 函数的值，存储int型或float型数值的np.ndarray对象。
        """
        return self.values_array(np.arange(start, end, step))

    def values_linspace(self, start, end, num, endpoint=True) -> npt.NDArray:
        """
        先利用`numpy.linspace(start, end, num, endpoint)`方法生成自变量`x`，
        然后，调用`self.values_array(x)`方法计算自变量`x`的函数值。
        注意：自变量区间[start,end]，其中，num为区间内产生自变量值的数量，
        endpoint指定是否包含自变量区间的终点。

        :param start: 自变量区间的起点（包含）。
        :param end: 自变量区间的终点（是否包含，由endpoint指定）。
        :param num: 在自变量区间内产生自变量值的数量。
        :param endpoint: 如果为True，则包含终点值，否则不包含。
        :return: 函数的值，存储int型或float型数值的np.ndarray对象。
        """
        return self.values_array(np.linspace(start, end, num, endpoint))

    def __call__(self, x: Union[int, float, npt.ArrayLike],
                 *args, **kwargs) -> Union[int, float, npt.NDArray]:
        """
        此方法使对象调用语法可用。

        :param x: 自变量。
        :param args: 可选参数。
        :param kwargs: 可选关键字参数。
        :return: 函数值。
        """
        if isinstance(x, (int, float)):
            return self.value(x, *args, **kwargs)
        else:
            return self.values(x, *args, **kwargs)

    def reviews(self, x: npt.ArrayLike, *args, **kwargs) -> pd.DataFrame:
        """
        审阅函数。

        可选关键字参数：

            1.is_data_out: bool，指定是否输出数据。

            2.data_outfile_name: str, 指定数据输出文件的名称（不含扩展名）。

            3.data_outpath: str, 指定数据输出文件的路径。

            4.is_print_data: bool, 指定是否print数据。

            5.is_plot: bool,指定是否绘图。

            6.fig_legend_text: str, 指定绘图中legend文本。

            7.is_fig_out: bool，是否输出绘图。

            8.fig_outfile_name: str, 指定绘图输出文件的名称（不含扩展名）。

            9.fig_outpath: str, 指定绘图输出文件的路径。

            10.is_show_fig: bool，是否显示绘图。


        :param x: 自变量。
        :param args: 可选参数。
        :param kwargs: 可选关键字参数。
        """
        x = np.array(x)
        y = self.values(x, *args, **kwargs)

        data = pd.DataFrame({'x': x, 'y': y})

        # ------------------------------------------------------------------------------
        if 'is_data_out' in kwargs and kwargs['is_data_out']:
            data_outfile_name = "UnivariateFunction"
            if 'data_outfile_name' in kwargs and kwargs['data_outfile_name'] is not None:
                data_outfile_name = kwargs['data_outfile_name']

            data_outpath = os.path.abspath(os.path.dirname(__file__))
            if 'data_outpath' in kwargs and kwargs['data_outpath'] is not None:
                data_outpath = kwargs['data_outpath']

            if not os.path.exists(data_outpath):
                os.makedirs(data_outpath, exist_ok=True)

            data_outfile = os.path.join(data_outpath, "{}.csv".format(data_outfile_name))
            data.to_csv(data_outfile, index=False)
        # ------------------------------------------------------------------------------
        if 'is_print_data' in kwargs and kwargs['is_print_data']:
            print(data)
        # ------------------------------------------------------------------------------
        if 'is_plot' in kwargs and kwargs['is_plot']:
            # 绘图时显示中文。
            plt.rcParams['font.family'] = 'SimHei'
            plt.rcParams['axes.unicode_minus'] = False

            plt.figure(figsize=(8, 6))
            if 'fig_legend_text' in kwargs and kwargs['fig_legend_text'] is not None:
                fig_legend_text = kwargs['fig_legend_text']
            else:
                fig_legend_text = "Univariate Function"

            plt.plot(x, y, label=fig_legend_text)
            plt.xlabel('x')
            plt.ylabel('y')

            fig_legend_other_text = "x:[{},{}]".format(min(x), max(x))
            ax = plt.gca()
            handles, labels = ax.get_legend_handles_labels()
            handles.append(mpatches.Patch(color='none', label=fig_legend_other_text))
            plt.rc('legend', fontsize=16)
            plt.legend(loc='best', handles=handles)

            if 'is_fig_out' in kwargs and kwargs['is_fig_out']:
                fig_outfile_name = "UnivariateFunction"
                if 'fig_outfile_name' in kwargs and kwargs['fig_outfile_name'] is not None:
                    fig_outfile_name = kwargs['fig_outfile_name']

                fig_outpath = os.path.abspath(os.path.dirname(__file__))
                if 'fig_outpath' in kwargs and kwargs['fig_outpath'] is not None:
                    fig_outpath = kwargs['fig_outpath']

                if not os.path.exists(fig_outpath):
                    os.makedirs(fig_outpath, exist_ok=True)

                fig_outfile = os.path.join(fig_outpath, "{}.png".format(fig_outfile_name))
                plt.savefig(fig_outfile)

            if 'is_show_fig' in kwargs and kwargs['is_show_fig']:
                plt.show()

        return data

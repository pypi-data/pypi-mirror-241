#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        constant.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 定义"常量函数对象"。
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

from typing import Union

import numpy as np
import numpy.typing as npt

from .elementary_function import UnivariateElementaryFunction


# 定义 ==============================================================
def constant(x: Union[int, float, npt.ArrayLike],
             a0: Union[int, float]) -> Union[int, float, npt.NDArray]:
    """
    常量(constant)函数。

    :param x: 自变量，int型或float型的数值，
                    或存储int型或float型数值的npt.ArrayLike对象。
    :param a0: 函数的参数，int型或float型的数值。
    :return: 函数值，int型或float型的数值，
             或存储int型或float型数值的np.ndarray对象。
    """
    if isinstance(x, (int, float)):
        return a0
    else:
        return np.array([a0 for _ in x])


# noinspection PyUnresolvedReferences
class Constant(UnivariateElementaryFunction):
    """
    类Constant表征“常量函数”。
    """

    # noinspection PyBroadException,PyUnresolvedReferences
    def __init__(self, *args, **kwargs):
        """
        类Constant的初始化方法。

            常量函数的参数被命名为a0。

        :param args: 函数的参数,应为1元素的元组。
        """
        super(Constant, self).__init__(*args, **kwargs)
        if not hasattr(self, 'a0'):
            raise ValueError("Expected a0 parameter, but that not be found.")

    def value(self, x: Union[float, int], *args, **kwargs) -> Union[int, float]:
        """
        计算指定自变量`x`的函数值。
        要求自变量`x`为int或float型的数值。

        :param x: 自变量，int或float类型。
        :return: 函数的值，int或float类型。
        """
        return self.a0

    def values_array(self, x: npt.ArrayLike, *args, **kwargs) -> npt.NDArray:
        """
        计算指定自变量`x`的函数值。
        要求自变量`x`为存储int型或float型数值的npt.ArrayLike对象。

        :param x: 自变量，存储int型或float型数值的npt.ArrayLike对象。
        :return: 函数的值，存储int型或float型数值的np.ndarray对象。
        """
        return self.gen(len(x))

    def gen(self, num: int) -> npt.NDArray:
        """
        生成指定数量的常量值。

        :param num: 指定的数量。
        :return: 生成的函数值，存储int型或float型数值的np.ndarray对象。
        """
        return np.full(num, fill_value=self.a0)

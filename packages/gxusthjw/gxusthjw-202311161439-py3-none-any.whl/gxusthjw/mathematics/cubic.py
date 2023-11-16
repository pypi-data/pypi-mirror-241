#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        cubic.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 定义"三次函数对象"。
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
def cubic(x: Union[int, float, npt.ArrayLike],
          a0: Union[int, float],
          a1: Union[int, float],
          a2: Union[int, float],
          a3: Union[int, float]) -> Union[int, float, npt.NDArray]:
    """
    立方(cubic)函数。

    :param x: 自变量，int型或float型的数值，
             或存储int型或float型数值的npt.ArrayLike对象。
    :param a0: 函数的参数，int型或float型的数值。
    :param a1: 函数的参数，int型或float型的数值。
    :param a2: 函数的参数，int型或float型的数值。
    :param a3: 函数的参数，int型或float型的数值。
    :return: 函数值，float型的数值或存储float型数值的np.ndarray对象。
    """
    if isinstance(x, (float, int)):
        return a0 + a1 * x + a2 * x * x + a3 * x * x * x
    else:
        _x = np.array(x, copy=False)
        return a0 + a1 * _x + a2 * _x * _x + a3 * _x * _x * _x


# noinspection PyUnresolvedReferences
class Cubic(UnivariateElementaryFunction):
    """
    类`Cubic`表征“立方函数”。
    """

    def __init__(self, *args, **kwargs):
        """
        类Cubic的初始化方法。

        :param args: 函数的参数，一个float类型的长度为4的元组。
        """
        super(Cubic, self).__init__(*args, **kwargs)
        if ((not hasattr(self, 'a0')) or
                (not hasattr(self, 'a1')) or
                (not hasattr(self, 'a2')) or
                (not hasattr(self, 'a3'))):
            raise ValueError("Expected {a0, a1, a2, a3} parameter, but that not be found.")

    def value(self, x: Union[float, int], *args, **kwargs) -> Union[int, float]:
        """
        计算函数在自变量为`x`时的值。

        :param x: 自变量，float类型。
        :return: 函数的值，float类型。
        """
        return self.a0 + self.a1 * x + self.a2 * (x ** 2) + self.a3 * (x ** 3)

    def values_array(self, x: npt.ArrayLike, *args, **kwargs) -> npt.NDArray:
        """
        计算指定自变量`x`的函数值。
        要求自变量`x`为存储int型或float型数值的np.ndarray对象。

        :param x: 自变量，存储int型或float型数值的np.ndarray对象。
        :return: 函数的值，np.ndarray对象。
        """
        _x = np.array(x, copy=False)
        return self.a0 + self.a1 * _x + self.a2 * (_x ** 2) + self.a3 * (_x ** 3)

    @property
    def intercept(self) -> float:
        """
        获取函数的截距。

        :return: 函数的截距。
        """
        return self.a0

    @property
    def slope(self) -> float:
        """
        获取函数的斜率。

        :return: 函数的斜率。
        """
        return self.a1

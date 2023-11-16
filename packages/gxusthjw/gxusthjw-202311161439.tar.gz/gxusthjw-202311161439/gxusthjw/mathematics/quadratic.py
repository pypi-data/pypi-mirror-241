#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        quadratic.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 定义"二次函数对象"。
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
def quadratic(x: Union[int, float, npt.ArrayLike],
              a0: Union[int, float],
              a1: Union[int, float],
              a2: Union[int, float]) -> Union[int, float, npt.NDArray]:
    """
    二次(quadratic)函数。

    :param x: 自变量，int型或float型的数值，
             或存储int型或float型数值的npt.ArrayLike对象。
    :param a0: 函数的参数，int型或float型的数值。
    :param a1: 函数的参数，int型或float型的数值。
    :param a2: 函数的参数，int型或float型的数值。
    :return: 函数值，float型的数值或存储float型数值的np.ndarray对象。
    """
    if isinstance(x, (float, int, np.ndarray)):
        return a0 + a1 * x + a2 * x * x
    else:
        _x = np.array(x, copy=False)
        return a0 + a1 * _x + a2 * _x * _x


# noinspection PyUnresolvedReferences
class Quadratic(UnivariateElementaryFunction):
    """
    类`Quadratic`表征“二次函数”。
    """

    def __init__(self, *args, **kwargs):
        """
        类`Quadratic`的初始化方法。

        :param args: 函数的参数,应为3元素的元组。
        """
        super(Quadratic, self).__init__(*args, **kwargs)
        if (not hasattr(self, 'a0')) or (not hasattr(self, 'a1')) or (not hasattr(self, 'a2')):
            raise ValueError("Expected {a0, a1, a2} parameter, but that not be found.")

    def value(self, x: Union[float, int], *args, **kwargs) -> Union[int, float]:
        """
        计算指定自变量`x`的函数值。
        要求自变量`x`为int或float型的数值。

        :param x: 自变量，int或float类型。
        :return: 函数的值，int或float类型。
        """
        return self.a0 + self.a1 * x + self.a2 * x * x

    def values_array(self, x: npt.ArrayLike, *args, **kwargs) -> npt.NDArray:
        """
        计算指定自变量`x`的函数值。
        要求自变量`x`为存储int型或float型数值的npt.ArrayLike对象。

        :param x: 自变量，存储int型或float型数值的npt.ArrayLike对象。
        :return: 函数的值，np.ndarray对象。
        """
        _x = np.array(x, copy=False)
        return self.a0 + self.a1 * _x + self.a2 * _x * _x

    @property
    def intercept(self) -> Union[int, float]:
        """
        获取函数的截距。

        :return: 函数的截距。
        """
        return self.a0

    @property
    def slope(self) -> Union[int, float]:
        """
        获取函数的斜率。

        :return: 函数的斜率。
        """
        return self.a1

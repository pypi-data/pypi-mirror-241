#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        polynomial.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 定义"多项式函数对象"。
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
def polynomial(x: Union[int, float, npt.ArrayLike],
               *args) -> Union[int, float, npt.NDArray]:
    """
    多项式（polynomial）函数。

    :param x: 自变量，int型或float型的数值，
             或存储int型或float型数值的npt.ArrayLike对象。
    :param args: 多项式函数的参数，长度必须大于0。
    :return: 函数值，int型或float型的数值，
             或存储int型或float型数值的np.ndarray对象。
    """
    args_len = len(args)
    if args_len <= 0:
        raise ValueError("polynomial expected: len(args) > 0, "
                         "but got len(args) = {}".format(len(args)))
    degree = args_len - 1

    if isinstance(x, (int, float)):
        make_sum = args[0]
        if degree == 0:
            return make_sum
        else:
            for i in range(1, args_len):
                make_sum += args[i] * (x ** i)
        return make_sum
    else:
        _x = np.array(x, copy=False)
        make_sum = np.full(len(_x), fill_value=args[0])
        if degree == 0:
            return make_sum
        else:
            for i in range(1, args_len):
                make_sum += args[i] * (_x ** i)
        return make_sum


class Polynomial(UnivariateElementaryFunction):
    """
    类`Polynomial`表征“多项式函数”。
    """

    def __init__(self, *args, **kwargs):
        """
        类`Polynomial`的初始化方法。

        :param args: 多项式函数的参数，长度必须大于0。
        """
        super(Polynomial, self).__init__(*args, **kwargs)
        if self.num_args <= 0:
            raise ValueError("Polynomial expected: len(args) > 0, "
                             "but got len(args) = {}".format(len(args)))

        self.degree = self.num_args - 1
        self.__args = args

    def value(self, x: Union[float, int], *args, **kwargs) -> Union[int, float]:
        """
        计算函数在自变量为`x`时的值。

        :param x: 自变量，float类型。
        :return: 函数的值，float类型。
        """
        make_sum = self.__args[0]
        if self.degree == 0:
            return make_sum
        else:
            for i in range(1, self.num_args):
                make_sum += self.__args[i] * (x ** i)
        return make_sum

    def values_array(self, x: npt.ArrayLike, *args, **kwargs) -> npt.NDArray:
        """
        计算指定自变量`x`的函数值。
        要求自变量`x`为存储int型或float型数值的np.ndarray对象。

        :param x: 自变量，存储int型或float型数值的np.ndarray对象。
        :return: 函数的值，np.ndarray对象。
        """
        _x = np.array(x, copy=False)
        make_sum = np.full(len(_x), fill_value=args[0])
        if self.degree == 0:
            return make_sum
        else:
            for i in range(1, self.num_args):
                make_sum += self.__args[i] * (_x ** i)
        return make_sum

    def item(self, x: npt.ArrayLike, i: int):
        """
        获取第i项的值。

        :param x: 自变量。
        :param i: 项索引号。
        :return: 第i项的值。
        """
        _x = np.array(x, copy=False)
        return self.__args[i] * (_x ** i)

    @property
    def intercept(self) -> float:
        """
        获取函数的截距。

        :return: 函数的截距。
        """
        return self.__args[0]

    @property
    def slope(self) -> float:
        """
        获取函数的斜率。

        :return: 函数的斜率。
        """
        if self.degree >= 1:
            return self.__args[1]
        else:
            raise RuntimeError("The Polynomial is 0 degree,"
                               "so it has not slope.")

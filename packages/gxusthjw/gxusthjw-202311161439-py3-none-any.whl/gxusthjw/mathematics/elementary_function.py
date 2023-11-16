#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        elementary_function.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 定义"初等函数对象"。
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
from abc import ABCMeta

from .univariate_function import UnivariateFunction
from ..commons import Interval, IntervalRule


# 定义 ==============================================================
class UnivariateElementaryFunction(UnivariateFunction, metaclass=ABCMeta):
    """
    类`UnivariateElementaryFunction`表征“单变量初等函数对象”。
    """

    def __init__(self, *args, **kwargs):
        """
        类`UnivariateElementaryFunction`的初始化方法。

        可选关键字参数：

           1. x_interval: 指定自变量的区间，缺省为(-inf,inf)。

           2. name: 指定函数名，缺省与实现类的名称相同。

           3. 其他关键字参数，被转换为函数的属性。

        :param args: 函数的参数。
        :param kwargs: 函数的其他关键字参数。
        """
        # 函数参数的个数。
        self.num_args = len(args)

        # 构造函数参数名，依次为：a0,a1,a2,...
        for i in range(self.num_args):
            setattr(self, "a{}".format(i), args[i])

        self.x_interval = Interval(float("-inf"), float('inf'), IntervalRule.OpenOpen)
        if "x_interval" in kwargs and kwargs['x_interval'] is not None:
            if isinstance(kwargs['x_interval'], str):
                self.x_interval = Interval.from_str(kwargs['x_interval'])
            elif isinstance(kwargs['x_interval'], Interval):
                self.x_interval = kwargs['x_interval']
            else:
                raise TypeError("Expected type of kwargs['x_interval'] is str or Interval,"
                                "but got type(kwargs['x_interval'])={}.".format(type(kwargs['x_interval'])))

        self.name = self.__class__.__name__
        if "name" in kwargs:
            self.name = kwargs['name']

        for key in kwargs.keys():
            if hasattr(self, key):
                continue
            else:
                setattr(self, key, kwargs[key])

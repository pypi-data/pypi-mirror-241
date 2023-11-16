#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        fitting_statistics.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: 定义表征“拟合统计”的类。
#                   Outer Parameters: xxxxxxx
# Class List:       FittingStatistics -- 表征“拟合统计”的类。
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/15     revise
# ------------------------------------------------------------------

# 导包 ==============================================================
import numpy as np
import numpy.typing as npt

from ..commons import is_sorted_ascending, Ordering, \
    is_sorted_descending, TINY_FLOAT


# 定义 ==============================================================


class FittingStatistics(object):
    """
    类`FittingStatistics`表征“拟合统计”的类。
    """

    def __init__(self, y: npt.ArrayLike,
                 y_fitted: npt.ArrayLike,
                 nvars_fitted: int = None,
                 x: npt.ArrayLike = None,
                 **kwargs):
        """
        类`FittingStatistics`的初始化方法。

        :param y: 被拟合的y坐标数据。
        :param y_fitted: 经拟合后的y坐标数据。
        :param nvars_fitted: 拟合变量的个数。
        :param x: 被拟合的y坐标数据对应的x坐标数据，可选。
        :param kwargs: 其他可选的关键字参数。
        """
        self.__y = np.array(y, copy=True, dtype=np.float64)

        self.__len = len(self.__y)

        self.__y_fitted = np.array(y_fitted, copy=True, dtype=np.float64)
        if self.__len != len(self.__y_fitted):
            raise ValueError("Expected the len of y_fitted and y is same, "
                             "but got {{len(y_fitted) = {}, "
                             "len(y) = {}}}.".format(
                len(self.__y_fitted), self.__len)
            )

        # 拟合残差数据。
        self.__residuals = self.__y - self.__y_fitted

        # 拟合变量的个数可以不给出，不给出时为None。
        self.__nvars_fitted = nvars_fitted
        if self.__nvars_fitted is not None:
            if nvars_fitted >= self.__len:
                raise ValueError("Expected nvars_fitted < {},"
                                 " but got {}.".format(
                    self.__len, nvars_fitted)
                )
            # 自由度。
            self.__nfree = self.__len - self.__nvars_fitted
        else:
            self.__nfree = None

        if x is None:
            self.__x = np.arange(self.__len, dtype=np.int32)
        else:
            self.__x = np.array(x, copy=True)

        if self.__len != len(self.__x):
            raise ValueError("Expected the len of x and y is same, "
                             "but got {{len(x) = {},"
                             "len(y) = {}}}.".format(
                len(self.__x), self.__len)
            )

        # 判断自变量是否为有序的。
        if is_sorted_ascending(self.__x):
            self.__x_sorted_type = Ordering.ascending
        elif is_sorted_descending(self.__x):
            self.__x_sorted_type = Ordering.descending
        else:
            self.__x_sorted_type = Ordering.unordered

        self.__kwargs = kwargs

    @property
    def y(self):
        """
        获取被拟合的y坐标数据。

        :return: 被拟合的y坐标数据。
        """
        return self.__y

    @property
    def y_fitted(self):
        """
        获取经拟合后的y坐标数据。

        :return: 经拟合后的y坐标数据。
        """
        return self.__y_fitted

    @property
    def residuals(self):
        """
        获取拟合残差数据。

        :return:拟合残差数据。
        """
        return self.__residuals

    @property
    def x(self):
        """
        获取被拟合的y坐标数据对应的x坐标数据。

        :return: 被拟合的y坐标数据对应的x坐标数据
        """
        return self.__x

    @property
    def len(self):
        """
        获取数据的长度。

        :return: 数据的长度。
        """
        return self.__len

    @property
    def nvars_fitted(self):
        """
        获取拟合变量的数量。

        :return: 拟合变量的数量。
        """
        return self.__nvars_fitted

    @property
    def nfree(self):
        """
        获取自由度。

        :return: 自由度。
        """
        return self.__nfree

    @property
    def kwargs(self):
        """
        获取其他关键字参数。

        :return: 其他关键字参数。
        """
        return self.__kwargs

    # ==========================================================
    @property
    def y_mean(self):
        """
        获取被拟合的y坐标数据的均值。

        :return: 被拟合的y坐标数据的均值。
        """
        return np.mean(self.y)

    @property
    def y_fitted_mean(self):
        """
        获取经拟合后的y坐标数据的均值。

        :return: 经拟合后的y坐标数据的均值。
        """
        return np.mean(self.y_fitted)

    @property
    def residuals_mean(self):
        """
        获取拟合残差数据的均值。

        :return: 拟合残差数据的均值。
        """
        return np.mean(self.residuals)

    @property
    def __chisqr(self):
        return (self.residuals ** 2).sum()

    @property
    def chisqr(self):
        """
        获取卡方统计量（chi-square statistic）。

        :return:卡方统计量（chi-square statistic）。
        """
        return max(self.__chisqr, 1.0e-250 * self.len)

    @property
    def redchi(self):
        """
        获取简化卡方统计量（reduced chi-square statistic）。

        :return:简化卡方统计量（reduced chi-square statistic）。
        """
        if self.nfree is not None:
            return self.__chisqr / max(1, self.nfree)
        else:
            return None

    @property
    def __neg2_log_likelihood(self):
        return self.len * np.log(self.chisqr / self.len)

    @property
    def aic(self):
        """
        获取赤池信息准则统计量（Akaike information criterion statistic）。

        :return:赤池信息准则统计量（Akaike information criterion statistic）。
        """
        if self.nvars_fitted is not None:
            return self.__neg2_log_likelihood + 2 * self.nvars_fitted
        else:
            return None

    @property
    def bic(self):
        """
        获取贝叶斯信息准则统计量（Bayesian Information Criterion statistic）。

        :return:贝叶斯信息准则统计量（Bayesian Information Criterion statistic）。
        """
        if self.nvars_fitted is not None:
            return self.__neg2_log_likelihood + np.log(self.len) * self.nvars_fitted
        else:
            return None

    @property
    def tss_array(self) -> npt.NDArray[float]:
        """
        计算y数据的方差。

        :return: y数据的方差。
        """
        return np.array([np.power(yi - self.y_mean, 2.0) for yi in self.y])

    @property
    def tss(self):
        """
        计算SST(total sum of squares)， 总平方和。

        :return: 总平方和SST。
        """
        return np.sum(self.tss_array)

    @property
    def rss_array(self) -> npt.NDArray[float]:
        """
        计算拟合后y数据的方差。

        :return: 拟合后y数据的方差。
        """
        return np.array([np.power(yi - self.y_mean, 2.0) for yi in self.y_fitted])

    @property
    def rss(self):
        """
        计算SSR(regression sum of squares) ，回归平方和。

        :return: 回归平方和SSR。
        """
        return np.sum(self.rss_array)

    @property
    def ess_array(self) -> npt.NDArray[float]:
        """
        总方差数组。

        :return: 总方差数组。
        """
        return np.array([np.power(
            self.y_fitted[i] - self.y[i], 2.0) for i in range(self.len)])

    @property
    def ess(self):
        """
        计算SSE(error sum of squares) , 残差平方和。

        :return: 残差平方和SSE。
        """
        return np.sum(self.ess_array)

    @property
    def rsquared(self):
        """
        获取R^2统计量。

        :return:R^2统计量。
        """
        # noinspection PyTypeChecker
        return 1.0 - self.ess / max(TINY_FLOAT, self.tss)

    @property
    def r2(self):
        """
        获取R^2统计量。

        :return:R^2统计量。
        """
        return self.rss / self.tss
# ==========================================================

#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ------------------------------------------------------------------
# File Name:        tensile_cre.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2023/06/22
# Description:      Main Function: 定义表征‘等速伸长拉伸(CRE)数据’的类。
#                   Outer Parameters: xxxxxxx
# Class List:       TensileCre-- 表征‘等速伸长拉伸(CRE)数据’。
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2023/06/22     create
#       Jiwei Huang        0.0.1         2023/11/15     revise
# ------------------------------------------------------------------
# 导包 ==============================================================
from typing import Tuple

import numpy as np
import numpy.typing as npt

import matplotlib.pyplot as plt
import pandas as pd

from scipy import integrate

import statsmodels.api as sm


# 定义 ==============================================================

class TensileCre(object):
    """
    类`TensileCre`表征‘等速伸长拉伸(CRE)数据’。

        拉伸实验的类型：

        1.等速伸长型(Constant Rate of Elongation, Constant Rate of Elongation,CRE):
          试样在受拉过程中单位时间的`变形率`保持一定;

        2.等加负荷型(Constant Rate of Loading, CRL):试样受拉伸时的`负荷增加率`基本持一定;

        3.等速牵引型(Constant rate of Traverse, CRT):试样受下铗牵引时,上铗按材料的应力-应变特性同时有一不规则的位移。
            等速牵引型仪器出现早应用广，属于机械式类型，常称为`摆锤式强力机`。
    """

    def __init__(self,
                 displacement: npt.ArrayLike,
                 force: npt.ArrayLike,
                 time: npt.ArrayLike = None,
                 displacement_unit: str = "mm",
                 force_unit: str = "N",
                 time_unit: str = "s",
                 sample_thickness: float = 0.2,
                 sample_thickness_unit: str = "mm",
                 sample_width: float = 10,
                 sample_width_unit="mm",
                 clamping_distance: float = 20,
                 clamping_distance_unit: str = "mm",
                 pre_tension: float = 0.05,
                 pre_tension_unit: str = "N",
                 tensile_speed: float = 10,
                 tensile_speed_unit: str = "mm/min",
                 sample_name: str = "Sample",
                 sample_test_no: int = 0,
                 **kwargs):
        """
        类`TensileCre`的初始化方法。

        :param displacement: 应变量（位移）。
        :param force: 应力。
        :param time: 采样时间，若为None，则以60s为总时长进行计算。
        :param displacement_unit: 应变量的单位，可以为：'km','m','dm','cm','mm','um'。
        :param force_unit: 应力的单位，可以为：'kN','N','dN','cN','mN','uN'。
        :param time_unit: 采样时间的单位，可以为：'s','min','h'。
        :param sample_thickness: 样品厚度。
        :param sample_thickness_unit:样品厚度的单位，可以为：'km','m','dm','cm','mm','um'。
        :param sample_width: 样品宽度。
        :param sample_width_unit:样品宽度的单位，可以为：'km','m','dm','cm','mm','um'。
        :param clamping_distance: 夹持间距。
        :param clamping_distance_unit:夹持间距的单位，可以为：'km','m','dm','cm','mm','um'。
        :param pre_tension: 预加张力。
        :param pre_tension_unit: 预加张力的单位，可以为：'kN','N','dN','cN','mN','uN'。
        :param tensile_speed: 拉伸速度。
        :param tensile_speed_unit:拉伸速度的单位。可以为：
                             'km/min','m/min','dm/min','cm/min','mm/min','um/min',
                             'km/s','m/s,'dm/s','cm/s','mm/s','um/s',
                             'km/h','m/h','dm/h','cm/h','mm/h','um/h',
        :param sample_name: 样品名。
        :param sample_test_no: 样品测试编号。
        :param kwargs: 其他可选的关键字参数。
        """

        # 确保displacement_unit是字符串值。
        if not isinstance(displacement_unit, str):
            raise ValueError("Expected displacement_unit is a str.")

        # 以m为基准单位。
        if displacement_unit.lower() == "m":
            self.__displacement = np.array(displacement, copy=True, dtype='f8')
        elif displacement_unit.lower() == "mm":
            self.__displacement = np.array(displacement, copy=True, dtype='f8') * 1E-3
        elif displacement_unit.lower() == "cm":
            self.__displacement = np.array(displacement, copy=True, dtype='f8') * 1E-2
        elif displacement_unit.lower() == "dm":
            self.__displacement = np.array(displacement, copy=True, dtype='f8') * 1E-1
        elif displacement_unit.lower() == "um":
            self.__displacement = np.array(displacement, copy=True, dtype='f8') * 1E-6
        elif displacement_unit.lower() == "km":
            self.__displacement = np.array(displacement, copy=True, dtype='f8') * 1E3
        else:
            raise ValueError(
                "Expected the displacement_unit is one of {{'m','cm','mm','dm','um','km'}} case-ignored,"
                "but got {}.".format(displacement_unit))
        self.__displacement_unit = "m"

        # 确保force_unit是字符串值。
        if not isinstance(force_unit, str):
            raise ValueError("Expected force_unit is a str.")

        # 以N为基准单位。
        if force_unit.lower() == "n":
            self.__force = np.array(force, copy=True, dtype='f8')
        elif force_unit.lower() == "cn":
            self.__force = np.array(force, copy=True, dtype='f8') * 1E-2
        elif force_unit.lower() == "dn":
            self.__force = np.array(force, copy=True, dtype='f8') * 1E-1
        elif force_unit.lower() == "kn":
            self.__force = np.array(force, copy=True, dtype='f8') * 1E3
        elif force_unit.lower() == "mn":
            self.__force = np.array(force, copy=True, dtype='f8') * 1E-3
        elif force_unit.lower() == "un":
            self.__force = np.array(force, copy=True, dtype='f8') * 1E-6
        else:
            raise ValueError(
                "Expected the force_unit is one of {{'N','cN','dN','kN','mN','uN'}} case-ignored,"
                "but got {}.".format(force_unit))
        self.__force_unit = "N"

        # 确保displacement,force的长度一致。
        self.__len = len(self.__displacement)
        if len(self.__force) != self.__len:
            raise ValueError(
                "Expected len(displacement) == len(force), "
                "but got {{len(displacement)={},len(force)={}}}.".format(
                    self.__len, len(self.__force)))

        if time is None:
            self.__time = np.linspace(0, 60, self.__len)
        else:
            # 确保time_unit是字符串值。
            if not isinstance(time_unit, str):
                raise ValueError("Expected time_unit is a str.")
            # 以s为基准单位。
            if time_unit.lower() == "s":
                self.__time = np.array(time, copy=True, dtype='f8')
            elif time_unit.lower() == "min":
                self.__time = np.array(time, copy=True, dtype='f8') * 60.0
            elif time_unit.lower() == "h":
                self.__time = np.array(time, copy=True, dtype='f8') * 60.0 * 60.0
            else:
                raise ValueError(
                    "Expected the time_unit is one of {{'s','min','h'}} case-ignored,"
                    "but got {}.".format(force_unit))
        self.__time_unit = "s"

        if len(self.__time) != self.__len:
            raise ValueError(
                "Expected len(displacement) == len(time), "
                "but got {{len(displacement)={},len(time)={}}}.".format(
                    self.__len, len(self.__time)))

        # 样品名必须为字符串, 如果不是字符串，则以Sample为默认样品名。
        self.__sample_name = sample_name
        if not isinstance(self.__sample_name, str):
            self.__sample_name = "Sample"

        # 样品编号必须为整数，否则取0为缺省的样品编号。
        self.__sample_test_no = sample_test_no
        if not isinstance(self.__sample_test_no, int):
            self.__sample_test_no = 0

        # name定义为数据名。
        self.__name = "{}_{}".format(self.__sample_name, self.__sample_test_no)

        # 确保sample_thickness_unit是字符串值。
        if not isinstance(sample_thickness_unit, str):
            raise ValueError("Expected sample_thickness_unit is a str.")

        # 以m为基准单位。
        if sample_thickness_unit.lower() == "m":
            self.__sample_thickness = float(sample_thickness)
        elif sample_thickness_unit.lower() == "mm":
            self.__sample_thickness = float(sample_thickness) * 1E-3
        elif sample_thickness_unit.lower() == "cm":
            self.__sample_thickness = float(sample_thickness) * 1E-2
        elif sample_thickness_unit.lower() == "dm":
            self.__sample_thickness = float(sample_thickness) * 1E-1
        elif sample_thickness_unit.lower() == "um":
            self.__sample_thickness = float(sample_thickness) * 1E-6
        elif sample_thickness_unit.lower() == "km":
            self.__sample_thickness = float(sample_thickness) * 1E3
        else:
            raise ValueError(
                "Expected the sample_thickness_unit is one of {{'m','cm','mm','dm','um','km'}} case-ignored,"
                "but got {}.".format(sample_thickness_unit))
        self.__sample_thickness_unit = "m"

        # 确保sample_width_unit是字符串值。
        if not isinstance(sample_width_unit, str):
            raise ValueError("Expected sample_width_unit is a str.")

        # 以m为基准单位。
        if sample_width_unit.lower() == "m":
            self.__sample_width = float(sample_width)
        elif sample_width_unit.lower() == "mm":
            self.__sample_width = float(sample_width) * 1E-3
        elif sample_width_unit.lower() == "cm":
            self.__sample_width = float(sample_width) * 1E-2
        elif sample_width_unit.lower() == "dm":
            self.__sample_width = float(sample_width) * 1E-1
        elif sample_width_unit.lower() == "um":
            self.__sample_width = float(sample_width) * 1E-6
        elif sample_width_unit.lower() == "km":
            self.__sample_width = float(sample_width) * 1E3
        else:
            raise ValueError(
                "Expected the sample_width_unit is one of {{'m','cm','mm','dm','um','km'}} case-ignored,"
                "but got {}.".format(sample_width_unit))
        self.__sample_width_unit = "m"

        # 确保clamping_distance_unit是字符串值。
        if not isinstance(clamping_distance_unit, str):
            raise ValueError("Expected clamping_distance_unit is a str.")

        if clamping_distance_unit.lower() == "m":
            self.__clamping_distance = float(clamping_distance)
        elif clamping_distance_unit.lower() == "mm":
            self.__clamping_distance = float(clamping_distance) * 1E-3
        elif clamping_distance_unit.lower() == "cm":
            self.__clamping_distance = float(clamping_distance) * 1E-2
        elif clamping_distance_unit.lower() == "dm":
            self.__clamping_distance = float(clamping_distance) * 1E-1
        elif clamping_distance_unit.lower() == "um":
            self.__clamping_distance = float(clamping_distance) * 1E-6
        elif clamping_distance_unit.lower() == "km":
            self.__clamping_distance = float(clamping_distance) * 1E3
        else:
            raise ValueError(
                "Expected the clamping_distance_unit is one of {{'m','cm','mm','dm','um','km'}} case-ignored,"
                "but got {}.".format(clamping_distance_unit))
        self.__clamping_distance_unit = "m"

        # 确保pre_tension_unit是字符串值。
        if not isinstance(pre_tension_unit, str):
            raise ValueError("Expected pre_tension_unit is a str.")

        # 以N为基准单位。
        if pre_tension_unit.lower() == "n":
            self.__pre_tension = float(pre_tension)
        elif pre_tension_unit.lower() == "cn":
            self.__pre_tension = float(pre_tension) * 1E-2
        elif pre_tension_unit.lower() == "dn":
            self.__pre_tension = float(pre_tension) * 1E-1
        elif pre_tension_unit.lower() == "kn":
            self.__pre_tension = float(pre_tension) * 1E3
        elif pre_tension_unit.lower() == "mn":
            self.__pre_tension = float(pre_tension) * 1E-3
        elif pre_tension_unit.lower() == "un":
            self.__pre_tension = float(pre_tension) * 1E-6
        else:
            raise ValueError(
                "Expected the pre_tension_unit is one of {{'N','cN','dN','kN','mN','uN'}} case-ignored,"
                "but got {}.".format(pre_tension_unit))
        self.__pre_tension_unit = "N"

        # 确保tensile_speed_unit是字符串值。
        if not isinstance(tensile_speed_unit, str):
            raise ValueError("Expected tensile_speed_unit is a str.")

        # 以m/min为基准单位。
        if tensile_speed_unit.lower() == "m/min":
            self.__tensile_speed = float(tensile_speed)
        elif tensile_speed_unit.lower() == "mm/min":
            self.__tensile_speed = float(tensile_speed) * 1E-3
        elif tensile_speed_unit.lower() == "cm/min":
            self.__tensile_speed = float(tensile_speed) * 1E-2
        elif tensile_speed_unit.lower() == "dm/min":
            self.__tensile_speed = float(tensile_speed) * 1E-1
        elif tensile_speed_unit.lower() == "um/min":
            self.__tensile_speed = float(tensile_speed) * 1E-6
        elif tensile_speed_unit.lower() == "km/min":
            self.__tensile_speed = float(tensile_speed) * 1E3
        elif tensile_speed_unit.lower() == "m/s":
            self.__tensile_speed = float(tensile_speed) * 60.0
        elif tensile_speed_unit.lower() == "mm/s":
            self.__tensile_speed = float(tensile_speed) * 1E-3 * 60.0
        elif tensile_speed_unit.lower() == "cm/s":
            self.__tensile_speed = float(tensile_speed) * 1E-2 * 60.0
        elif tensile_speed_unit.lower() == "dm/s":
            self.__tensile_speed = float(tensile_speed) * 1E-1 * 60.0
        elif tensile_speed_unit.lower() == "um/s":
            self.__tensile_speed = float(tensile_speed) * 1E-6 * 60.0
        elif tensile_speed_unit.lower() == "km/s":
            self.__tensile_speed = float(tensile_speed) * 1E3 * 60.0
        elif tensile_speed_unit.lower() == "m/h":
            self.__tensile_speed = float(tensile_speed) / 60.0
        elif tensile_speed_unit.lower() == "mm/h":
            self.__tensile_speed = float(tensile_speed) * 1E-3 / 60.0
        elif tensile_speed_unit.lower() == "cm/h":
            self.__tensile_speed = float(tensile_speed) * 1E-2 / 60.0
        elif tensile_speed_unit.lower() == "dm/h":
            self.__tensile_speed = float(tensile_speed) * 1E-1 / 60.0
        elif tensile_speed_unit.lower() == "um/h":
            self.__tensile_speed = float(tensile_speed) * 1E-6 / 60.0
        elif tensile_speed_unit.lower() == "km/h":
            self.__tensile_speed = float(tensile_speed) * 1E3 / 60.0
        else:
            raise ValueError("Expected the tensile_speed_unit is one of case-ignored {{"
                             "'m/min','cm/min','mm/min','dm/min','um/min','km/min',"
                             "'m/s,'cm/s','mm/s','dm/s','um/s','km/s',"
                             "'m/h','cm/h','mm/h','dm/h','um/h','km/h'}}, "
                             "but got {}.".format(tensile_speed_unit))
        self.__tensile_speed_unit = "m/min"

        # 计算应变，单位：%
        self.__strain = (self.__displacement / self.__clamping_distance) * 100
        self.__strain_unit = "%"

        # 计算截面积，单位：m^2
        self.__cross_section_area = self.__sample_width * self.__sample_thickness
        self.__cross_section_area_unit = "m^2"

        # 计算应力，单位：MPa
        self.__stress = (self.__force / self.__cross_section_area) * 1E-6
        self.__stress_unit = "MPa"

        # 最大应力处的索引值。
        self.__max_stress_index = np.argmax(self.__stress)
        self.__breaking_stress_index = self.__max_stress_index

        # 最大应变处的索引值。
        self.__max_strain_index = np.argmax(self.__strain)

        # 其他关键字参数转换为对象的属性。
        for key in kwargs.keys():
            if hasattr(self, key):
                continue
            else:
                setattr(self, key, kwargs[key])
        self.kwargs = kwargs

    @property
    def displacement(self) -> npt.NDArray[np.float64]:
        """
        获取应变量（位移）。

        :return: 应变量（位移）。
        """
        return self.__displacement

    @property
    def force(self) -> npt.NDArray[np.float64]:
        """
        获取应力。

        :return: 应力。
        """
        return self.__force

    @property
    def time(self) -> npt.NDArray[np.float64]:
        """
        获取采样时间。

        :return: 采样时间。
        """
        return self.__time

    @property
    def displacement_unit(self) -> str:
        """
        获取应变量的单位。

        :return: 应变量的单位。
        """
        return self.__displacement_unit

    @property
    def force_unit(self) -> str:
        """
        获取应力的单位。

        :return:应力的单位。
        """
        return self.__force_unit

    @property
    def time_unit(self) -> str:
        """
        获取采样时间的单位。

        :return: 采样时间的单位。
        """
        return self.__time_unit

    @property
    def len(self) -> int:
        """
        获取原始数据的长度。

        :return:原始数据的长度。
        """
        return self.__len

    @property
    def sample_name(self) -> str:
        """
        获取样品名。

        :return: 样品名。
        """
        return self.__sample_name

    @property
    def sample_test_no(self) -> int:
        """
        获取样品测试编号。

        :return: 样品测试编号。
        """
        return self.__sample_test_no

    @property
    def name(self) -> str:
        """
        获取应力-应变曲线名。

        :return: 应力-应变曲线名。
        """
        return self.__name

    @property
    def sample_thickness(self) -> float:
        """
        获取样品厚度。

        :return:样品厚度。
        """
        return self.__sample_thickness

    @property
    def sample_thickness_unit(self) -> str:
        """
        获取样品厚度的单位。

        :return:样品厚度的单位。
        """
        return self.__sample_thickness_unit

    @property
    def sample_width(self) -> float:
        """
        获取样品宽度。

        :return:样品宽度。
        """
        return self.__sample_width

    @property
    def sample_width_unit(self) -> str:
        """
        获取样品宽度的单位。

        :return:样品宽度的单位。
        """
        return self.__sample_width_unit

    @property
    def clamping_distance(self) -> float:
        """
        获取夹持间距。

        :return:夹持间距。
        """
        return self.__clamping_distance

    @property
    def clamping_distance_unit(self) -> str:
        """
        获取夹持间距的单位。

        :return:夹持间距的单位。
        """
        return self.__clamping_distance_unit

    @property
    def pre_tension(self) -> float:
        """
        获取预加张力。

        :return: 预加张力。
        """
        return self.__pre_tension

    @property
    def pre_tension_unit(self) -> str:
        """
        获取预加张力的单位。

        :return: 预加张力的单位。
        """
        return self.__pre_tension_unit

    @property
    def tensile_speed(self) -> float:
        """
        获取拉伸速度。

        :return: 拉伸速度。
        """
        return self.__tensile_speed

    @property
    def tensile_speed_unit(self) -> str:
        """
        获取拉伸速度的单位。

        :return: 拉伸速度的单位。
        """
        return self.__tensile_speed_unit

    # ================================================================
    @property
    def strain_rate(self) -> Tuple:
        """
        获取应变速率。

        :return: 应变速率。
        """
        time_data = np.column_stack((self.time,))
        time_data = sm.add_constant(time_data)
        res = sm.RLM(self.strain, time_data).fit()
        return res.params[1], res

    @property
    def strain(self) -> npt.NDArray[np.float64]:
        """
        获取应变，单位：%。

        :return: 应变，单位：%。
        """
        return self.__strain

    @property
    def strain_unit(self):
        """
        获取应变的单位：%。

        :return: 应变的单位：%。
        """
        return self.__strain_unit

    @property
    def cross_section_area(self) -> float:
        """
        获取截面积，单位：m^2。

        :return: 截面积，单位：m^2。
        """
        return self.__cross_section_area

    @property
    def cross_section_area_unit(self):
        """
        获取截面积的单位：m^2。

        :return: 截面积的单位：m^2。
        """
        return self.__cross_section_area_unit

    @property
    def stress(self) -> npt.NDArray[np.float64]:
        """
        获取应力，单位：MPa。

        :return: 应力，单位：MPa。
        """
        return self.__stress

    @property
    def stress_unit(self):
        """
        获取应力的单位：MPa。

        :return: 应力的单位：MPa。
        """
        return self.__stress_unit

    @property
    def max_stress_index(self):
        """
        获取最大应力的索引。

        :return: 最大应力的索引。
        """
        return np.argmax(self.__stress)

    @property
    def max_strain_index(self):
        """
        获取最大应变的索引。

        :return: 最大应变的索引。
        """
        return np.argmax(self.__strain)

    # =============================================================
    # noinspection DuplicatedCode
    def find_index_strain(self, value: float, is_from_strain: bool = True):
        """
        找到小于指定应变值的最大应变的索引。

        :param value: 指定的应变（单位：%）或应变量（单位：m)。
        :param is_from_strain: 如果为True，则依据应变值找，否则依据位移值中找。
        :return: 小于指定应变值的最大应变的索引。
        """
        if is_from_strain:
            r = np.where(np.diff(np.sign(self.strain - value)) != 0)
            idx = r + (value - self.strain[r]) / (self.strain[r + np.ones_like(r)] - self.strain[r])
            idx = np.append(idx, np.where(self.strain == value))
            idx = np.sort(idx)
            return int(np.round(idx)[0])
        else:
            r = np.where(np.diff(np.sign(self.displacement - value)) != 0)
            idx = r + (value - self.displacement[r]) / (
                    self.displacement[r + np.ones_like(r)] - self.displacement[r])
            idx = np.append(idx, np.where(self.displacement == value))
            idx = np.sort(idx)
            return int(np.round(idx)[0])

    def find_index_strain_range(self, value1, value2, is_from_strain: bool = True):
        """
        找到小于指定应变范围内的索引。

        :param is_from_strain: 如果为True，则依据应变值找，否则依据位移值中找。
        :param value1: 指定的应变（单位：%）或应变量（单位：m)。
        :param value2: 指定的应变（单位：%）或应变量（单位：m)。
        :return: 索引范围。
        """
        strain1_index = self.find_index_strain(value1, is_from_strain)
        strain2_index = self.find_index_strain(value2, is_from_strain)
        return (strain1_index, strain2_index) if strain2_index > strain1_index else (strain2_index, strain1_index)

    def slice(self, value1, value2, is_from_strain: bool = True):
        """
        切片。

        :param is_from_strain: 如果为True，则依据应变值找，否则依据位移值中找。
        :param value1: 指定的应变（单位：%）或应变量（单位：m)。
        :param value2: 指定的应变（单位：%）或应变量（单位：m)。
        :return: 索引。
        """
        value1_index, value2_index = self.find_index_strain_range(value1, value2, is_from_strain)
        return TensileCre(
            self.displacement[value1_index:(value2_index + 1)],
            self.force[value1_index:(value2_index + 1)],
            self.time[value1_index:(value2_index + 1)],
            displacement_unit=self.displacement_unit,
            force_unit=self.force_unit,
            time_unit=self.time_unit,
            sample_thickness=self.sample_thickness,
            sample_thickness_unit=self.sample_thickness_unit,
            sample_width=self.sample_width,
            sample_width_unit=self.sample_width_unit,
            clamping_distance=self.clamping_distance,
            clamping_distance_unit=self.clamping_distance_unit,
            pre_tension=self.pre_tension,
            pre_tension_unit=self.pre_tension_unit,
            tensile_speed=self.tensile_speed,
            tensile_speed_unit=self.tensile_speed_unit,
            sample_name=self.sample_name,
            sample_test_no=self.sample_test_no,
            **self.kwargs
        )

    # =============================================================
    def breaking_stress_index(self, setting=None):
        """
        获取断裂应力处的索引。

        :return: 断裂应力处的索引。
        """
        if setting is None:
            return self.__breaking_stress_index
        elif isinstance(setting, (int, float)):
            self.__breaking_stress_index = setting
            return self.__breaking_stress_index
        elif isinstance(setting, (tuple, list)):
            value1 = setting[0]
            value2 = setting[-1]
            strain1_index, strain2_index = self.find_index_strain_range(value1, value2)
            max_index = strain1_index + np.argmax(self.stress[strain1_index:(strain2_index + 1)])
            self.__breaking_stress_index = max_index
            return self.__breaking_stress_index
        else:
            raise TypeError(
                "Expected setting type is one of {{None,int,float,tuple,list}},"
                "but got {}.".format(type(setting)))

    @property
    def breaking_stress(self):
        """
        获取断裂应力。

        :return: 断裂应力。
        """
        return self.stress[self.__breaking_stress_index]

    @property
    def breaking_strain(self):
        """
        获取断裂应变。

        :return: 断裂应变。
        """
        return self.strain[self.__breaking_stress_index]

    @property
    def toughness(self):
        """
        获取韧性。

        :return: 韧性。
        """
        half_strength = 0.5 * self.breaking_stress
        res = np.where(self.stress[self.__breaking_stress_index:] > half_strength)
        integ_end = len(res) + self.__breaking_stress_index
        return integrate.trapz(self.stress[:integ_end], self.strain[:integ_end] / 100.0), integ_end

    def modulus(self, setting=None):
        """
        计算模量。

        :param setting: 拟合区间设置。
        :return: 模量，拟合结果。
        """
        if setting is None:
            num_fitting = int(0.01 * self.len)
            xdata = self.strain[:num_fitting]
            ydata = self.stress[:num_fitting]
            x_vars = np.column_stack((xdata,))
            x_vars = sm.add_constant(x_vars)
            res = sm.RLM(ydata, x_vars).fit()
            return res.params[1] * 100, res
        elif isinstance(setting, (int, float)):
            num_fitting = self.find_index_strain(setting)
            xdata = self.strain[:num_fitting]
            ydata = self.stress[:num_fitting]
            x_vars = np.column_stack((xdata,))
            x_vars = sm.add_constant(x_vars)
            res = sm.RLM(ydata, x_vars).fit()
            return res.params[1] * 100, res
        elif isinstance(setting, (list, tuple)):
            value1 = setting[0]
            value2 = setting[-1]
            strain1_index, strain2_index = self.find_index_strain_range(value1, value2)
            xdata = self.strain[strain1_index:strain2_index + 1]
            ydata = self.stress[strain1_index:strain2_index + 1]
            x_vars = np.column_stack((xdata,))
            x_vars = sm.add_constant(x_vars)
            res = sm.RLM(ydata, x_vars).fit()
            return res.params[1] * 100, res
        else:
            raise TypeError(
                "Expected setting type is one of {{None,int,float,tuple,list}},"
                "but got {}.".format(type(setting)))

    def initial_modulus(self, num_fitting=None):
        """
        计算初始模量。

        :param num_fitting:计算初始模量需要的点数。
        :return:
        """
        if num_fitting is None:
            num_fitting = int(0.01 * self.len)
        xdata = self.strain[:num_fitting]
        ydata = self.stress[:num_fitting]
        x_vars = np.column_stack((xdata,))
        x_vars = sm.add_constant(x_vars)
        res = sm.RLM(ydata, x_vars).fit()
        return res.params[1] * 100, res

    def yield_point_index(self, num_fitting=None, num_extension=200, error=0.1):
        """
        获取屈服点索引。

        :param num_fitting: 拟合数据点数量。
        :param num_extension: 拟合区后扩展的点数。
        :param error: 偏离判断的误差。
        :return: 屈服点索引。
        """
        if num_fitting is None:
            num_fitting = int(0.01 * self.len)
        _, res = self.initial_modulus(num_fitting)
        fitting_value = res.params[1] * self.strain[:num_fitting + num_extension] + res.params[0]
        diff = self.stress[:num_fitting + num_extension] - fitting_value
        res_index = np.argwhere(np.abs(diff) > error)
        return res_index[0][-1]

    def yield_strain(self, num_fitting=None, num_extension=200, error=0.05):
        """
        获取屈服点索引。

        :param num_fitting: 拟合数据点数量。
        :param num_extension: 拟合区后扩展的点数。
        :param error: 偏离判断的误差。
        :return: 屈服点索引。
        """
        return self.strain[self.yield_point_index(num_fitting, num_extension, error)]

    def yield_stress(self, num_fitting=None, num_extension=200, error=0.1):
        """
        获取屈服点索引。

        :param num_fitting: 拟合数据点数量。
        :param num_extension: 拟合区后扩展的点数。
        :param error: 偏离判断的误差。
        :return: 屈服点索引。
        """
        return self.stress[self.yield_point_index(num_fitting, num_extension, error)]

    # =============================================================
    def reviews(self, **kwargs):
        """
        绘图。

        :param kwargs: 可选关键字参数。
        """
        plt.figure(figsize=(8, 6))
        if 'is_using_displacement' in kwargs and kwargs['is_using_displacement']:
            plt.plot(self.displacement, self.stress, label="{}".format(self.name))
            plt.xlabel('displacement ({})'.format(self.displacement_unit))
        else:
            plt.plot(self.strain, self.stress, label="{}".format(self.name))
            plt.xlabel('strain ({})'.format(self.strain_unit))
        plt.ylabel('stress ({})'.format(self.stress_unit))
        plt.show()

    def analysis(self, **kwargs):
        """
        综合分析。

        :param kwargs: 可选的关键字参数。
        :return: 所有分析结果组成的字典。
        """
        self.reviews(**kwargs)
        breaking_strain_range = input("please input the range of breaking strain:")
        bsr1_str, bsr2_str = breaking_strain_range.split(',')
        bsr1 = float(bsr1_str.strip())
        bsr2 = float(bsr2_str.strip())
        bsi = self.breaking_stress_index(setting=(bsr1, bsr2))

        initial_modulus_range = input("please input the range of initial modulus:")
        imr1_str, imr2_str = initial_modulus_range.split(',')
        imr1 = float(imr1_str.strip())
        imr2 = float(imr2_str.strip())
        imr2_value = self.find_index_strain(imr2)
        num_fitting = len(self.strain[:imr2_value + 1])

        # 保存原始数据。
        strain_stress = pd.DataFrame({"strain": self.strain, "stress": self.stress})

        # 保存剪切后的数据。
        strain_stress_truncate = pd.DataFrame({"strain": self.strain[:bsi],
                                               "stress": self.stress[:bsi]})

        # 用以保存最终结果。
        make_result = {"strain_stress": strain_stress, "strain_stress_truncate": strain_stress_truncate}

        # 计算初始模量
        modulus, modulus_fitting_res = self.initial_modulus(num_fitting)
        num_extension = 200
        error = 0.8
        # 计算屈服点
        yield_strain = self.yield_strain(num_fitting, num_extension, error=error)
        yield_stress = self.yield_stress(num_fitting, num_extension, error=error)

        # 计算韧性
        toughnes, integral_upper = self.toughness

        # 保存数据
        make_result["max_strain"] = self.breaking_strain
        make_result["max_stress"] = self.breaking_stress
        make_result["modulus"] = modulus
        make_result["yield_strain"] = yield_strain
        make_result["yield_stress"] = yield_stress
        make_result["toughnes"] = toughnes

        # 绘图
        plt.plot(self.strain, self.stress)
        plt.scatter(self.breaking_strain, self.breaking_stress, s=150, edgecolors='red',
                    label="Strain:{:.2f}%\nStress:{:.2f}MPa".format(self.breaking_strain, self.breaking_stress))
        plt.scatter(yield_strain, yield_stress, s=150, edgecolors='red',
                    label="yield_strain:{:.2f}%\nyield_stress:{:.2f}MPa".format(yield_strain, yield_stress))

        plt.plot(self.strain[:num_fitting], self.stress[:num_fitting], label="")
        fitting_value = modulus_fitting_res.params[1] * self.strain[:num_fitting + num_extension] + \
                        modulus_fitting_res.params[0]
        plt.plot(self.strain[:num_fitting + num_extension], fitting_value, label="Module:{:.2f}MPa".format(modulus))
        plt.fill_between(self.strain[:integral_upper], 0, self.stress[:integral_upper], facecolor='pink', alpha=0.9,
                         label="Toughnes:{:.2f}".format(toughnes))
        plt.xlim(0)
        plt.ylim(0)
        plt.legend(loc="best")
        plt.show()

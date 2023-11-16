#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        __init__.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: gxusthjw.zhxyao包的__init__.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/30     revise
# ----------------------------------------------------------------
# 导包 ============================================================
from .arbitrary_deriv_zhxyao import (deriv_gl_zhxyao, sech,
                                     sech_numpy, quasi_sech,
                                     quasi_sech_ifft0,
                                     quasi_sech_ifft,
                                     deriv_quasi_sech0,
                                     deriv_quasi_sech,
                                     deriv_quasi_sech0_reviews,
                                     deriv_quasi_sech_reviews)
from .arbitrary_deriv_zhxyao_ext import (deriv_quasi_sech0_with_fit_steepness,
                                         deriv_quasi_sech0_search)
from .smoothing_zhxyao import smoothing_zhxyao
from .arbitrary_deriv_zhxyao_oop import (EnvelopeFunction,
                                         QuasiSechEnvelope,
                                         GeneralPeakEnvelope,
                                         ArbitraryOrderDerivativeAlgorithm,
                                         ArbitraryOrderDerivativeZhxyaoGl,
                                         ArbitraryOrderDerivative)

# 定义 ============================================================
__version__ = "0.0.1"

__doc__ = """
 the functions and classes for Arbitrary order derivative
"""

__all__ = [
    'deriv_gl_zhxyao', 'sech', 'sech_numpy', 'quasi_sech',
    'quasi_sech_ifft0', 'quasi_sech_ifft',
    'deriv_quasi_sech0', 'deriv_quasi_sech',
    'deriv_quasi_sech0_reviews',
    'deriv_quasi_sech_reviews',
    'deriv_quasi_sech0_with_fit_steepness',
    'deriv_quasi_sech0_search',
    'smoothing_zhxyao',
    'EnvelopeFunction',
    'QuasiSechEnvelope',
    'GeneralPeakEnvelope',
    'ArbitraryOrderDerivativeAlgorithm',
    'ArbitraryOrderDerivativeZhxyaoGl',
    'ArbitraryOrderDerivative',

]

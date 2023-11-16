#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        __init__.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: pygxusthjw包的__init__.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/11/08     revise
# ----------------------------------------------------------------
# 导包 ============================================================
from . import axs
from . import commons
from . import findpeaks
from . import fityk
from . import fityk_helpers
from . import fsd
from . import ftir
from . import ma
from . import mathematics
from . import matlab
from . import nmr
from . import origin_helpers
from . import peakfit_helpers
from . import spectrum
from . import ta
from . import units
from . import xrd
from . import zhxyao

# 定义 ============================================================
__version__ = "0.0.1"

__doc__ = """
the python libraries of gxusthjw.
"""

# noinspection DuplicatedCode
__all__ = [
    'axs',
    'commons',
    'findpeaks',
    'fityk',
    'fityk_helpers',
    'fsd',
    'ftir',
    'ma',
    'mathematics',
    'matlab',
    'nmr',
    'origin_helpers',
    'peakfit_helpers',
    'spectrum',
    'ta',
    'units',
    'xrd',
    'zhxyao',
]

#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        __init__.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: gxusthjw.nmr包的__init__.py。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/11/05     revise
# ----------------------------------------------------------------
# 导包 ============================================================
from .bruker import (read_bruker_fid, read_bruker_pdata,
                     get_spectrum_from_bruker_pdata)

# 定义 ============================================================
__version__ = "0.0.1"

__doc__ = """
The functions and classes for processing nmr data.
"""

__all__ = ['read_bruker_fid', 'read_bruker_pdata',
           'get_spectrum_from_bruker_pdata']

# cython: language_level=3
# cython: profile=True
# Time-stamp: <2022-05-24 14:10:03 Tao Liu>

"""Module for HMMRStates IO classes.

This code is free software; you can redistribute it and/or modify it
under the terms of the BSD License (see the file LICENSE included with
the distribution).
"""

# ------------------------------------
# python modules
# ------------------------------------
#from itertools import groupby
#from operator import itemgetter
#import random
import re
import sys

# ------------------------------------
# MACS3 modules
# ------------------------------------

from MACS3.Utilities.Constants import *

# ------------------------------------
# Other modules
# ------------------------------------

from cpython cimport bool

# ------------------------------------
# constants
# ------------------------------------
__version__ = "HMMRStates $Revision$"
__author__ = "Tao Liu <vladimir.liu@gmail.com>"
__doc__ = "HMMRStates class"

# ------------------------------------
# Misc functions
# ------------------------------------
cdef str subpeak_letters( int i):
    if i < 26:
        return chr(97+i)
    else:
        return subpeak_letters(i // 26) + chr(97 + (i % 26))

# ------------------------------------
# Classes
# ------------------------------------

cdef class HMMRStates:
    cdef:
        public dict statepath       # dictionary storing statepath contents
        public bool CO_sorted   # whether peaks have been sorted by coordinations
        public long total       # total number of peaks

    def __init__ (self):
        self.peaks = {}
        self.CO_sorted = False
        self.total = 0

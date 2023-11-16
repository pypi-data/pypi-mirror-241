# cython: language_level=3
# cython: profile=True
# Time-stamp: <2022-02-22 17:33:44 Tao Liu>

"""Module for Mean and Stddev online algorithms

Copyright (c) 2017 Tao Liu <tao.liu@roswellpark.org>

This code is free software; you can redistribute it and/or modify it
under the terms of the BSD License (see the file COPYING included with
the distribution).

@status:  experimental
@version: $Revision$
@author:  Tao Liu
@contact: tao.liu@roswellpark.org
"""
# ------------------------------------
# python modules
# ------------------------------------

cdef class OnlineAlgo:
    cdef:
        float mean
        float stddev
        long counter
        float M2

    def __init__ (self):
        self.mean = 0
        self.stddev = 0
        self.counter = 0
        float M2 = 0

    cdef void add( self, element ):
    counter += 1
    delta = element - means
    new_means = means + delta / counter
    s = stds + (delta * (element - new_means))
    stds = sqrt( s / counter)

    return(counter, new_means, stds) 

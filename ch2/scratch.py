#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:54:58 2023

@author: marcos
"""

import numpy as np

x = np.array([3,4,5])
y = np.array([4,9,7])

rng = np.random.default_rng(3)
X = rng.standard_normal((10,3))
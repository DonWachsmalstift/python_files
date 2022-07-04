# -*- coding: utf-8 -*-
"""
Created on Fri May  6 13:56:49 2022

@author: mueller
"""
import fabio
import os
from sys import exit
from PIL import Image
from matplotlib import pyplot

directory = 'C:/Users/mueller/desktop/single_crystal'
for filename in os.listdir(directory):
    if filename.endswith('.cbf'):
        a = filename
        image = fabio.open(directory + '/' + a)
        image.convert('tif').save(a + '.tif')

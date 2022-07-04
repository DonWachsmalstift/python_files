# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:44:43 2022

@author: mueller
"""

import matplotlib.pyplot as plt
import pandas as pd
from sys import exit
import numpy as np
from glob import glob
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'qt')

path = r'C:\Users\mueller\Desktop\DESY\DESY_11_05\PDF'

cb_files = glob(f'{path}/CBa*')

df_cb = [pd.read_csv(cb_file, sep='\s+', names=['r', 'Gr'], header=None, skiprows=(26)) for cb_file in cb_files]

fig, ax1 = plt.subplots()

c = 0
for i, ax_i in enumerate(df_cb):

    c += 2
    name = [cb_files[i].split('\\')[-1].split('.')[0]]
    ax1.plot(df_cb[i].r, df_cb[i].Gr + c, c=np.random.rand(3,), label=name)
    #ax1.plot(df_cb_CB.TT, df_kat_CB.I, 'r-')
    ax1.legend()
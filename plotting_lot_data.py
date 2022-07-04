# -*- coding: utf-8 -*-
"""
Created on Tue May  3 16:29:26 2022

@author: mueller
"""

import matplotlib.pyplot as plt
import pandas as pd
from sys import exit
import numpy as np
from glob import glob
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'qt')
path = r'C:\Users\mueller\Desktop\DESY_dawn'
dat_files = list(set(glob(f'{path}/*.dat')) - set(glob(f'{path}/*Traeger*.dat')) - set(glob(f'{path}/*empty*.dat'))
                     - set(glob(f'{path}/*SiO2*.dat')) - set(glob(f'{path}/*LaB6*.dat')))
sup_files = glob(f'{path}/*Traeger*')
emp_files = glob(f'{path}/*empty*')

dat_dfs = [pd.read_csv(dat_file, sep='\s+', names=['TT', 'I'], header=None) for dat_file in dat_files]
name_dat = [file.split('\\')[-1].split('.')[0] for file in dat_files]
sup_dfs = [pd.read_csv(sup_file, sep='\s+', names=['TT', 'I'], header=None) for sup_file in sup_files]
name_sup = [file.split('\\')[-1].split('.')[0] for file in sup_files]
emp_dfs = [pd.read_csv(emp_file, sep='\s+', names=['TT', 'I'], header=None) for emp_file in emp_files]

fig, ax = plt.subplots(2, 2)

ax_flat = np.array(ax).reshape(-1)

scale = [1.025, 1.075]

var = 0
# =============================================================================
# print(dat_dfs[1])
# exit()
# =============================================================================
for i, ax_i in enumerate(ax_flat):
    if i%2 == 0:
        ind = int(i/2)

        ax_i.plot(dat_dfs[ind].TT, dat_dfs[ind].I, label=name_dat[ind])
        ax_i.plot(sup_dfs[ind].TT, sup_dfs[ind].I * scale[ind], 'r-',
                  label=name_sup[ind] + ' ' + 'scale =' + ' ' + str(scale[ind]))
        ax_i.legend()
    if i%2 == 1:
        var += 1
        ind = int(i-var)

        ax_i.plot(dat_dfs[ind].TT, dat_dfs[ind].I - sup_dfs[ind].I * scale[ind],
                  label='diff')
        ax_i.legend()

plt.show()
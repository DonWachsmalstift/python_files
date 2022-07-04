# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:44:56 2022

@author: mueller
"""


import matplotlib.pyplot as plt
from glob import glob
import pandas as pd
from sys import exit

path = r'C:/users/mueller/desktop/rwth phd/narayanan_xrd/processed_by_narayanan'

dat_files = (glob(f'{path}/SCALMS*'))
dat_dfs = [pd.read_csv(dat_file, sep='\s+', names=['r', 'I'], header=None, skiprows=27) for dat_file in dat_files]
name = [file.split('\\')[-1] for file in dat_files]
# =============================================================================
# print(name[0])
# exit()
# =============================================================================
    
# =============================================================================
# print(dat_dfs[0])
# exit()
# 
# =============================================================================
fig, ax1 = plt.subplots()

ax1.plot(dat_dfs[0].r, dat_dfs[0].I, 'r-', label=name[0])
ax1.plot(dat_dfs[1].r, dat_dfs[1].I, 'b-', label=name[1])
ax1.plot(dat_dfs[2].r, dat_dfs[2].I, 'g-', label=name[2])
plt.legend()

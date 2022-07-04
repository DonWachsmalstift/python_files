# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:00:16 2022

@author: mueller
"""

import matplotlib.pyplot as plt
import pandas as pd
from sys import exit
import numpy as np
from glob import glob
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')


path = path = r'C:/Users/mueller/Desktop/DESY/DESY_19_05/'

cap = path + r'20220509_112628_CBa_SiO2_Traeger_1-3_sum_00000.q'
#sup = path + r'20220509_112628_CBa_SiO2_Traeger_1-3_sum.chi'
kat = path + r'20220509_112546_CBa_156.4_Katalysator_1-3_sum_00000.q'

df_cap = pd.read_csv(cap, sep='\s+', names=['Q', 'I'], header=None) #, skiprows=(8))
#df_sup = pd.read_csv(sup, sep='\s+', names=['Q', 'I'], header=None, skiprows=(8))
df_kat = pd.read_csv(kat, sep='\s+', names=['Q', 'I'], header=None) #, skiprows=(8))

fig, ax1 = plt.subplots()

ax1.plot(df_cap.Q, df_cap.I, 'b-', label='capillary')
#ax1.plot(df_sup.Q, df_sup.I, 'r-', alpha=0.5, label='support')
ax1.plot(df_kat.Q, df_kat.I, 'g-', alpha=0.5, label='catalyst')
ax1.legend()
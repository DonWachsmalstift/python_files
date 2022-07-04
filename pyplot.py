# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:09:26 2022

@author: mueller
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'qt')
path = r'C:/Users/mueller/desktop/Messungen_Simitsis'

df1 = pd.read_csv(path + r'/Ag_Hb/Ag_Hb_acc.xyd', sep='\s+',
                 names=['Q', 'I'])
df2 = pd.read_csv(path + r'/Hb_110C/Hb_110C_acc.xyd', sep='\s+',
                 names=['Q', 'I'])

fig, ax1 = plt.subplots()

ax1.plot(df1.Q, df1.I, 'r-', label='cat')
ax1.plot(df2.Q, df2.I - 1000, 'g-', label='sup_not_calcined')
ax1.legend(prop={'size': 20})
#plt.savefig(path + r'sup+cat.jpg', dpi=200)

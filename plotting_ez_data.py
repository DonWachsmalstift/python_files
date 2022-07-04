# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython import get_ipython
from sys import exit

path_1 = r'C:/Users/mueller/Desktop/DESY_29.04'
path_2 = r'C:/Users/mueller/Desktop/DESY_dawn'


df_1_1 = pd.read_csv(path_1 + r'/20220429_150416_empty_16-75_sum.chi', sep='\s+',
                 names=['Q', 'I'], skiprows=(8))
df_1_2 = pd.read_csv(path_1 + r'/20220429_150308_BK_Katalysator_76-135_sum.chi', sep='\s+',
                 names=['Q', 'I'], skiprows=(8))
df_1_3 = pd.read_csv(path_1 + r'/20220429_145847_CBa_156.4_Katalysator_196-255_sum.chi', sep='\s+',
                 names=['Q', 'I'], skiprows=(8))




df_2_1 = pd.read_csv(path_2 + r'/20220429_150416_empty_16-75_sum_00000.dat', sep='\s+',
                   names=['TT', 'I'])
df_2_2 = pd.read_csv(path_2 + r'/20220429_150308_BK_Katalysator_76-135_sum_00000.dat', sep='\s+',
                   names=['TT', 'I'])
df_2_3 = pd.read_csv(path_2 + r'/20220429_145847_CBa_156.4_Katalysator_196-255_sum_00000.dat', sep='\s+',
                   names=['TT', 'I'])

#df.to_csv(r'C:/Users/mueller/Desktop/d_spacing/NdPO4_dspacing.d', index=False
#get_ipython().run_line_magic('matplotlib', 'qt')



lam = 0.20733 
tt_t_q = lambda x: 4 * np.pi * np.sin(x * np.pi / (180 * 2 )) / lam

df_2_1['Q'] = df_2_1['TT'].apply(tt_t_q)
df_2_2['Q'] = df_2_2['TT'].apply(tt_t_q)
df_2_3['Q'] = df_2_3['TT'].apply(tt_t_q)



# =============================================================================
# df_1_2['I'] = df_1_2['I'] / (np.max(df_1_2['I'])-np.min(df_1_2['I']))
# df_2_2['I'] = df_2_2['I'] / (np.max(df_2_2['I'])-np.min(df_2_2['I']))
# 
# =============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2)
#fig, (ax1) = plt.subplots(nrows=1, ncols=1, sharex=False, sharey=False)





ax1.plot(df_1_3.Q, df_1_3.I,'r-') #label=path_11[len(path_data_folder) + 1:-3])
ax1.plot(df_2_3.Q, df_2_3.I, 'b-')
ax2.plot(df_1_2.Q, df_1_2.I,'r-')
ax2.plot(df_2_2.Q, df_2_2.I, 'b-')
#plt.savefig(path + r'/arsch.png', dpi=500)
plt.show()

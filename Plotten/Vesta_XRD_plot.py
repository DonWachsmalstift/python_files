# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 10:28:44 2022

@author: mueller
"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from sys import exit

path_data_folder = r'C:\Users\mueller\Desktop\LaCeNiO_Palkovits\Bayreuth'


path_1 = path_data_folder + r'\CeO2.xy'
path_2 = path_data_folder + r'\La2O3.xy'
path_3 = path_data_folder + r'\NiO.xy'
path_4 = path_data_folder + r'\La05Ce15niO4.xyd'
path_5 = path_data_folder + r'\La2NiO4_tetragonal.xy'
path_5_1 = path_data_folder + r'\LaNiO3.xy'
path_5_2 = path_data_folder + r'\La2NiO4_F4_mmm.xy'
path_6 = path_data_folder + r'\redLa05Ce15niO4.xyd'

path_7 = path_data_folder + r'\La2NiO4_palko.xy'
path_8 = path_data_folder + r'\La15Ce05NiO4_palko.xy'
path_9 = path_data_folder + r'\LaCeNiO4_palko.xy'
path_10 = path_data_folder + r'\La05Ce15NiO4_palko.xy'
path_11 = path_data_folder + r'\Ce2NiO4_palko.xy'





lam_cu = 1.54059
lam = 0.5594075
tt_t_q = lambda x: 4 * np.pi * np.sin(x * np.pi / (180 * 2 )) / lam
tt_t_q_cu = lambda x: 4 * np.pi * np.sin(x * np.pi / (180 * 2 )) / lam_cu

df_1 =pd.read_csv(path_1, sep='\s+', names=['TT', 'I', 'dI'])
df_2 =pd.read_csv(path_2, sep='\s+', names=['TT', 'I', 'dI'])
df_3 =pd.read_csv(path_3, sep='\s+', names=['TT', 'I', 'dI'])
df_4 =pd.read_csv(path_4, sep='\s+', names=['Q', 'I'])
df_5 =pd.read_csv(path_5, sep='\s+', names=['TT', 'I', 'dI'])
df_5_1 =pd.read_csv(path_5_1, sep='\s+', names=['TT', 'I', 'dI'])
df_5_2 =pd.read_csv(path_5_2, sep='\s+', names=['TT', 'I', 'dI'])

df_6 =pd.read_csv(path_6, sep='\s+', names=['Q', 'I'])

df_7 =pd.read_csv(path_7, sep='\s+', names=['TT', 'I'])
df_8 =pd.read_csv(path_8, sep='\s+', names=['TT', 'I'])
df_9 =pd.read_csv(path_9, sep='\s+', names=['TT', 'I'])
df_10 =pd.read_csv(path_10, sep='\s+', names=['TT', 'I'])
df_11 =pd.read_csv(path_11, sep='\s+', names=['TT', 'I'])
# =============================================================================
# print(df_1, df_4)
# exit()
# =============================================================================

df_1['Q'] = df_1['TT'].apply(tt_t_q)
df_2['Q'] = df_2['TT'].apply(tt_t_q)
df_3['Q'] = df_3['TT'].apply(tt_t_q)
df_5['Q'] = df_5['TT'].apply(tt_t_q)
df_5_1['Q'] = df_5_1['TT'].apply(tt_t_q)
df_5_2['Q'] = df_5_2['TT'].apply(tt_t_q)

df_7['Q'] = df_7['TT'].apply(tt_t_q_cu)
df_8['Q'] = df_8['TT'].apply(tt_t_q_cu)
df_9['Q'] = df_9['TT'].apply(tt_t_q_cu)
df_10['Q'] = df_10['TT'].apply(tt_t_q_cu)
df_11['Q'] = df_11['TT'].apply(tt_t_q_cu)


#matplotlib widget


df_1['I'] = df_1['I'] / (np.max(df_1['I'])-np.min(df_1['I']))
df_2['I'] = df_2['I'] / (np.max(df_2['I'])-np.min(df_2['I']))
df_3['I'] = df_3['I'] / (np.max(df_3['I'])-np.min(df_3['I']))
df_4['I'] = df_4['I'] / (np.max(df_4['I'])-np.min(df_4['I']))
df_5['I'] = df_5['I'] / (np.max(df_5['I'])-np.min(df_5['I']))
df_5_1['I'] = df_5_1['I'] / (np.max(df_5_1['I'])-np.min(df_5_1['I']))
df_5_2['I'] = df_5_2['I'] / (np.max(df_5_2['I'])-np.min(df_5_2['I']))

df_6['I'] = df_6['I'] / (np.max(df_6['I'])-np.min(df_6['I']))
df_7['I'] = df_7['I'] / (np.max(df_7['I'])-np.min(df_7['I']))
df_8['I'] = df_8['I'] / (np.max(df_8['I'])-np.min(df_8['I']))
df_9['I'] = df_9['I'] / (np.max(df_9['I'])-np.min(df_9['I']))
df_10['I'] = df_10['I'] / (np.max(df_10['I'])-np.min(df_10['I']))
df_11['I'] = df_11['I'] / (np.max(df_11['I'])-np.min(df_11['I']))


# =============================================================================
# plt.subplot(121)
# plt.plot()
# plt.ylabel('I [a.u.]')
# plt.plot(df_Co.Q, df_Co.I, label='Co')
# plt.plot(df_CoO.Q, df_CoO.I, label='CoO')
# plt.xlabel('Q [A^-1]')
# plt.legend()
# plt.subplot(122)
# plt.plot(df_Co.TT, df_Co.I)
# plt.plot(df_CoO.TT, df_CoO.I)
# plt.xlabel(r'2$\theta$ [°]')
# plt.show()
# =============================================================================

fig, (ax1) = plt.subplots(nrows=1, ncols=1, sharex=False, sharey=False)




#ax1.plot(df_4.Q, df_4.I,'r-', label=path_4[len(path_data_folder) + 1:-4])
#ax1.plot(df_6.Q, df_6.I,'b-', label=path_6[len(path_data_folder) + 1:-4])
#ax1.plot(df_5.Q, df_5.I +2,'m-', label=path_5[len(path_data_folder) + 1:-3])
#ax1.plot(df_5_1.Q, df_5_1.I + 2,'y-', label=path_5_1[len(path_data_folder) + 1:-3])
#ax1.plot(df_5_2.Q, df_5_2.I +2,'y-', label=path_5_2[len(path_data_folder) + 1:-3])

#ax1.plot(x_2, y_2n, 'r-', label=path_2[len(path_data_folder) + 1:-4])
#ax1.plot(x_4, y_4n, 'm-', label=path_4[len(path_data_folder) + 1:-4])
#ax1.plot(x_5, y_5n, 'c-', label=path_5[len(path_data_folder) + 1:-4])
#ax1.plot(df_3.Q, df_3.I,'m-', label=path_3[len(path_data_folder) + 1:-3])


ax1.plot(df_11.Q, df_11.I - 1.5 ,'k-', label=path_11[len(path_data_folder) + 1:-3])
ax1.plot(df_10.Q, df_10.I - 2.5  ,'y-', label=path_10[len(path_data_folder) + 1:-3])
ax1.plot(df_9.Q, df_9.I - 1.5 ,'b-', label=path_9[len(path_data_folder) + 1:-3])
ax1.plot(df_8.Q, df_8.I - 3  ,'r-', label=path_8[len(path_data_folder) + 1:-3]) #La15Ce05NiO4 Palko
ax1.plot(df_7.Q, df_7.I - 1 ,'g-', label=path_7[len(path_data_folder) + 1:-3]) #La2NiO4 Palko

ax1.plot(df_1.Q, df_1.I * 5,'m-', label=path_1[len(path_data_folder) + 1:-3])
ax1.plot(df_2.Q, df_2.I * 5,'c-', label=path_2[len(path_data_folder) + 1:-3])
ax1.plot(df_3.Q, df_3.I * 5, 'k-', label=path_3[len(path_data_folder) + 1:-3])



font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

plt.xlabel(r'Q(A$^-$$^1$)', fontdict=font)
plt.ylabel('I [a.u.]', fontdict=font)

plt.xlim([0, 7])

ax1.grid("on")

ax1.legend(loc="upper right")
plt.show()
#plt.savefig(path_data_folder + r'palkovits_supreme.png', dpi=500)
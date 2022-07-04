# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:04:04 2022

@author: mueller
"""

import pandas as pd
import numpy as np
from glob import glob
from sys import exit

path = r'C:/Users/mueller/Desktop/DESY/DESY_19_05/processed/'
path_normalized =  r'C:/Users/mueller/Desktop/DESY/DESY_19_05/processed/normalized/'
xrd_files = glob(f'{path}/*sum.chi')
xrd_dfs = [pd.read_csv(xrd_file, sep='\s+', names=['Q', 'I'], header=None, skiprows=8) for xrd_file in xrd_files]
name_dat = [file.split('\\')[-1].split('sum')[0] for file in xrd_files]

#df_1_2['I'] = df_1_2['I'] / (np.max(df_1_2['I'])-np.min(df_1_2['I']))

for i in range(len(xrd_dfs)):
# =============================================================================
#     print(xrd_dfs[i]["I"])
# =============================================================================

    xrd_dfs[i]["I"] = xrd_dfs[i]["I"] / (np.max(xrd_dfs[i]["I"]) - np.min(xrd_dfs[i]["I"]))
# =============================================================================
#     print(xrd_dfs[i]["I"])
#     exit()
# =============================================================================
    xrd_dfs[i].to_csv(path_normalized +   name_dat[i] + '.csv', sep='\t', header=False, index=False)
    
                              
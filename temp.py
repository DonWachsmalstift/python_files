# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
path = r'C:/Users/mueller/Desktop/DESY_29.04'
df = pd.read_csv(path + r'/20220429_145116_CBa_159.2_SiO2_GOAc2_376-430_sum.chi', sep='\s+',
                 names=['Q', 'I'], skiprows=(8))
#df.to_csv(r'C:/Users/mueller/Desktop/d_spacing/NdPO4_dspacing.d', index=False)
plt.plot(df.Q, df.I)
plt.savefig(path + r'/arsch.png', dpi=500)



"""
Spyder Editor

This is a File to plot multiple scaled PDF_s in one Plot
"""

import matplotlib.pyplot as plt
import pandas as pd
from os import listdir
import numpy as np
from sys import exit

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }


path_data_folder = r'C:\Users\mueller\Desktop\LaCeNiO_Palkovits\Bayreuth\G(r)'
### path_1 = g_diff ###
path_data_1 = path_data_folder + r'\g_diffn_red.csv'
path_data_2 = path_data_folder + r'\redLa05Ce15NiO4_plot.gr'
path_data_3 = path_data_folder + r'\g_calcn_red.csv'
#path_data_4 = path_data_folder + r'\Calculated_Co_PDF.txt'
#path_data_5 = path_data_folder + r'\Calculated_CoO_PDF.txt'

data_1 = pd.read_csv(path_data_1, sep="r", header=None).values
data_2 = pd.read_csv(path_data_2, sep=" ", header=None).values
data_3 = pd.read_csv(path_data_3, sep="r", header=None).values
#data_4 = pd.read_csv(path_data_4, sep=" ", header=None).values
#data_5 = pd.read_csv(path_data_5, sep=" ", header=None).values
print(data_1)
exit()




x_1 = data_1[:, 0]
x_2 = data_2[:, 0]
x_3 = data_3[:, 0]
#x_4 = data_4[:, 0]
#x_5 = data_5[:, 0]

y_1 = data_1[:, 1]
y_2 = data_2[:, 1]
y_3 = data_3[:, 1]
#y_4 = data_4[:, 1]
#y_5 = data_5[:, 1]

y_1n = (y_1) / (np.max(y_1)-np.min(y_1)) - 1
y_2n = (y_2) / (np.max(y_2)-np.min(y_2)) 
y_3n = (y_3) / (np.max(y_3)-np.min(y_3)) 
#y_4n = (y_4) / (np.max(y_4)-np.min(y_4)) + 1
#y_5n = (y_5) / (np.max(y_5)-np.min(y_5)) + 2


fig, (ax1) = plt.subplots(nrows=1, ncols=1, sharex=False, sharey=False)

ax1.plot(x_1, y_1n,'b--', label=path_data_1[len(path_data_folder) + 1:-4])
ax1.plot(x_2, y_2n, 'r-', label=path_data_2[len(path_data_folder) + 1:-4])
ax1.plot(x_3, y_3n, 'g-', label=path_data_3[len(path_data_folder) + 1:-4])
#ax1.plot(x_4, y_4n, 'm-', label=path_data_4[len(path_data_folder) + 1:-4])
#ax1.plot(x_5, y_5n, 'c-', label=path_data_5[len(path_data_folder) + 1:-4])

plt.xlabel('r / Å', fontdict=font)
plt.ylabel('G(r) / a.u.', fontdict=font)



ax1.grid("on")

ax1.legend(loc="upper right")

plt.show()

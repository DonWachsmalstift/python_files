
"""
Created on Sun May 22 11:15:37 2022

@author: Bleck
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sys import exit
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'qt')


###Definition von Gleichungen###
def Debye_Hückel(z, I, a):
    A = 0.5085
    B = 0.3285*10**10
    log_gamma= - (A* z**2 * np.sqrt(I))/(1+ B *a * np.sqrt(I))
    gamma = 10**log_gamma
    return gamma

def Truesdell_Jones(z, I, a, b):
    A = 0.5085
    B = 0.3285*10**10
    log_gamma= - (A* z**2 * np.sqrt(I))/(1+ B *a * np.sqrt(I)) +b*I
    gamma = 10**log_gamma
    return gamma
    
###Definition vom Intervall I###
I = np.arange(0.0001, 10, 0.001)

###Definition von Ionen###
Na = Debye_Hückel(1, I, 4*10**-10)
Mg = Debye_Hückel(2, I, 8*10**-10)
SO4 = Debye_Hückel(2, I, 4*10**-10)

Na_T = Truesdell_Jones(1, I, 4*10**-10, 0.075)
Mg_T = Truesdell_Jones(2, I, 8*10**-10, 0.2)
SO4_T = Truesdell_Jones(2, I, 4*10**-10, -0.04)


fig, ax1 = plt.subplots()
ax1.set_xscale('log')
ax1.set_ylim([0, 1.2])

ax1.plot(I, Na, 'r-', label="Debye-Hückel $Na^{+}$")
ax1.plot(I, Mg, '-b',label='Debye-Hückel $Mg^{2+}$')
ax1.plot(I, SO4, '-g',label='Debye-Hückel $SO_4^{2-}$')
ax1.plot(I, Na_T, '--r',label='Truesdell-Jones $Na^+$')
ax1.plot(I, Mg_T, '--b',label='Truesdell-Jones $Mg^{2+}$')
ax1.plot(I, SO4_T, '--g',label='Truesdell-Jones $SO_4^{2-}$')
plt.legend()

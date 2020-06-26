# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:19:01 2020

@author: GSC
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas
import scipy.fftpack

"""
===============================================================================
DATA PREPARATION
===============================================================================
"""


TT=pandas.read_csv("TT.csv")
TTc=pandas.read_csv("TT.csv")

#TT.drop(["DATE"], axis=1)
#TTc.drop(["DATE"], axis=1)

def func0(x):
    if x>20 and x<50:
        return x
    else:
        return 0
        
        
def func1(x):
    if x>10:
        return x
    else:
        return 0     

TTc["TAVE"]=TT["TAVE"].apply(lambda x:func0(x))
TTc["TMAX"]=TT["TMAX"].apply(lambda x:func0(x))
TTc["TMIN"]=TT["TMIN"].apply(lambda x:func0(x))
TTc["RAIN"]=TT["RAIN"].apply(lambda x:func1(x))
TTa=TTc.as_matrix()
L=len(TTa[:,0])
for jj in range(0,len(TTa[:,0])):
    if jj==0:
        if TTa[jj,2] ==0:
            TTa[jj,2]=np.average(TTa[:,2])
    else:
        if TTa[jj,2]== 0:
            TTa[jj,2]=np.average(TTa[jj-1,2])
            
for jj in range(0,len(TTa)):
    if jj==0:
        if TTa[jj,3] ==0:
            TTa[jj,3]=np.average(TTa[:,3])
    else:
        if TTa[jj,3]== 0:
            TTa[jj,3]=np.average(TTa[jj-1,3])
            
for jj in range(0,len(TTa)):
    if jj==0:
        if TTa[jj,5] ==0:
            TTa[jj,5]=np.average(TTa[:,5])
    else:
        if TTa[jj,5]== 0:
            TTa[jj,5]=np.average(TTa[jj-1,5])


"""
===============================================================================
PLOTTING
===============================================================================
"""
plt.figure(0)
ax0=plt.subplot(312)
plt.title("Temp. Average")   
plt.plot(TT["TAVE"],color="r")
plt.xticks(rotation="horizontal")
plt.ylabel("ºC")

ax0=plt.subplot(313)
plt.title("Temp. Max.")   
plt.plot(TT["TMAX"],color="b")
plt.ylabel("ºC")

ax0=plt.subplot(311)
plt.title("Temp. Min.")   
plt.plot(TT["TMIN"],color="m")
plt.ylabel("ºC")

"""
===============================================================================
"""



plt.figure(1)
x=np.arange(0,len(TTa[:,0]))

ax1=plt.subplot(313)
plt.title("Temp. Average")   
plt.plot(x,TTa[:,5],color="m") 
plt.xticks(rotation="horizontal")
plt.ylabel("ºC")

ax1=plt.subplot(311)
plt.title("Temp. Max.")   
plt.plot(x,TTa[:,2],color="r") 
plt.ylabel("ºC")

ax1=plt.subplot(312)
plt.title("Temp. Min.")   
plt.plot(x,TTa[:,3],color="b") 
plt.ylabel("ºC")

#"""
#===============================================================================
#"""

plt.figure(2)
ax2=plt.subplot(212)
plt.title("Solar radiation")   
plt.plot(TT["SRAD"],color="r")
plt.xticks(rotation="horizontal")
plt.ylabel("W2/m2")

ax2=plt.subplot(211)
plt.title("Precipitation")   
plt.plot(TT["RAIN"],color="r")
plt.xticks(rotation="horizontal")
plt.ylabel("mm")


"""
===============================================================================
MATRIX CORRELATION
===============================================================================
"""    

TTcorr=TTc.drop(["DATE"],axis=1)
print("=========================================================")
print("Correlation Matrix")
print(TTcorr.corr(method="pearson"))
print("=========================================================")
"""
===============================================================================
PROBABILITY of RAIN
===============================================================================
"""   

R=TTc[TTc["RAIN"]>0]["RAIN"].count()

print("=========================================================")
print("Probability of rain in the data =")
print(R/L)
print("=========================================================")
    
  
"""
===============================================================================
FOURIER
===============================================================================
"""           
#Number of Sample points
N=len(x)
# Sample spacing
T=360

freq=scipy.fftpack.fftfreq(int(T/2))
i=freq>0
plt.figure(3)
plt.title("Fourier Transform T. Average")   
plt.plot(freq[i],10*np.log10(TTa[:,5][2*int(T/2):3*int(T/2)][i]),color="m")
plt.xlabel("Freq")

plt.savefig('Fourier', format='eps',dpi=1200)


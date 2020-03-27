#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import numpy as np
import matplotlib.pylab as plt
import readcol
import itertools as it
from itertools import tee
import pandas as pd
import warnings
import decimal
# Loading files
Hfiles = readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/highres/cptmarvel.test.orbit')
Ffiles =  readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/fatso/cptmarvel.fatso.orbit')

# DATA
# Convertions
m_sol= 2.31e15
l_kpc  = 25000
m_g = 1.989e33
l_cm = 3.086e21
timee = 38.78
d_timee = 1.22386438e18
t_square = 1.49784401e36
         
# Highes Accretion
Denergy =( Hfiles[:,13]* m_sol*( l_kpc**2) *m_g *(l_cm**2))/t_square
Dtime = Hfiles[:,14]*d_timee
dEdt = Denergy/Dtime
Time =((Hfiles[:,1]-1.0)*timee)*1e9

# Functions

def pair(iterable):
    "c -> (c0,c1), (c1,c2), (c2, c3), ..." # This function creates ordered pairs 
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def float_range(start, stop, step):
  while start < stop:                 # Float Range function 
    yield float(start)
    start += decimal.Decimal(step)

def medians(Time,dEdt,intervals):          
    out = []                          # Calculate median valuea given intervals
    warnings.simplefilter("ignore")
    np.mean(out)

    for tmin, tmax in intervals:
        mask = (Time >= tmin) & (Time < tmax)
        out.append(np.median(dEdt[mask]))
    return np.array(out)

#i = pair(range(8,16,1))
#print(i)


intervals = pair(float_range(0,3,0.25))
centers = [(tmin+tmax)/2. for tmin, tmax in intervals]
#print (intervals )
#print(centers)
#print(medians(Time, dEdt, intervals))


plt.plot(centers, medians(Time,dEdt,intervals), 'ko')
plt.ylim(10e30,10e40)
plt.show()

'''
# OLD CODE

df = pd.DataFrame({'Time': Time, 'dEdt': dEdt})
data_cut = pd.cut(df.Time,intervals)
grp = df.groupby(by = data_cut)
ret = grp.aggregate(np.median)
plt.title(" $\Delta$E/$\Delta$t vs Time")
plt.plot(i, ret.dEdt,'ko', label=('Highres Simulation')) # highres
#plt.scatter(Time, dEdt)
plt.legend(loc = 'upper right')
plt.xlabel("Time(Gyrs)")
plt.ylabel("$\Delta$E/$\Delta$t(Erg/s)")
plt.yscale('log')
plt.ylim(10e30,10e40)
plt.xlim(0,3)
plt.show()
#plt.savefig("Accretion_highres.png")

'''

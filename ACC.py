#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import numpy as np
import matplotlib.pylab as plt
import readcol
import pandas as pd

## Loading Files

Hfiles = readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/highres/cptmarvel.test.orbit')
Sfiles = readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/smallsoft/cptmarvel.smallsoft.orbit')
ASfiles = readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/allsmallsoft/cptmarvel.tinysoft.orbit')
Ffiles =  readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/fatso/cptmarvel.fatso.orbit')
Rfiles =  readcol.readcol('/media/jillian/h229/supersample/h229.2.iso.orbit')

# Convertions
m_sol= 2.31e15
l_kpc  = 25000
m_g = 1.989e33
l_cm = 3.086e21
timee = 38.78
d_timee = 1.22386438e18
t_square = 1.49784401e36
# Highes Accretion
start = 0
n = 8
stop = 0.08*timee
bins = np.linspace(start,stop,n)
Denergy =( Hfiles[:,13]* m_sol*( l_kpc**2) *m_g *(l_cm**2))/t_square
Dtime = Hfiles[:,14]*d_timee
dEdt = Denergy/Dtime
Time =(Hfiles[:,1]-1.0)*timee

df = pd.DataFrame({'Time': Time, 'dEdt': dEdt})
data_cut = pd.cut(df.Time,bins)
grp = df.groupby(by = data_cut)
ret = grp.aggregate(np.median)
plt.title(" $\Delta$E/$\Delta$t vs Time")
plt.plot(ret.Time, ret.dEdt,'ko', label=('Highres')) # highres
#plt.scatter(Time, dEdt)
plt.legend(loc = 'upper right')
plt.xlabel("Time(Gyrs)")
plt.ylabel("$\Delta$E/$\Delta$t(Erg/s)")
plt.yscale('log')
plt.ylim(10e32,10e44)
plt.legend(loc = 'upper left')
plt.show()
plt.savefig("Accretion_highres.png")


# SMALLSOFT Accretion
DE = (Sfiles[:,13]* m_sol* (l_kpc**2) *m_g *(l_cm**2)) / t_square
DT = Sfiles[:,14]*d_timee
DE_DT = DE/DT
time = (Sfiles[:,1]-1)*timee
plt.title("$\Delta$E/$\Delta$t vs Time")
plt.scatter(time,DE_DT, c='g' ,label='SmallSoft' )
plt.xlabel("Time(Gyrs)")
plt.ylabel("$\Delta$E/$\Delta$t(Erg/s)")
plt.yscale('log')
plt.legend(loc = 'upper center')
plt.ylim(10e32,10e44)
plt.savefig("Accretion_smallsoft.png")
plt.show()

# ALLSOMALLSOFT Accretion
De = (ASfiles[:,13]* m_sol* (l_kpc**2) *m_g *(l_cm**2))/ t_square
Dt = ASfiles[:,14]*d_timee
de_dt = De/Dt
t = (ASfiles[:,1]-1.0)*timee

plt.title("$\Delta$E/$\Delta$t vs Time")
#plt.plot(retr.t, retr.de_dt,'bo', label=('AllSmallSoft Simulation')) # ALLSMALLSOFT
plt.scatter(t,de_dt, c='b', label=("AllSmallSoft"))
plt.xlabel("Time(Gyrs)")
plt.ylabel("$\Delta$E/$\Delta$t(Erg/s)")
plt.yscale('log')
plt.legend(loc = 'upper right')
plt.ylim(10e32,10e44)
plt.show()
plt.savefig("Accretion_allsmallsoft.png")

# FATSO Accretion
DENERGY = (Ffiles[:,13]* m_sol* (l_kpc**2) *m_g *(l_cm**2)) / t_square
DTIME = Ffiles[:,14]*d_timee
DE__DT = DENERGY/DTIME
TI = (Ffiles[:,1]-1.0)*timee

plt.title("$\Delta$E/$\Delta$t vs Time")
plt.scatter(TI,DE__DT, c ='r', label= 'Fatso')
#plt.plot(rt.TI, rt.DE__DT,'ro', label=('FATSO Simulation')) # FATSO
plt.xlabel("Time(Gyrs)")
plt.ylabel("$\Delta$E/$\Delta$t(Erg/s)")
plt.yscale('log')
plt.ylim(10e26,10e42)
plt.show()
plt.savefig("Accretion_FATSO.png")

# RUTH Accretion

D_E = (Rfiles[:,13]* m_sol* (l_kpc**2) *m_g *(l_cm**2))/ t_square
D_T = Rfiles[:,14]*d_timee
de_dt = D_E/D_T
TiMe = (Rfiles[:,1]-1.0)*timee
'''
R = pd.DataFrame({'TiMe': TiMe, 'de_dt': de_dt})
Rcut = pd.cut(R.TiMe,B)
g = R.groupby(by = Rcut)
r = g.aggregate(np.median)
'''
plt.title("$\Delta$E/$\Delta$t vs Time")
plt.scatter(TiMe, de_dt, c ='m', label= 'Ruth')
#plt.plot(r.TiMe, r.de_dt,'mo', label=('RUTH Simulation')) # RUTH
plt.xlabel("Time(Gyrs)")
plt.ylabel("$\Delta$E/$\Delta$t(Erg/s)")
plt.yscale('log')
plt.ylim(10e32,10e42)
plt.show()
plt.savefig("Accretion_RUTH.png")

# H,S,A
plt.title("$\Delta$E/$\Delta$t vs Time")
plt.plot(ret.Time, ret.dEdt,'ko', label=('Highres Simulation')) 
plt.scatter(time,DE_DT, c='g', label= ("SmallSoft Simulation") )
plt.scatter(t,de_dt, c='b', label = "AllSmallSoft Simulation")
plt.xlabel("Time(Gyrs)")
plt.ylabel("$\Delta$E/$\Delta$t (Erg/s)")
plt.yscale('log')
plt.ylim(10e32,10e44)
plt.show()
plt.savefig("Accretion_plots.png")

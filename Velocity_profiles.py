import pynbody
import numpy as np 
import pandas as pd
import matplotlib.pylab as plt
from matplotlib.ticker import NullFormatter
import readcol
# -*- coding: utf-8 -*-
#Loading the file 
s = pynbody.load("cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std")
s.physical_units()

# Function to find a Black Hole
# input 
def findBH(s):  
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)

maxr= 2
nbins=50

pynbody.analysis.angmom.faceon(s)
#profile stars
pstars = pynbody.analysis.profile.Profile(s.s, min=0.1, max=maxr, nbins=nbins, ndim=3)
#profile dark matter
pdarkm = pynbody.analysis.profile.Profile(s.d, min=0.1, max=maxr, nbins=nbins, ndim=3, type= 'log')
#profile gas
pgas = pynbody.analysis.profile.Profile(s.g, min=0.1, max=maxr, nbins=nbins, ndim=3, type= 'log')
#profile for star, gas and dark matter
pall  = pynbody.analysis.profile.Profile(s, min=0.1, max=maxr, nbins=nbins, ndim=3, type= 'log')

f, axs = plt.subplots(1,4, figsize=(14,6))

# plot the star profile
axs[0].plot(pstars['rbins'].in_units('kpc'),pstars['vr_disp'].in_units('km s^-1'),'k')
axs[0].semilogx()
axs[0].semilogy()
axs[0].set_xlabel('R [kpc]')
axs[0].set_ylabel('$\sigma_{r}$')
axs[0].set_title("Velocity Stars vs Radius ")

# plot the dark matter profile
axs[1].plot(pdarkm['rbins'].in_units('kpc'),pdarkm['vr_disp'].in_units('km s^-1'),'k')
axs[1].semilogx()
axs[1].semilogy()
axs[1].set_xlabel('R [kpc]')
axs[1].set_ylabel('$\sigma_{r}$')
axs[1].set_title("Velocity Dark Matter vs Radius ")

#plot the gas profile
axs[2].plot(pgas['rbins'].in_units('kpc'),pgas['vr_disp'].in_units('km s^-1'),'k')
axs[2].semilogx()
axs[2].semilogy()
axs[2].set_xlabel('R [kpc]')
axs[2].set_ylabel('$\sigma_{r}$')
axs[2].set_title("Velocity Gas vs Radius ")

#plot the total profile
axs[3].plot(pall['rbins'].in_units('kpc'),pall['vr_disp'].in_units('km s^-1'),'k')
axs[3].semilogx()
axs[3].semilogy()
axs[3].set_xlabel('R [kpc]')
axs[3].set_ylabel('$\sigma_{r}$')
axs[3].set_title(" Total Velocity vs Radius ")
    
plt.savefig("profiles.png")
plt.show()

# Profiles source: https://pynbody.github.io/pynbody/tutorials/profile.html

f, axs = plt.subplots(1,4, figsize=(14,6))

# plot the star profile
axs[0].plot(pstars['rbins'].in_units('kpc'),pstars['v_circ'].in_units('km s^-1'),'k')
axs[0].semilogx()
axs[0].semilogy()
axs[0].set_xlabel('R [kpc]')
axs[0].set_ylabel('$\sigma_{r}$')
axs[0].set_title("Velocity Stars vs Radius ")

# plot the dark matter profile
axs[1].plot(pdarkm['rbins'].in_units('kpc'),pdarkm['v_circ'].in_units('km s^-1'),'k')
axs[1].semilogx()
axs[1].semilogy()
axs[1].set_xlabel('R [kpc]')
axs[1].set_ylabel('$\sigma_{r}$')
axs[1].set_title("Velocity Dark Matter vs Radius ")

#plot the gas profile
axs[2].plot(pgas['rbins'].in_units('kpc'),pgas['v_circ'].in_units('km s^-1'),'k')
axs[2].semilogx()
axs[2].semilogy()
axs[2].set_xlabel('R [kpc]')
axs[2].set_ylabel('$\sigma_{r}$')
axs[2].set_title("Velocity Gas vs Radius ")

#plot the total profile
axs[3].plot(pall['rbins'].in_units('kpc'),pall['v_circ'].in_units('km s^-1'),'k')
axs[3].semilogx()
axs[3].semilogy()
axs[3].set_xlabel('R [kpc]')
axs[3].set_ylabel('$\sigma_{r}$')
axs[3].set_title(" Total Velocity vs Radius ")
    
plt.savefig("profiles.png")
plt.show()

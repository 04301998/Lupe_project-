#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import numpy as np
import matplotlib.pylab as plt
import readcol

Path = "/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/fatso/"
files = readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/fatso/files.list')
all_files = files[:,0]

# FUNCTION TO FIND A BLACK HOLE
def findBH(s):  
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

for i in all_files:
    s = pynbody.load(Path + i)
    s.physical_units()
    #BH = findBH(s)
    pynbody.analysis.angmom.faceon(s)
    maxr= 2
    nbins = 60
    #stars = s.stars[np.where(s.stars["tform"]>0)]
    beta = pynbody.analysis.profile.Profile(s.stars[np.where(s.stars["tform"]>0)], min=0.1, max=maxr, nbins=nbins, ndim=3, type= 'lin')
    
    # plot the profile
    plt.plot(beta['rbins'].in_units('kpc'),beta['beta'],'b', label = "With Bh")
    plt.xlabel('Radius [kpc]')
    plt.ylabel('Velocity Anisotropy ($\\beta$)')
    plt.ylim(-.4, 0.8)
    plt.title("Velocity Anisotropy vs Radius ")
    plt.legend(loc = 'upper right')
    plt.savefig(i +"Fatso_beta.png")
    plt.close()
   #plt.show() 

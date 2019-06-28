import pynbody
import numpy as np 
import pandas as pd
import matplotlib.pylab as plt 
import readcol
import astropy.units as u 
# -*- coding: utf-8 -*- 

# Loading the file 
s = pynbody.load("cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std")

s.physical_units()

# Function to find a Black Hole
# input 
def findBH(s):  
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
#Print the black hole
#print(BH)

# VELOCITY OF THE GALAXY
galaxy = s['vel']
Galaxy_vx = galaxy[:,0]
Galaxy_vy = galaxy[:,1]
Galaxy_vz = galaxy[:,2]
mass = s['mass']

# AVERAGE VELOCITY
Av_Vx = np.sum(Galaxy_vx*mass)/(np.sum(mass))
#print(Av_Vx)
Av_Vy = np.sum(Galaxy_vy*mass)/(np.sum(mass))
#print(Av_Vy)
Av_Vz = np.sum(Galaxy_vz*mass)/(np.sum(mass))
#print(Av_Vz)

# BLACK HOLE VELOCITY
BH_x = Av_Vx - BH['vel'][:,0]
#print(BH_x)
BH_y= Av_Vy - BH['vel'][:,1]
#print(BH_y)
BH_z= Av_Vz - BH['vel'][:,2]
#print(BH_z)

magnitude = np.sqrt((BH_x)**2 + (BH_y)**2 + (BH_z)**2)
print(magnitude)


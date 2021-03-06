# find starts near the black hole.measure their velocities(make a histogram, find the averas(0.5 kpc). HInt. pynbody sphere code.

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

radius = 0.5
#center = (-634.00464133, 1258.07020815, 29.86851614)

stars = s.stars[0:]

# Find the number of stars around the black hole
Sphere = stars[pynbody.filt.Sphere(radius, cen = (-634.00464133, 1258.07020815, 29.8685161))]
#print(Sphere)
stars_BH = len(Sphere)
print(stars_BH)
starsv = Sphere['vel']

#print(stars v)
# Velocity of the stars
vel_1 = np.array([vel[0] for vel in starsv])
vel_2 = np.array([vel[1] for vel in starsv])
vel_3 = np.array([vel[2] for vel in starsv])

print(vel_1)
print(vel_2)
print(vel_3)
print(Sphere['vel'].units)

#magnitude = np.sqrt((vel_1)**2 + (vel_2)**2 + (vel_3)**2)
#Av_vel =  magnitude.sum()/stars_BH
#print(Av_vel)

V1 = np.abs(vel_1)
V2 = np.abs(vel_2)
V3 = np.abs(vel_3)
magnitude = np.sqrt((V1)**2 + (V2)**2 + (V3)**2)
Average= magnitude.sum()/1773
print(Average)
Av = np.average(magnitude)


print(Av)

#Plotting

plt.figure(1)

# Stars vs Velocity plot in the x-direction
plt.subplot(221)
plt.hist(vel_1, bins= 100)
plt.title('Stars vs Velocity')
plt.xlabel('Velocity1 (km/s)')
plt.ylabel('Number of stars')
plt.legend()
plt.grid(True)

# Stars vs Velocity plot in the y-direction
plt.subplot(222)
plt.hist(vel_2, bins= 100)
plt.title('Stars vs Velocity')
plt.xlabel('Velocity2 (km/s)')
plt.ylabel('Number of stars')
plt.legend()
plt.grid(True)

# Stars vs Velocity plot in the z-direction
plt.subplot(223)
plt.hist(vel_3, bins= 100)
#plt.title('Stars vs Velocity')
plt.xlabel('Velocity3 (km/s)')
plt.ylabel('Number of stars')
plt.legend()
plt.grid(True)
#plt.show()

#pynbody.plot.image(s.d[pynbody.filt.Sphere('5 Mpc')], width='10 Mpc', units = 'Msol kpc^-2', cmap='Greys')
#plt.show()

pynbody.analysis.angmom.faceon(s)
# create an image using  the default bands (i, v, u)
pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='Faceon.png')

# create an image using  the default bands (i, v, u)
pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='Edgeon.png')
plt.show()

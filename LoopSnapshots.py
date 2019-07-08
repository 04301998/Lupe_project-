import pynbody 
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

s = pynbody.load("cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std")
s.physical_units()

# FUNCTION TO FIND A BLACK HOLE
def findBH(s):  
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)

pynbody.analysis.angmom.faceon(s)

def getz(s):
    return s.properties['z']

def gettime(s):
    return pynbody.analysis.cosmoogy.age(s)
# Loading Snapshots
for i in s:
   
    BHposition = BH['pos'] # POSITION OF THE BLACK HOLE
    print(BHposition)
    BHx = BHposition[:,0]
    print(BHx)
    BHy = BHposition[:,1]
    print(BHy)
    BHz = BHposition[:,2]
    print(BHz)
    posi_magnitude = np.sqrt((BHx)**2 + (BHy)**2 + (BHz)**2)
    print("Magnitude position of the Black Hole: ",posi_magnitude)
    print("Position units: ",s['pos'].units)

# VELOCITY OF THE STARS IN THE GALAXY
# How many stars?
number_stars = s.stars[0:]
total_stars = len(number_stars)
# Velocity of the galaxy
galaxy = s['vel']
mass = s['mass']
Galaxy_vx = galaxy[:,0]
Galaxy_vy = galaxy[:,1]
Galaxy_vz = galaxy[:,2]
# Average galaxy velocity
Av_Vx = np.sum(Galaxy_vx*mass)/(np.sum(mass))
Av_Vy = np.sum(Galaxy_vy*mass)/(np.sum(mass))
Av_Vz = np.sum(Galaxy_vz*mass)/(np.sum(mass))
# Find the velocity of the star 
vel_1 = Av_Vx - s.stars['vel'][:,0]
vel_2 = Av_Vy - s.stars['vel'][:,1]
vel_3 = Av_Vz - s.stars['vel'][:,2]
print(" Velocity units: ",s['vel'].units)
magnitude = np.sqrt((vel_1)**2 + (vel_2)**2 + (vel_3)**2)
for i in s:
    Av_vel_stars_in_galaxy =  magnitude.sum()/total_stars
    print("Velocity of stars in the galaxy: ",Av_vel_stars_in_galaxy)

# Find the number of stars around the black hole
stars = s.stars[0:]
radius = 0.5
Sphere = stars[pynbody.filt.Sphere(radius, cen = (0.86460325,-0.36786913,0.1918984))]
#print(Sphere)
stars_BH = len(Sphere)
print("Stars around the Black Hole at 0.5 kpc: ",stars_BH)
starsv = Sphere['vel']

# VELOCITY OF THE STARS AROUND THE BLACK HOLE
for i in s:
    vel_stars1 = Av_Vx - starsv[:,0]
    vel_stars2 = Av_Vy - starsv[:,1]
    vel_stars3 = Av_Vz - starsv[:,2]
    magnitude = np.sqrt((vel_1)**2 + (vel_2)**2 + (vel_3)**2)
    Av_vel_around_BH =  magnitude.sum()/total_stars
    print("Velocity of the stars around the Black Hole  ",Av_vel_around_BH)




#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pynbody 
import numpy as np
import pandas as pd
import readcol
Path = "/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/"
files = readcol.readcol("/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/files.list")
files = files[:,0]
print(files)
# FUNCTION TO FIND A BLACK HOLE
def findBH(s):  
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
#BH = findBH(s) until I define s
def getz(s):
    return s.properties['z']

def gettime(s):
    return pynbody.analysis.cosmology.age(s)
pos=[]
vel=[]
f = open("LoopSnapshots.txt","w+")
f.write("Position,  Velocity \n" )
# Loading Snapshots
for i in files:
    print(i)
    s  = pynbody.load(Path + i)
    s.physical_units()
    BH = findBH(s)
    pynbody.analysis.angmom.faceon(s)
    print(BH)
    BHposition = BH['pos'] # POSITION OF THE BLACK HOLE
    #print(BHposition)
    BHx = BHposition[:,0]
    print(BHx)
    BHy = BHposition[:,1]
    print(BHy)
    BHz = BHposition[:,2]
    print(BHz)
    posi_magnitude = np.sqrt((BHx)**2 + (BHy)**2 + (BHz)**2)
    posi_magni = posi_magnitude[0]
    print("Magnitude position of the Black Hole: ",posi_magnitude)
    print("Position units: ",s['pos'].units)

    # VELOCITY OF THE STARS IN THE GALAXY
    # How many stars?
    number_stars = s.stars[0:]
    total_stars = len(number_stars)
    print("Total number of stars: ", total_stars)
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
    Av_vel_stars_in_galaxy =  magnitude.sum()/total_stars
    print("Velocity of stars in the galaxy: ",Av_vel_stars_in_galaxy)
# Find the number of stars around the black hole
    stars = s.stars[0:]
    radius = 0.5
    Sphere = stars[pynbody.filt.Sphere(radius, cen = (np.array([BHx[0],BHy[0],BHz[0]])))]
    #print(Sphere)
    stars_BH = len(Sphere)
    print("Stars around the Black Hole at 0.5 kpc: ",stars_BH)
    starsv = Sphere['vel']
    # VELOCITY OF THE STARS AROUND THE BLACK HOLE
    x = Av_Vx - starsv[:,0]
    y = Av_Vy - starsv[:,1]
    z = Av_Vz - starsv[:,2]
    magnitude = np.sqrt((vel_1)**2 + (vel_2)**2 + (vel_3)**2)
    Av_vel_around_BH =  magnitude.sum()/total_stars
    
    # VELOCITY OF THE STARS WITH RESPECT OF THE BLACK HOLE
    stars_x = x - BH['vel'][:,0]
    stars_y = y - BH['vel'][:,1]
    stars_z = z - BH['vel'][:,2]

    stars_xyz = np.sqrt((stars_x)**2 + (stars_y)**2 + (stars_z)**2)
    print("Velocity of the stars around the Black Hole with respect of the BH", stars_xyz)
    print("Velocity of the stars around the Black Hole  ",Av_vel_around_BH)
    vel.append(Av_vel_around_BH)
    pos.append(posi_magnitude)
    data = str(posi_magni)+"   "+str(Av_vel_around_BH)+"\n" 
    
    f.write(data)
    
    print(data)

f.close()

    
numbers = np.array([1,2,10,20])*0.194

# Plot Velocity
plt.axes()
plt.title("Velocity vs Time")
plt.plot(numbers, vel)
plt.tick_params(axis ="x", labelcolor="r")
plt.xlabel("Time(Gyr)")
plt.ylabel("Velocity(km/s)")
plt.legend()
plt.show()
# Plot Position
plt.title("Position vs Time")
plt.plot(numbers, pos)
plt.tick_params(axis = "x", labelcolor="b")
plt.xlabel("Time(Gyr)")
plt.ylabel("Position(kpc)")
plt.legend()
plt.show()
'''
    pynbody.analysis.angmom.faceon(s)
python    # create an image using  the default bands (i, v, u)
    pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='halo11Faceon.png')

    # create an image using  the default bands (i, v, u)
    pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='halo11Edgeon.png')
    plt.show()
'''

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import numpy as np
import matplotlib.pylab as plt
import readcol

Path = "/media/jillian//cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/nobh/"
files = readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/nobh/files.list')

all_files = files[:,0]
filesBH = readcol.readcol('/home/lupe/Lupe_project-/highres.txt', skipline=1)
radius_influence = np.array(filesBH[:,6])
radius = radius_influence.astype(np.float)
BHx_direction = np.array(filesBH[:,2])
BHx = BHx_direction.astype(np.float)
BHy_direction = np.array(filesBH[:,3])
BHy = BHy_direction.astype(np.float)
BHz_direction = np.array(filesBH[:,4])
BHz = BHz_direction.astype(np.float)

f = open("velocity_without_BH.txt","w+")
f.write("Velocity of stars in the galaxy without a BH '\n")
j = 0
for i in all_files:
    a = pynbody.load(Path + i)
    a.physical_units()
    pynbody.analysis.halo.center(a)
    number_stars = a.stars[0:]
    total_stars = len(number_stars)
    #Find velocity of the stars
    stars = a.stars#['vel']
    starsv = a.stars['vel']
    # Velocity 
    vel_1 = np.array([vel[0] for vel in starsv])
    vel_2 = np.array([vel[1] for vel in starsv])
    vel_3 = np.array([vel[2] for vel in starsv])
    magnitude = np.sqrt((vel_1)**2 + (vel_2)**2 + (vel_3)**2)
    Av =  magnitude.sum()/total_stars
    #print(Av)
    
    SPHER = pynbody.filt.Sphere(radius[j], cen = np.array([BHx[j],BHy[j],BHz[j]]))
    print(SPHER)
    #insphere = SPHERE[0]
    in_sphere = stars[SPHER]
    tot_stars = len(in_sphere)
    print("Stars in sphere", tot_stars)

    # Find velocity of the stars in the sphere
    velocity = in_sphere['vel']
    # Find velocity of the stars in all direction (x,y,z)
    x = in_sphere['vel'][:,0]
    y = in_sphere['vel'][:,1]
    z = in_sphere['vel'][:,2]

    vel_mag = np.sqrt((x)**2 + (y)**2 + (z)**2)
    VELOCITY = vel_mag.sum()/tot_stars
    print("Velocity stars in sphere",VELOCITY)


    j = j+1
    data = str(Av)+" "+str(VELOCITY)
    print(data)
    f.write(data+'\n')

f.close()

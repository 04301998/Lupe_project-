#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import numpy as np
import matplotlib.pylab as plt
import readcol
'''
r = (G * BH_Mass) / (stars_vel**2)
G = 6.674e-11
'''
#Now I need a code that will load the snapshots(s will stand for )
Path = "/media/jillian//cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/"
files = readcol.readcol('/media/jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/supersample/files.list')
all_files = files[:,0]

#Tell where BH is Function
def findBH(s):
    BH = s.stars[pynbody.filt.LowPass('tform', 0.0)]
    return BH

#std stands for standard deviation (velocity dispersion)
def DispersionVelocity(s):
    velocity = s.stars['vel']
    x = np.std(velocity[0])
    y = np.std(velocity[1])
    z = np.std(velocity[2])
    #print(x_direct)
    #print(y_direct)
    #print(z_direct)
    dispersion_velocity = np.sqrt( (x)**2 + (y)**2 + (z)**2)
    print("Dispersion velocity: ",dispersion_velocity)
    return dispersion_velocity

#Need my units to match up so the calculations go correctly
#Couldn't find a way to convert G, so i converted everything else and then converte back to KPC
def RadInfluence(s):
    G = 6.674e-11
    #G is in m**3 * kg**-1 * s**-2
    BH = findBH(s)
    BH_Mass = BH['mass'].in_units('kg')
    #Kg mtches kg in G
    stars_vel = DispersionVelocity(s) * 1e3
    r = (G * BH_Mass) / (stars_vel**2)
    return r * 3.24e-20*3
#Finally converted back to KPC (the conversion is * 3.24e-20)   
for i in all_files:
    s = pynbody.load(Path + i)
    s.physical_units()
    #Don't forget to center the galaxy with this
    pynbody.analysis.angmom.faceon(s)
    BH = findBH(s)
    BH_pos = BH['pos']
    BHx = BH_pos[:,0]
    BHy = BH_pos[:,1]
    BHz = BH_pos[:,2]
    BH_position = np.array([BHx[0], BHy[0], BHz[0]])
    Mass_Msol = BH['mass']
    #print(BH_pos)
    #dispersion = DispersionVelocity(s)
    #print(dispersion)
    #The radius here is an array, we need the center to be an integer
    radius = RadInfluence(s)
    radius_influence = radius[0]
    print(radius)
    #BH_pos is a three int array so it will be the center
    sphere = pynbody.filt.Sphere(radius_influence, cen = BH_position)
    #print(sphere)
    stars = s.stars[np.where(s.stars["tform"]>0)]
    in_sphere = stars[sphere]
    total_stars = len(in_sphere)
    print("Total stars: ",total_stars)
    #This code tells us how many stars are in this section
    num_of_stars = s.stars[0:]
    in_sphere = num_of_stars[sphere]
    #This is how many stars there are
    total_stars = len(in_sphere)
    #This find their velocity
    velocity = in_sphere['vel']
    #Now we need to find the velocity of these stars in x,y,z
    x = np.array([vel[0] for vel in velocity])
    y = np.array([vel[1] for vel in velocity])
    z = np.array([vel[2] for vel in velocity])
    #Now we can find the average of these by dividing by the total
    vel_answer = np.sqrt((x)**2 + (y)**2 + (z)**2)
    #Now divide by total number of stars
    velocity = vel_answer.sum() / total_stars
    

    # Velocity of the stars with respect of the BH
    stars_BH_X = x - BH['vel'][:,0]
    stars_BH_Y = y - BH['vel'][:,1]
    stars_BH_Z = z - BH['vel'][:,2]
    stars_xyz = np.sqrt((stars_BH_X)**2 + (stars_BH_Y)**2 +(stars_BH_Z)**2)
    stars_magnitude = stars_xyz/total_stars
    print("Velocity of the stars around the BH", stars_magnitude)
    

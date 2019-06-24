import pynbody
import numpy as np 
import pandas as pd
import matplotlib.pylab as plt 
import readcol
# -*- coding: utf-8 -*- 

#Loading the file 
s = pynbody.load("cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.5.std")

s.physical_units()

#Find the velocity if the star 
stars = s.stars['vel']

#How many stars
number_stars = s.stars[0:]
total_stars = len(number_stars)
# Velocity 

vel_1 = np.array([vel[0] for vel in stars])
vel_2 = np.array([vel[1] for vel in stars])
vel_3 = np.array([vel[2] for vel in stars])

# Average Velocity
Av_vel1 = vel_1/total_stars
Av_vel2 = vel_2/total_stars
Av_vel3 = vel_3/total_stars

#print(Av_vel1)
#print(Av_vel2)
#print(Av_vel3)

print(s['vel'].units)

magnitude = np.sqrt((vel_1)**2 + (vel_2)**2 + (vel_3)**2)

print(magnitude)

Av_vel =  magnitude.sum()/total_stars
print(Av_vel)

Average = np.average(magnitude)
print(Average)


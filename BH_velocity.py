import pynbody
import numpy as np 
import pandas as pd
import matplotlib.pylab as plt 
import readcol
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
# Print the black hole
#print(BH)

# Velocity of the galaxy
stars = s.stars[0:]
gas = s.gas[0:]
dark_matter = s.d[0:]
tot_stars = len(stars)
tot_gas = len(gas)
tot_dark_matter = len(dark_matter)
#print(tot_stars)
#print(tot_gas)
#print(tot_dark_matter)

tot_particles = tot_stars + tot_gas + tot_dark_matter

galaxy = s['vel']
starsv = s.stars['vel']
gasv = s.gas['vel']
dark_matterv = s.d['vel']
#print(galaxy)
vel_1 = np.array([vel[0] for vel in galaxy])
vel_2 = np.array([vel[1] for vel in galaxy])
vel_3 = np.array([vel[2] for vel in galaxy])

# Velocity Galaxy
magnitude = np.sqrt((vel_1)**2 + (vel_2)**2 + (vel_3)**2)
Av_vel =  magnitude.sum()/tot_particles 
print(Av_vel)
Average = np.average(magnitude)
print(Average)

# Velocity stars
vel_s_1 = np.array([vel[0] for vel in starsv])
vel_s_2 = np.array([vel[1] for vel in starsv])
vel_s_3 = np.array([vel[2] for vel in starsv])
# Calculate average velocity
magnitude_stars = np.sqrt((vel_s_1)**2 + (vel_s_2)**2 + (vel_s_3)**2)
Av_vel_stars =  magnitude_stars.sum()/tot_stars
print(Av_vel_stars)
Average_stars = np.average(magnitude_stars)
print(Average_stars)

# Velocity gas
vel_g_1 = np.array([vel[0] for vel in gasv])
vel_g_2 = np.array([vel[1] for vel in gasv])
vel_g_3 = np.array([vel[2] for vel in gasv])
# Calculate average velocity
magnitude_gas = np.sqrt((vel_g_1)**2 + (vel_g_2)**2 + (vel_g_3)**2)
Av_vel_gas =  magnitude_gas.sum()/tot_gas
print(Av_vel_gas)
Average_gas = np.average(magnitude_gas)
print(Average_gas)
#print(s['vel'].units)

# Velocity dark matter
``vel_dm_1 = np.array([vel[0] for vel in dark_matterv])
vel_dm_2 = np.array([vel[1] for vel in dark_matterv])
vel_dm_3 = np.array([vel[2] for vel in dark_matterv])
# Calculate average velocity
magnitude_dm = np.sqrt((vel_dm_1)**2 + (vel_dm_2)**2 + (vel_dm_3)**2)
Av_vel_dm =  magnitude_dm.sum()/tot_dark_matter
print(Av_vel_dm)
Average_dm = np.average(magnitude_dm)
print(Average_dm)

# Black Hole velocity 
BH_v = BH['vel']
vel_bh1 = np.array([vel[0] for vel in BH_v])
vel_bh2 = np.array([vel[1] for vel in BH_v])
vel_bh3 = np.array([vel[2] for vel in BH_v])
# Calculate average velocity
magnitude_bh = np.sqrt((vel_bh1)**2 + (vel_bh2)**2 + (vel_bh3)**2)

Av_vel_bh =  magnitude_bh
print(Av_vel_bh)
Average_bh = np.average(magnitude_bh)
print(Average_bh)


BH_vel = Average - Average_stars - Average_gas - Average_dm
print(BH_vel)



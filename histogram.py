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
print(stars)
number_stars = s.stars[0:]
total_stars = len(number_stars)
# Velocity 

print(number_stars)
print(total_stars)

vel_1 = np.array([vel[0] for vel in stars])
vel_2 = np.array([vel[1] for vel in stars])
vel_3 = np.array([vel[2] for vel in stars])

print(vel_1)

plt.hist(vel_1, bins= 60)
plt.title('Stars vs Velocity')
plt.xlabel('Velocity1 (km/s)')
plt.ylabel('Number of stars')
plt.legend()
plt.grid(True)
plt.show()


plt.hist(vel_2, bins=30)
plt.title('Stars vs Velocity')
plt.xlabel('Velocity2 (km/s)')
plt.ylabel('Number of stars')
plt.legend()
plt.grid(True)
plt.show()

plt.hist(vel_3, bins=20)
plt.title('Stars vs Velocity')
plt.xlabel('Velocity3 (km/s)')
plt.ylabel('Number of stars')
plt.legend()
plt.grid(True)
plt.show()

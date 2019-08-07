#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import pynbody
import pylab
import numpy as np
import matplotlib.pylab as plt
import readcol
# Loading files
filesBH = readcol.readcol('/home/lupe/Lupe_project-/velocity_with_BH.txt')
files = readcol.readcol('/home/lupe/Lupe_project-/velocity_without_BH.txt')
FILESBH = readcol.readcol('/home/lupe/Lupe_project-/highres.txt', skipline=1)
file_ss = readcol.readcol('/home/lupe/Lupe_project-/smallsoft.txt', skipline=1)
F =  readcol.readcol('/home/lupe/Lupe_project-/smallsoft_vel_withoutBH.txt', skipline=1)
# Find velocities of the stars in the galaxy with BH and whitout BH
# Vel stars in the galaxy With BH
vel_starsBH = np.array(filesBH[:,0])
vel_stars = vel_starsBH.astype(np.float)
#Vel stars in the galaxy without BH
v_stars = np.array(files[:,0])
VEL_STARS =  v_stars.astype(np.float)
# Find velocities of the stars in the sphere of influence with BH and without BH
# vel stars in the sphere of influence with BH
vel_stars_sphereBH = np.array(FILESBH[:,7])
VelStarsSphereBH = vel_stars_sphereBH.astype(np.float)
# Vel stars in the sphere of influence without BH
vel_stars_sphereNoBH = np.array(files[:,1])
VelStarsSphereNoBH = vel_stars_sphereNoBH.astype(np.float)
# NEW SIMULATION "SMALL SOFT" with a BH
#Sphere of influence of new simulation with BH
VelStarsS_sphere = np.array(file_ss[:,6])
veStarsSS = VelStarsS_sphere.astype(np.float)
Ve = np.array(F[:,1])
V= Ve.astype(np.float)
#Velocity of the stars in the entire galaxy with new simulation
VelstarsSS = np.array(file_ss[:,7])
VelstarsS = VelstarsSS.astype(np.float)
# Radius of influence
Rad = np.array(FILESBH[:,6])
R = Rad.astype(np.float)
Radi = np.array(file_ss[:,5])
Radius = Radi.astype(np.float)
# Snapshots with BH
time = np.arange(164)*0.194/10
# Snapshots without BH
TIME = np.arange(152)*0.194/10
# Snapshots of the new simulation
Time = np.arange(156)*0.194/10
# Radius of influence vs Time
plt.title("Radius of Influence vs Time") 
plt.plot(time,R,'b',label= 'First Simulation')
plt.plot(Time,Radius,'r',label= 'New High Resolution Simulation')
plt.xlabel("Time( Gyrs)" )
plt.ylabel("Radius of Influence (Kpc)")
#plt.tick_params(axis="x", color="black")
plt.legend()
plt.savefig("RadiusInfluence.png")
plt.show()

# Velocity stars in the Galaxy with BH 
plt.title("Velocity of the stars in the Galaxy with BH and without BH vs Time") 
plt.plot(time,vel_stars,'b',label= 'WITH BH')
plt.plot(TIME,VEL_STARS,'r',label= 'WITHOUT BH')
plt.plot(Time,VelstarsS,'g',label= 'New High Resolution Simulation with BH' )
plt.xlabel("Time( Gyrs)" )
plt.ylabel("Velocity stars in galaxy (Km/s)")
#plt.tick_params(axis="x", color="black") 
plt.legend()
plt.savefig("VelocityOfStars.png")
plt.show()

# Velocity stars in the sphere of influence with BH and without BH
plt.title("VELOCITY OF THE STARS IN THE SPHERE OF INFLUENCE WITH BH AND WITHOUT BH vs TIME") 
plt.plot(time,VelStarsSphereBH,'b',label= 'WITH BH')
plt.plot(TIME,VelStarsSphereNoBH,'r',label= 'WITHOUT BH')
plt.plot(Time,veStarsSS,'g',label='SmallSoft(High Resolution) with BH')
plt.plot(TIME,V,'m',label='SmallSoft without BH')
plt.xlabel("Time( Gyrs)" )
plt.ylabel("Velocity stars in sphere of influence (Km/s)")
#plt.tick_params(axis="x", color="black")
plt.legend()
plt.savefig("VelocityOfStarsInSphere.png")
plt.show()


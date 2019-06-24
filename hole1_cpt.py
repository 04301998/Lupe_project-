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
print(BH)

BHposition=BH['pos']
print(BHposition)

# x-values
BHx = BHposition[:,0]
print(BHx)

# y-values
BHy = BHposition[:,1]
print(BHy)

#z-values
BHz = BHposition[:,2]
print(BHz)

pos_magnitude = np.sqrt((BHx)**2 + (BHy)**2 + (BHz)**2)
print(pos_magnitude)
print(s['pos'].units)

mass_BH =(BH['mass'],BH['mass'].units)
print(mass_BH)
pynbody.analysis.angmom.faceon(s)

# create an image using  the default bands (i, v, u)
#pynbody.plot.stars.render(s,width= '10 kpc',plot=True,ret_im=True,filename='Faceon.png')


# create an image using  the default bands (i, v, u)
#pynbody.plot.stars.render(s,width= '10 kpc',plot=True,ret_im=True,filename='Edgeon.png')
#plt.show()


# create an image using  the default bands (i, v, u)
pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='Faceon.png')


# create an image using  the default bands (i, v, u)
pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='Edgeon.png')
plt.show()

import readcol
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

files = readcol.readcol('times.list')
redshift = files[:,0]
time = files[:,1]


plt.plot(time,redshift)
plt.tick_params(axis="x",labelcolor="r")
plt.xlabel("Time")
plt.ylabel("Redshift")
plt.legend()
plt.show()

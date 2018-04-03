# -*- coding: utf-8 -*-
"""
Recreating ankle work loop data in Python.
Translated from Matlab syntax
Last edit by JRM 4/2/2018
"""
#import numpy and matlib libraries as shortcuts. now np.CMD and M.CMD will be used instead of numpy. or numpy.matlib.
import numpy as np   #importing the numpy package and functions as np
import numpy.matlib as M    #importing the matlib package and functions as M
import matplotlib.pyplot as plt   #importing plotting package and functions as plt
from scipy import integrate   #import the integrate function
#create an array of slopes and then sort from -9 to 9
slopes = np.array([-9,3,-6,-3,6,0,9])
slopes.sort()
#create % and time x axes vectors
x = np.arange(1, 101, 1, dtype=int)   
time_vector = np.zeros((100,1))
time = np.arange(0.01,1.01,0.01, dtype=float)
#preallocate array for AnklePowerRight with zeros, length=100 (0-99)
AnklePowerRight = np.zeros((100,len(slopes)+1))
AnkleWorkArray = np.zeros((99,len(slopes)))
AnkleWork = np.zeros((len(slopes),1))
for j in range(len(time)):
        time_vector[j]=[time[j]]
        AnklePowerRight[j,0]=time_vector[j]
#file import
for slope in range(len(slopes)):
    filename = 'AvgAnklePower_Right_125_' + str(slopes[slope]) + 'deg.ascii'
    f = open(filename, 'r')
#initiate index
    i=0
#loop through the data file being read in line 15 and assign each line to an index
    for line in f:
        AnklePowerRight[i,slope+1] = np.array(line)
        i=i+1
#integrate ankle power to get ankle work
    AnkleWorkArray[:,slope] = integrate.cumtrapz(AnklePowerRight[:,slope+1],AnklePowerRight[:,0])  
    AnkleWork[slope,0] = AnkleWorkArray[-1,slope]
#plot ankle power as a line plot
    plt.plot(x, AnklePowerRight[:,slope+1])

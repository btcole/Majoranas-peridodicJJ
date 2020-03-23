import numpy as np
import matplotlib.pyplot as plt

import majoranas.modules.constants as const
import majoranas.modules.lattice as lat
import majoranas.modules.operators as op

R = 20

coor = lat.halfdisk(R)
NN = lat.NN_Arr(coor)
NNk = lat.NN_Bound(NN, coor)


#This is to see if the nearest neighbor array is working correctly
idx = 0
print(NN[idx, 0], NN[idx, 1], NN[idx, 2], NN[idx, 3])
plt.scatter(coor[:, 0],coor[:, 1] ,c = 'b')
plt.scatter(coor[idx, 0],coor[idx, 1], c = 'r')
if NN[idx, 0] != -1:
    plt.scatter(coor[NN[idx, 0], 0], coor[NN[idx, 0], 1], c = 'g')
if NN[idx, 1] != -1:
    plt.scatter(coor[NN[idx,1], 0], coor[NN[idx, 1], 1], c = 'magenta')
if NN[idx, 2] != -1:
    plt.scatter(coor[NN[idx,2], 0], coor[NN[idx, 2], 1], c = 'purple')
if NN[idx, 3] != -1:
    plt.scatter(coor[NN[idx,3], 0], coor[NN[idx, 3], 1], c = 'cyan')

plt.xlim(0, max(coor[:,0])+1)
plt.ylim(-1, max(coor[:,1])+1)
plt.show()

#This is to see if the nearest neighbor boundary array is working correctly
idx = 0
print(NN[idx, 0], NN[idx, 1], NN[idx, 2], NN[idx, 3])
plt.scatter(coor[:, 0],coor[:, 1] ,c = 'b')
plt.scatter(coor[idx, 0],coor[idx, 1], c = 'r')
if NNk[idx, 0] != -1:
    plt.scatter(coor[NNk[idx, 0], 0], coor[NNk[idx, 0], 1], c = 'g')
if NNk[idx, 1] != -1:
    plt.scatter(coor[NNk[idx,1], 0], coor[NNk[idx, 1], 1], c = 'magenta')
if NNk[idx, 2] != -1:
    plt.scatter(coor[NNk[idx,2], 0], coor[NNk[idx, 2], 1], c = 'purple')
if NNk[idx, 3] != -1:
    plt.scatter(coor[NNk[idx,3], 0], coor[NNk[idx, 3], 1], c = 'cyan')

plt.xlim(0, max(coor[:,0])+1)
plt.ylim(-1, max(coor[:,1])+1)
plt.show()


''' 
 * GameOfLife.py
 *
 *   Created on:         10.11.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import Universe     as un
import ClusterSpace as cs
import SpaceCluster as sc
import Reality      as rt
import Patterns     as pt
from Enums import *

#import matplotlib.pyplot as plt


USE_CLUSTER_SPACE = True

if __name__ == '__main__':

    if USE_CLUSTER_SPACE:
        mySpace    = cs.ClusterSpace()
    else:
        mySpace    = sc.SpaceCluster()

    myUniverse = un.Universe( mySpace )
    myReality  = rt.Reality( myUniverse )

    print("Initial live cells:")
    #for cell in pt.glider: #
    for cell in pt.collider:
        myUniverse.create_LiveCell_if_Coord_is_Void_or_Dead( cell )
        print( cell)

    
    myReality.update(32)



''' END '''


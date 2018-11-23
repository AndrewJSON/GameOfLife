
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

import matplotlib.pyplot as plt


def add_offset_to_positions( _pos, _offset ):
    # Since an 2D array is used for matplotlib graphics, ...
    # ... coords must not be negative.

    offsetPositions = []
    for pos in _pos:
        offsetPositions.append( pos + _offset ) 

    return offsetPositions

USE_CLUSTER_SPACE = False

if __name__ == '__main__':

    if USE_CLUSTER_SPACE:
        mySpace    = cs.ClusterSpace()
    else:
        mySpace    = sc.SpaceCluster()

    myUniverse = un.Universe(mySpace)
    myReality  = rt.Reality()

    offsetPattern = add_offset_to_positions( pt.glider, (10+5j) )

    print("Initial live cells:")
    for cell in offsetPattern:
        myUniverse.create_LiveCell_if_Coord_is_Void_or_Dead( cell )
        print( cell)

    #lives = myUniverse.getLivePositions()
    #plotCells( lives )

    #plt.ion()

    for i in range(0, 8):
        print("Generation", i)
        myUniverse.update()

        lives = myUniverse.get_CellPositions_of_type_or_all( CellType.LIVE )
        deads = myUniverse.get_CellPositions_of_type_or_all( CellType.DEAD )
        #myReality.plotMatrix( lives )
        myReality.plot_distinct_cells( lives, deads )

    plt.show()
    #myReality.separated_coords_as_lists( lives )


''' END '''



''' 
 * GameOfLife.py
 *
 *   Created on:         10.11.2018
 *   last modified on:   -
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import Universe as un
import Space    as sp
import Reality  as rt
import Patterns as pt
from Enums import *

import matplotlib.pyplot as plt


def add_offset_to_positions( _pos, _offset ):

    offsetPositions = []
    for pos in _pos:
        offsetPositions.append( pos + _offset ) 

    return offsetPositions


if __name__ == '__main__':

    mySpace    = sp.Space()
    myUniverse = un.Universe(mySpace)
    myReality  = rt.Reality()

    offsetPattern = add_offset_to_positions( pt.glider, (10+5j) )

    print("Initial live cells:")
    for cell in offsetPattern:
        myUniverse.create_LiveCell_if_Pos_is_Void_or_Dead( cell )
        print( cell)

    #lives = myUniverse.getLivePositions()
    #plotCells( lives )

    #plt.ion()

    for i in range(0, 8):
        print("Generation", i)
        myUniverse.update()

        lives = myUniverse.getCellPositionsOf( CellType.LIVE )
        whiteSpaces = myUniverse.getCellPositionsOf( CellType.DEAD )
        #myReality.plotMatrix( lives )
        myReality.plot_distinct_cells( lives, whiteSpaces )

    plt.show()
    #myReality.separated_coords_as_lists( lives )


''' END '''


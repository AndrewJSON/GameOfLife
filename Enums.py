
''' 
 * CardinalDirection.py
 *
 *   Created on:         13.06.2017
 *   last modified on:   10.11.2018
 *   Author:             Andrew Jason Bishop
 * 
 * Some general functionalities:
 *   Creates an enumeration to specify the orientation
 *   in an cartesian coordinate system.
'''

from enum import Enum


#class Cd(Enum):
EAST      = E  = ( 1 + 0j)
NORTHEAST = NE = ( 1 + 1j)
NORTH     = N  = ( 0 + 1j)
NORTHWEST = NW = (-1 + 1j)
WEST      = W  = (-1 + 0j)
SOUTHWEST = SW = (-1 - 1j)
SOUTH     = S  = ( 0 - 1j)
SOUTHEAST = SE = ( 1 - 1j)


directions = [E, NE, N, NW, W, SW, S, SE]
hexDirections

class CellType(Enum):     # Cell states
    LIVE       = 2
    DEAD       = 4


class CellTransition(Enum):     # Cell transitions
    NONE       = 0
    EMERGENT   = 1
    DYING      = 3
    TERMINATE  = 5


''' END '''
    


''' 
 * SpacialRules.py
 *
 *   Created on:         25.12.2018
 *   last modified on:   -
 *   Author:             Andrew Jason Bishop
 *
 * General description:
 *   xxx
'''

import LifeCycler     as lc


class CellTransition(Enum):     # Cell transitions
    NONE       = 0
    EMERGENT   = 1
    DYING      = 3
    TERMINATE  = 5


class SpacialRules:

    def __init__(self, _lifeCycler):
        self.lifeCycler = _lifeCycler


    def getCoordInDirection(self, _direction):
        pass


    def deathCondition(self, _lifeNeighborCount):

        if (2 > _lifeNeighbors or 3 < _lifeNeighbors):  # Conway Rule 2&4
            return self.lifeCycler.cellDeath

        else:
            return None                                 # Conway Rule 3


    def persistensCondition(self, _lifeNeighborCount):
        pass


    def birthOrTerminationCondition(self, _lifeNeighborCount):

        if   3 == _lifeNeighbors :                      # Conway Rule 1
            return self.lifeCycler.cellBirth

        elif 0 == _lifeNeighbors :                      # free memory
            return self.lifeCycler.cellTermination

        else:
            return None


''' END '''


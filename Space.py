
''' 
 * Space.py
 *
 *   Created on:         10.11.2018
 *   last modified on:   -
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

from Enums import *


class Space:

    def __init__(self):

        self.space = {}
        self.keys = []
        self.spatialDirections = directions # from Enums


    def get_all_cellPositions(self):

        self.updateKeys()
        return self.keys


    def updateKeys(self):
        self.keys = list(self.space.keys())


    def update_cellTransition(self, _pos):
        self.space[_pos].update_transition()


    def update_cellState(self, _pos):
        self.space[_pos].update_state()


    def getCellType(self, _pos):

        if self.isOccupied( _pos ):
            return self.space[_pos].getCellType()
        else:
            return None


    def getCellTransition(self, _pos):

        if self.isOccupied( _pos ):
            return self.space[_pos].getCellTransition()
        else:
            return None


    def isOccupied(self, _pos):
        return (_pos in self.space)


    def place(self, _cell):
        self.space[ _cell.getPos() ] = _cell


    def remove(self, _pos):

        try:
            del self.space[_pos]
        except:
            pass


''' END '''



''' 
 * Universe.py
 *
 *   Created on:         10.11.2018
 *   last modified on:   -
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import Cell  as cl
from Enums import *


class Universe:

    def __init__(self, _space):
        self.space      = _space


    def update(self):

        positions = self.space.get_all_cellPositions()
        self.update_cellTransistions( positions )
        self.update_cellStates( positions )


    def update_cellTransistions(self, _positions):

        for position in _positions:
            self.space.update_cellTransition( position )


    def update_cellStates(self, _positions):

        for position in _positions:
            self.space.update_cellState( position )


    def create_LiveCell_if_Pos_is_Void_or_Dead(self, _pos=(0+0j)):

        cellState = self.space.getCellType( _pos )

        if (None == cellState or CellType.DEAD == cellState):
            newCell = cl.LiveCell( self, _pos)
            self.space.place( newCell )


    def create_DeadCell_at_Pos(self, _pos=(0+0j)):

        newDeadCell = cl.DeadCell( self, _pos)
        self.space.place( newDeadCell )


    def flipCellType(self, _cell):

        cellType = _cell.getCellType()
        cellPos  = _cell.getPos()

        if CellType.DEAD == cellType:
            newCell = cl.LiveCell( self, cellPos)

        elif CellType.LIVE == cellType:
            newCell = cl.DeadCell( self, cellPos)

        self.space.place( newCell )


    def getCellType(self, _pos):
        return self.space.getCellType( _pos )


    def getCellTransition(self, _pos):
        return self.space.getCellTransition( _pos )

    def removeCell(self, _pos):
        self.space.remove( _pos )


    def getSpatialDirections(self):
        return self.space.spatialDirections


    def getCellPositionsOf(self, _type):

        all_positions = self.space.get_all_cellPositions()

        if (CellType.LIVE == _type or CellType.DEAD == _type):
            return self.filteredCellType( all_positions, _type )

        else:
            return all_positions


    def filteredCellType(self, _all_positions, _type):

        filtered_positions = []
        for position in _all_positions:

            state = self.space.getCellType( position )
            if state == _type:
                filtered_positions.append( position )

        return filtered_positions


''' END '''


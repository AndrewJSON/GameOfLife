
''' 
 * Universe.py
 *
 *   Created on:         10.11.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import Cell  as cl
from Enums import *


class Universe:

    def __init__(self, _space):
        self.space = _space


    def update(self):

        coords = self.space.get_all_cellCoords()
        self.update_cellTransistions( coords )
        self.perform_cellTransitions( coords )


    def update_cellTransistions(self, _coords):

        for coord in _coords:
            cell = self.space.getCell( coord )
            cell.update_transition()


    def perform_cellTransitions(self, _coords):

        for coord in _coords:
            cell = self.space.getCell( coord )
            cell.perform_transition()


    def create_LiveCell_if_Coord_is_Void_or_Dead(self, _coord=(0+0j)):

        cellType = self.getCellType( _coord )

        if (None == cellType or CellType.DEAD == cellType):
            newCell = cl.LiveCell( self, _coord)
            self.space.placeCell( newCell )


    def getCell(self, _coord):
        return self.space.getCell( _coord)


    def create_DeadCell_at_Coord(self, _coord=(0+0j)):

        newDeadCell = cl.DeadCell( self, _coord)
        self.space.placeCell( newDeadCell )


    def flipCellType(self, _cell):

        cellType  = _cell.getCellType()
        cellCoord = _cell.getCellCoord()

        if CellType.DEAD == cellType:
            newCell = cl.LiveCell( self, cellCoord)

        elif CellType.LIVE == cellType:
            newCell = cl.DeadCell( self, cellCoord)

        self.space.placeCell( newCell )


    def getCellType(self, _coord):

        cell = self.space.getCell( _coord )

        if cell:
            return cell.getCellType()
        else:
            return None # None means coord is not occupied


    def removeCell(self, _coord):
        self.space.removeCell( _coord )


    def get_CellPositions_of_type_or_all(self, _type):

        all_coords = self.space.get_all_cellCoords()

        if (CellType.LIVE == _type or CellType.DEAD == _type):
            return self.filteredCellType( all_coords, _type )

        else:
            return all_coords


    def filteredCellType(self, _all_coords, _type):

        filtered_coords = []
        for coord in _all_coords:

            cellType = self.getCellType( coord )
            if cellType == _type:
                filtered_coords.append( coord )

        return filtered_coords


''' END '''


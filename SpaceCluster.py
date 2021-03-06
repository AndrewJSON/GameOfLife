
''' 
 * Space.py
 *
 *   Created on:         10.11.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

from Enums import *


#TODO ? remove isClusterEmpty()

class SpaceCluster:

    def __init__(self):

        self.cellSpace  = {}
        self.cellCoords = []

        self.spatialDirections  = directions # from Enums


    def get_all_cellCoords(self):

        self.update_CellCoords()
        return self.cellCoords


    def update_CellCoords(self):
        self.cellCoords = list(self.cellSpace.keys())


    def isCellCoordOccupied(self, _cellCoord):
        return (_cellCoord in self.cellSpace)


    def getCell(self, _cellCoord):

        if self.isCellCoordOccupied( _cellCoord ):
            return self.cellSpace[_cellCoord]
        else:
            return None


    def removeCell(self, _cellCoord):

        try:
            del self.cellSpace[_cellCoord]
        except:
            print("No cell to delete")


    def placeCell(self, _cell):

        cellCoord = _cell.getCellCoord()
        self.cellSpace[ cellCoord ] = _cell


    def isClusterEmpty(self):

        self.update_CellCoords()
        number_of_cells = len( self.cellCoords )

        if 0 >= number_of_cells:
            return True
        else:
            return False
        

''' END '''


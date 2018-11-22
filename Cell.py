
''' 
 * Cell.py
 *
 *   Created on:         09.11.2018
 *   last modified on:   -
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

from Enums import *


class Cell:

    def __init__(self, _universe, _coord, _state):

        self.universe      = _universe
        self.coord         = _coord
        self.type          = _state
        self.transition    = CellTransition.NONE
        self.lifeNeighbors = 0


    def getCellCoord(self):
        return self.coord


    def getCellType(self):
        return self.type


    def getCellTransition(self):
        return self.transition


    def eval_Number_of_Life_Neighbors(self):

        self.lifeNeighbors = 0

        for spatialDirection in directions: # from Enums.py
            self.sum_up_if_Neighbor_is_Live( spatialDirection )


    def sum_up_if_Neighbor_is_Live(self, _spatialDirection):

        neighborCoord = self.coord + _spatialDirection
        neighborState = self.universe.getCellType( neighborCoord )

        if CellType.LIVE == neighborState:
            self.lifeNeighbors += 1


    def debugPlot(self, _caller=""):

        if CellType.DEAD == self.type:
            return

        print("Pos:", self.coord,
              "\tType:", self.type,
              "\tNeighbors:", self.lifeNeighbors,
              "\tCaller:", _caller)


# ---- ---- ---- ----

class LiveCell(Cell):

    def __init__(self, _universe, _coord):

        Cell.__init__(self, _universe, _coord, CellType.LIVE)
        self.create_surrounding_DeadCells()


    def create_surrounding_DeadCells(self):

        for spatialDirection in directions: # from Enums.py

            neighborCoord = self.coord + spatialDirection
            self.create_DeadCell_if_Pos_is_Void_or_Terminate( neighborCoord )


    def create_DeadCell_if_Pos_is_Void_or_Terminate(self, _coord):

        neighborTransition = self.universe.getCellTransition( _coord )

        if ( None == neighborTransition or
             CellTransition.TERMINATE == neighborTransition):
            self.universe.create_DeadCell_at_Coord( _coord )


    def update_transition(self):

        self.eval_Number_of_Life_Neighbors()
        self.debugPlot("update_transition")

        if (2 > self.lifeNeighbors or 3 < self.lifeNeighbors): # Conway Rule 2&4
            self.transition = CellTransition.DYING

        else:
            self.transition = CellTransition.NONE              # Conway Rule 3


    def update_type(self):

        if CellTransition.DYING == self.transition:
            self.death()


    def death(self):
        self.universe.flipCellType( self )


# ---- ---- ---- ----

class DeadCell(Cell):

    def __init__(self, _universe, _coord):
        Cell.__init__(self, _universe, _coord, CellType.DEAD)


    def update_transition(self):

        self.eval_Number_of_Life_Neighbors()
        self.debugPlot("update_transition")

        if   3 == self.lifeNeighbors :                         # Conway Rule 1
            self.transition = CellTransition.EMERGENT

        elif 0 == self.lifeNeighbors :                         # free memory
            self.transition = CellTransition.TERMINATE

        else:
            self.transition = CellTransition.NONE


    def update_type(self):

        if   CellTransition.EMERGENT  == self.transition:
            self.birth()

        elif CellTransition.TERMINATE == self.transition:
            self.terminate()


    def birth(self):
        self.universe.flipCellType( self )


    def terminate(self):
        self.universe.removeCell( self.coord )


''' END '''



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

    def __init__(self, _universe, _pos, _state):

        self.universe      = _universe
        self.pos           = _pos
        self.type         = _state
        self.transition    = CellTransition.NONE
        self.lifeNeighbors = 0


    def getPos(self):
        return self.pos


    def getCellType(self):
        return self.type


    def getCellTransition(self):
        return self.transition


    def eval_Number_of_Life_Neighbors(self):

        self.lifeNeighbors = 0

        for spatialDirection in self.universe.getSpatialDirections():
            self.sum_up_if_Neighbor_is_Live( spatialDirection )


    def sum_up_if_Neighbor_is_Live(self, _spatialDirection):

        neighborCoords = self.pos + _spatialDirection
        neighborState = self.universe.getCellType( neighborCoords )

        if CellType.LIVE == neighborState:
            self.lifeNeighbors += 1


    def debugPlot(self, _caller=""):

        if CellType.DEAD == self.type:
            return

        print("Pos:", self.pos,
              "\tType:", self.type,
              "\tNeighbors:", self.lifeNeighbors,
              "\tCaller:", _caller)


# ---- ---- ---- ----

class LiveCell(Cell):

    def __init__(self, _universe, _pos):

        Cell.__init__(self, _universe, _pos, CellType.LIVE)
        self.create_surrounding_DeadCells()


    def create_surrounding_DeadCells(self):

        for spatialDirection in self.universe.getSpatialDirections():

            neighborCoords = self.pos + spatialDirection
            self.create_DeadCell_if_Pos_is_Void_or_Terminate( neighborCoords )


    def create_DeadCell_if_Pos_is_Void_or_Terminate(self, _pos):

        neighborTransition = self.universe.getCellTransition( _pos )

        if ( None == neighborTransition or
             CellTransition.TERMINATE == neighborTransition):
            self.universe.create_DeadCell_at_Pos( _pos )


    def update_transition(self):

        self.eval_Number_of_Life_Neighbors()
        self.debugPlot("update_transition")

        if (2 > self.lifeNeighbors or 3 < self.lifeNeighbors): # Conway Rule 2&4
            self.transition = CellTransition.DYING

        else:
            self.transition = CellTransition.NONE              # Conway Rule 3


    def update_state(self):

        if CellTransition.DYING == self.transition:
            self.death()


    def death(self):
        self.universe.flipCellType( self )


# ---- ---- ---- ----

class DeadCell(Cell):

    def __init__(self, _universe, _pos):
        Cell.__init__(self, _universe, _pos, CellType.DEAD)


    def update_transition(self):

        self.eval_Number_of_Life_Neighbors()
        self.debugPlot("update_transition")

        if   3 == self.lifeNeighbors :                         # Conway Rule 1
            self.transition = CellTransition.EMERGENT

        elif 0 == self.lifeNeighbors :                         # free memory
            self.transition = CellTransition.TERMINATE

        else:
            self.transition = CellTransition.NONE


    def update_state(self):

        if   CellTransition.EMERGENT  == self.transition:
            self.birth()

        elif CellTransition.TERMINATE == self.transition:
            self.terminate()


    def birth(self):
        self.universe.flipCellType( self )


    def terminate(self):
        self.universe.removeCell( self.pos )


''' END '''


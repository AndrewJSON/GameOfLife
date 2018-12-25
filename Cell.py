
''' 
 * Cell.py
 *
 *   Created on:         09.11.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

from Enums import *


class Cell:

    def __init__(self, _lifeCycler, _evaluator, _coord, _type):

        self.lifeCycler    = _lifeCycler
        self.evaluator     = _evaluator
        self.coord         = _coord
        self.type          = _type
        self.transition    = CellTransition.NONE


    def update_transition(self):

        lifeNb = self.evaluator.eval_numOf_lifeNeighbors( self.coord )
        self.determine_transition( lifeNb )


    def getCellCoord(self):
        return self.coord


    def getCellType(self):
        return self.type


    def getCellTransition(self):
        return self.transition


# ---- ---- Live Cell ---- ----

class LiveCell(Cell):

    def __init__(self, _lifeCycler, _evaluator, _coord):

        Cell.__init__(  self,
                        _lifeCycler,
                        _evaluator,
                        _coord,
                        CellType.LIVE )


    def determine_transition(self, _lifeNeighbors):

        if (2 > _lifeNeighbors or 3 < _lifeNeighbors): # Conway Rule 2&4
            self.transition = CellTransition.DYING

        else:
            self.transition = CellTransition.NONE      # Conway Rule 3


    def update_type(self):

        if CellTransition.DYING == self.transition:
            self.lifeCycler.cellDeath( self )


# ---- ---- Dead Cell ---- ----

class DeadCell(Cell):

    def __init__(self, _lifeCycler, _evaluator, _coord):
        Cell.__init__(  self,
                        _lifeCycler,
                        _evaluator,
                        _coord,
                        CellType.DEAD
                        )


    def determine_transition(self, _lifeNeighbors):

        if   3 == _lifeNeighbors :                         # Conway Rule 1
            self.transition = CellTransition.EMERGENT

        elif 0 == _lifeNeighbors :                         # free memory
            self.transition = CellTransition.TERMINATE

        else:
            self.transition = CellTransition.NONE


    def update_type(self):

        if   CellTransition.EMERGENT  == self.transition:
            self.lifeCycler.cellBirth( self )

        elif CellTransition.TERMINATE == self.transition:
            self.lifeCycler.cellTermination( self )


    def avert_termination(self):
        self.transition = CellTransition.NONE


''' END '''


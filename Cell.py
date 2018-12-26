
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

    def __init__(self, _coord, _evaluator):

        self.coord            = _coord
        self.evaluator        = _evaluator
        self.type             = None
        self.ruleMethod       = None
        self.transitionMethod = None


    def update_transition(self):

        lifeNbCount = self.evaluator.eval_numOf_lifeNeighbors( self.coord )
        self.transitionMethod = self.ruleMethod( lifeNbCount )


    def update_type(self): # TODO rename to perform_transition ?

        if self.transitionMethod:
            self.transitionMethod( self )


    def getCellCoord(self):
        return self.coord


    def getCellType(self):
        return self.type


    def getCellTransition(self):
        return self.transitionMethod


# ---- ---- Live Cell ---- ----

class LiveCell(Cell):


    def __init__(self, _coord, _evaluator, _rules):

        Cell.__init__(  self,
                        _coord,
                        _evaluator )

        self.type       = CellType.LIVE
        self.ruleMethod = _rules.liveCellRules


# ---- ---- Dead Cell ---- ----

class DeadCell(Cell):

    def __init__(self, _coord, _evaluator, _rules):

        Cell.__init__(  self,
                        _coord,
                        _evaluator )

        self.type       = CellType.DEAD
        self.ruleMethod = _rules.deadCellRules


    def avert_termination(self):
        self.transitionMethod = None


''' END '''


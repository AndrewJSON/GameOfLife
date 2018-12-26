
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

    def __init__(self, _ruleMethod, _type, _coord, _evaluator):

        self.ruleMethod = _ruleMethod
        self.type       = _type
        self.coord      = _coord
        self.evaluator  = _evaluator

        self.transitionMethod = None


    def update_transition(self):

        lifeNb = self.evaluator.eval_numOf_lifeNeighbors( self.coord )
        self.transitionMethod = self.ruleMethod( lifeNb )


    def update_type(self):

        if self.transitionMethod:
            self.transitionMethod( self )


    def avert_termination(self):
        self.transitionMethod = None


    def getCellCoord(self):
        return self.coord


    def getCellType(self):
        return self.type


    def getCellTransition(self):
        return self.transitionMethod


# ---- ---- Live Cell ---- ----

class LiveCell(Cell):

    def __init__(self, _lifeCycler, _evaluator, _coord, _rules=None):

        Cell.__init__(  self,
                        _lifeCycler,
                        _evaluator,
                        _coord,
                        CellType.LIVE,
                        _rules )

        self.ruleMethod = _rules.liveCellRules


    def determine_transition(self, _lifeNeighbors):
        self.transitionMethod = self.ruleMethod( _lifeNeighbors )
        #self.transitionMethod = self.rules.liveCellRules( _lifeNeighbors )


    def update_type(self):

        if self.transitionMethod:
            self.transitionMethod( self )


# ---- ---- Dead Cell ---- ----

class DeadCell(Cell):

    def __init__(self, _lifeCycler, _evaluator, _coord, _rules=None):

        Cell.__init__(  self,
                        _lifeCycler,
                        _evaluator,
                        _coord,
                        CellType.DEAD,
                        _rules )

        self.ruleMethod = _rules.deadCellRules


    def determine_transition(self, _lifeNeighbors):
        self.transitionMethod = self.ruleMethod( _lifeNeighbors )
        #self.transitionMethod = self.rules.deadCellRules( _lifeNeighbors )


    def avert_termination(self):
        self.transitionMethod = None


    def update_type(self):

        if self.transitionMethod:
            self.transitionMethod( self )


''' END '''


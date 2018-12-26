
''' 
 * LifeCycler.py
 *
 *   Created on:         24.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import Cell  as cl
from Enums import *


class LifeCycler:

    def __init__(self, _space):
        self.space        = _space
        self.envirCreator = None
        self.evaluator    = None
        self.rules        = None


    def setCreator(self, _ec):
        self.envirCreator = _ec


    def setEvaluator(self, _ev):
        self.evaluator = _ev


    def setRules(self, _rules):
        self.rules = _rules


    def createLiveCell(self, _coord):

        return cl.Cell( self.rules.liveCellRules,
                        CellType.LIVE,
                        _coord,
                        self.evaluator )


    def createDeadCell(self, _coord):

        return cl.Cell( self.rules.deadCellRules,
                        CellType.DEAD,
                        _coord,
                        self.evaluator )


    def cellBirth(self, _deadCell):

        deadCellCoord = _deadCell.getCellCoord()
        newLiveCell = self.createLiveCell( deadCellCoord )

        self.space.placeCell( newLiveCell )
        self.envirCreator.create_surrounding_DeadCells( deadCellCoord )


    def cellDeath(self, _liveCell):

        newDeadCell = self.createDeadCell( _liveCell.coord )
        self.space.placeCell( newDeadCell )


    def cellTermination(self, _cellToTerminate):
        self.space.removeCell( _cellToTerminate.coord )


''' END '''


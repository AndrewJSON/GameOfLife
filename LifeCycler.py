
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


    def setCreator(self, _ec):
        self.envirCreator = _ec


    def setEvaluator(self, _ev):
        self.evaluator = _ev


    def createLiveCell(self, _coord):
        return cl.LiveCell( self, self.evaluator, _coord )


    def createDeadCell(self, _coord):
        return cl.DeadCell( self, self.evaluator, _coord )


    def cellBirth(self, _deadCell):

        newLiveCell = self.createLiveCell( _deadCell.coord )
        self.space.placeCell( newLiveCell )
        self.envirCreator.create_surrounding_DeadCells( _deadCell.coord )


    def cellDeath(self, _liveCell):

        newDeadCell = self.createDeadCell( _liveCell.coord )
        self.space.placeCell( newDeadCell )


    def cellTermination(self, _cellToTerminate):
        self.space.removeCell( _cellToTerminate.coord )


''' END '''


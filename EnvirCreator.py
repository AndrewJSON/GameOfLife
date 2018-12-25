
''' 
 * EnvirCreator.py
 *
 *   Created on:         24.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import Cell  as cl
import Enums as en
#from Enums import *


class EnvirCreator:

    def __init__(self, _space):

        self.space      = _space
        self.lifeCycler = None
        self.evaluator  = None


    def setLifeCycler(self, _lc):
        self.lifeCycler = _lc


    def setEvaluator(self, _ev):
        self.evaluator = _ev


    def create_initial_LiveCell(self, _coord):

        cellType = self.evaluator.getCellType( _coord )

        if (None == cellType or en.CellType.DEAD == cellType):
            newLiveCell = self.lifeCycler.createLiveCell( _coord )
            self.space.placeCell( newLiveCell )
            self.create_surrounding_DeadCells( _coord )


    def create_surrounding_DeadCells(self, _coord):

        for spatialDirection in en.directions: # from Enums.py

            neighborCoord = _coord + spatialDirection # TODO new class
            self.create_DeadCell_or_avert_termination( neighborCoord )


    def create_DeadCell_or_avert_termination(self, _coord):

        neighborCell = self.space.getCell( _coord )

        if not neighborCell:
            self.create_DeadCell_at_Coord( _coord )
        else:
            self.avert_termination_if_scheduled( neighborCell )


    def create_DeadCell_at_Coord(self, _coord):

        newDeadCell = self.lifeCycler.createDeadCell( _coord )
        self.space.placeCell( newDeadCell )


    def avert_termination_if_scheduled(self, _neighborCell):

        neighborTransition = _neighborCell.getCellTransition()

        if ( en.CellTransition.TERMINATE == neighborTransition ):
            _neighborCell.avert_termination()


''' END '''


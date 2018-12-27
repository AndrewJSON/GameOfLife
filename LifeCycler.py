
''' 
 * LifeCycler.py
 *
 *   Created on:         24.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''


class LifeCycler:

    def __init__(self, _space):
        self.space        = _space
        self.cellFactory  = None
        self.envirCreator = None

    def setCellFactory(self, _cf):
        self.cellFactory = _cf

    def setCreator(self, _ec):
        self.envirCreator = _ec


    def cellBirth(self, _deadCell):

        deadCellCoord = _deadCell.getCellCoord()
        newLiveCell = self.cellFactory.createLiveCell( deadCellCoord )

        self.space.placeCell( newLiveCell )
        self.envirCreator.create_surrounding_DeadCells( deadCellCoord )


    def cellDeath(self, _liveCell):

        newDeadCell = self.cellFactory.createDeadCell( _liveCell.coord )
        self.space.placeCell( newDeadCell )


    def cellTermination(self, _cellToTerminate):
        self.space.removeCell( _cellToTerminate.coord )


''' END '''


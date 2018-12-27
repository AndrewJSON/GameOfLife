
''' 
 * EnvirEvaluator.py
 *
 *   Created on:         24.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import Enums as en # TODO obsolete with Directions class


class EnvirEvaluator:

    def __init__(self, _space):

        self.space = _space
        self.lifeNeighbors = 0


    def getCellType(self, _coord):

        cell = self.space.getCell( _coord )

        if cell:
            return cell.getCellType()
        else:
            return None # None means coord is not occupied


    def eval_numOf_lifeNeighbors(self, _coord):

        self.lifeNeighbors = 0

        for spatialDirection in en.directions: # from Enums.py
            neighborCoord = _coord + spatialDirection  # TODO new class
            self.sum_up_if_Neighbor_is_Live( neighborCoord )

        return self.lifeNeighbors


    def sum_up_if_Neighbor_is_Live(self, _neighborCoord ):

        neighborType = self.getCellType( _neighborCoord )

        if en.CellType.LIVE == neighborType:
            self.lifeNeighbors += 1


''' END '''


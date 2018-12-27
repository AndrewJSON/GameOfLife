
''' 
 * Rules.py
 *
 *   Created on:         25.12.2018
 *   Author:             Andrew Jason Bishop
 *
 * General description:
 *   xxx
'''


class Rules:

    def __init__(self, _lifeCycler):
        self.lifeCycler = _lifeCycler


    def liveCellRules(self, _lifeNeighborCount):

        # Conway Rules 2&4
        if (2 > _lifeNeighborCount or 3 < _lifeNeighborCount):
            return self.lifeCycler.cellDeath

        # Conway Rule 3
        else:
            return None


    def deadCellRules(self, _lifeNeighborCount):

        # Conway Rule 1
        if   3 == _lifeNeighborCount:
            return self.lifeCycler.cellBirth

        # free memory
        elif 0 == _lifeNeighborCount :
            return self.lifeCycler.cellTermination

        else:
            return None


''' END '''


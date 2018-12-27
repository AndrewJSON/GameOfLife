
''' 
 * CellFactory.py
 *
 *   Created on:         24.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import Cell as cl


class CellFactory:

    def __init__(self, _evaluator, _rules):

        self.evaluator = _evaluator
        self.rules     = _rules


    def createLiveCell(self, _coord):

        return cl.LiveCell( _coord,
                        self.evaluator,
                        self.rules )


    def createDeadCell(self, _coord):

        return cl.DeadCell( _coord,
                        self.evaluator,
                        self.rules )


''' END '''


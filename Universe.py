
''' 
 * Universe.py
 *
 *   Created on:         10.11.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import Cell  as cl
from Enums import *


class Universe:

    def __init__(self, _space):
        self.space        = _space


    def update(self):

        coords = self.space.get_all_cellCoords()
        print("cell count:", self.space.get_cell_count())
        self.update_cellTransistions( coords )
        self.update_cellTypes( coords )


    def update_cellTransistions(self, _coords):

        for coord in _coords:
            cell = self.space.getCell( coord )
            cell.update_transition()


    def update_cellTypes(self, _coords):

        for coord in _coords:
            cell = self.space.getCell( coord )
            cell.update_type()


''' END '''


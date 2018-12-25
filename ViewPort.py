
''' 
 * Viewport.py
 *
 *   Created on:         13.11.2018
 *   last modified on:   -
 *   Author:             Andrew Jason Bishop
 *
 * General description:
 *   xxx
'''

from Enums import *

import tkinter as tk
import colors  as col
import numpy   as np


class ViewPort(tk.Canvas):

    def __init__(self, _parent, _creator, _evaluator):

        super().__init__( _parent )

        self.parent             = _parent
        self.envirCreator       = _creator
        self.envirEvaluator     = _evaluator

        self.centerPortCoord    = (0+0j)
        self.halfPortCoordRange = (20+20j)
        self.cellWidth_px       = 24
        self.cellMargin_px      = 2

        self.x_limit = 2 * int(self.halfPortCoordRange.real) + 1
        self.y_limit = 2 * int(self.halfPortCoordRange.imag) + 1
        self.setSize()
        
        self.bind("<Button-3>", self.parent.switchState)


    def setSize(self):

        width_x = self.x_limit * (self.cellWidth_px + self.cellMargin_px)
        width_y = self.y_limit * (self.cellWidth_px + self.cellMargin_px)
        self.config(width=width_x, height=width_y)


    def update_viewPort(self):

        self.clear_viewPort()
        self.scan_Port_and_draw_Cells()
        self.update()


    def clear_viewPort(self):
        self.delete( tk.ALL )


    def scan_Port_and_draw_Cells(self):

        for y in range(0, self.y_limit):
            for x in range(0, self.x_limit):
                portCoord = complex(x, y)
                self.update_portCell( portCoord )


    def update_portCell(self, _portCoord):

        cellCoord = self.portCoord_to_cellCoord( _portCoord )
        cellType = self.envirEvaluator.getCellType( cellCoord )

        if cellType:
            self.draw_portCell( cellType, _portCoord )


    def portCoord_to_cellCoord(self, _portCoord):
        return ( self.centerPortCoord
                 - self.halfPortCoordRange
                 + _portCoord )


    def draw_portCell(self, _cellType, _portCoord):

        fillCol  = self.determine_fillColor( _cellType )
        pxCoords = self.calculate_pxCoords( _portCoord )
        self.create_rectangle(  pxCoords, 
                                fill = fillCol,
                                width=0)        # no border

    def determine_fillColor(self, _cellType):

        if (CellType.DEAD == _cellType):
            return col.gy2
        else:
            return col.gn


    def calculate_pxCoords(self, _portCoord):

        cw = self.cellWidth_px
        cm = self.cellMargin_px

        upperLeft_corner_px = _portCoord * (cw+cm) + (cm+cm*1j)

        x0 = upperLeft_corner_px.real; y0 = upperLeft_corner_px.imag
        x1 = x0+cw; y1 = y0+cw

        return (x0, y0, x1, y1)


    def new_lifeCell(self, _event): # TODO

        cellCoord = self.coords_for_new_lifeCell( (_event.x, _event.y) )
        self.envirCreator.create_initial_LiveCell( cellCoord )
        self.update_viewPort()


    def coords_for_new_lifeCell(self, _pxCoord ):

        portCoord = self.pxCoord_to_portCoord( _pxCoord )
        cellCoord = self.portCoord_to_cellCoord( portCoord )
        return cellCoord


    def pxCoord_to_portCoord(self, _pxCoord):

        cw = self.cellWidth_px
        cm = self.cellMargin_px
        
        port_x = np.floor( _pxCoord[0] / (cw + cm) )
        port_y = np.floor( _pxCoord[1] / (cw + cm) )

        return complex(port_x, port_y)


''' END '''


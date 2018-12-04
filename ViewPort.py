
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


# TODO
'''
*Implement ViewPort as a state machine that returns itself as a new state:
 It calls:

 def reality.on_event(self, _event)
     self.viewPort = self.viewPort.on_event( _event )

 https://dev.to/karn/building-a-simple-state-machine-in-python 

*Implement class Reality as class Reality(TK)
'''

class ViewPort(tk.Canvas):

    def __init__(self, _parent, _universe, _reality):

        super().__init__( _parent )

        self.parent             = _parent
        self.universe           = _universe
        self.reality            = _reality
        self.centerPortCoord    = (0+0j)
        self.halfPortCoordRange = (8+8j)
        self.cellWidth_px       = 24
        self.cellMargin_px      = 2

        self.x_limit = 17
        self.y_limit = 17

        self.setSize()
        self.bind("<Button-1>", self.eventHandler)
        self.bind("<Button-3>", self.switchState)


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
        cellType = self.universe.getCellType( cellCoord )
        # TODO make replace universe reference with reality

        if cellType:
            print("Port Coord", _portCoord,
                  "Cell Coord:", cellCoord,
                  "Type", cellType)
            self.draw_portCell( cellType, _portCoord )


    def portCoord_to_cellCoord(self, _portCoord):
        return ( self.centerPortCoord - self.halfPortCoordRange + _portCoord )


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


    def eventHandler(self, _event):

        if self.reality.IS_EDIT_STATE:
            pxCoord = (_event.x, _event.y)
            portCoord = self.pxCoord_to_portCoord( pxCoord )
            cellCoord = self.portCoord_to_cellCoord( portCoord )
            print("port coord:", portCoord, ", cell coord:", cellCoord, "\n")

            self.reality.create_liveCell( cellCoord )
            self.update_viewPort()


    def switchState(self, event):
        print("Switch State")
        self.reality.IS_EDIT_STATE = not self.reality.IS_EDIT_STATE


    def pxCoord_to_portCoord(self, _pxCoord):

        cw = self.cellWidth_px
        cm = self.cellMargin_px
        
        port_x = np.floor( _pxCoord[0] / (cw + cm) )
        port_y = np.floor( _pxCoord[1] / (cw + cm) )

        return complex(port_x, port_y)


if __name__ == '__main__':

# TODO
# scan all coords in view port by requesting Universe.getCellType()
# draw rectangle for every successful return, fill col depends on cell type
# use canvas.delete(tk.ALL) for every view port update ...
# (... this makes GraphicsSpace obsolete as well as GraphiCell.)
# class ViewPort(tk.Canvas):

    top = tk.Tk()
    #top.geometry("512x512")

    port = ViewPort(top)
    port.pack()
    port.update_viewPort()
    #port.pack()
    top.mainloop()


''' END '''


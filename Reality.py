
''' 
 * Reality.py
 *
 *   Created on:         13.11.2018
 *   last modified on:   -
 *   Author:             Andrew Jason Bishop
 *
 * General description:
 *   xxx
'''

import ViewPort as vp

#import matplotlib.pyplot as plt
#import numpy as np

import tkinter as tk
import colors as col

# TODO
'''
*Implement class Reality as class Reality(TK)
'''


class Reality:

    def __init__(self, _universe):

        self.universe = _universe
        self.top      = tk.Tk()
        self.top.title( "Game of Life" )
        self.viewPort = vp.ViewPortRun( self.top, _universe, self )
        self.viewPort.pack()


    def editPhase(self):

        newPort = vp.ViewPortRun( self.top, self.universe, self )
        self.viewPort.clear_viewPort()
        self.viewPort.destroy()
        self.viewPort = None
        self.viewPort = newPort

        self.viewPort.pack()
        self.viewPort.loop()


    def runPhase(self):

        newPort = vp.ViewPortRun( self.top, self.universe, self )
        self.viewPort.clear_viewPort()
        self.viewPort.destroy()
        self.viewPort = None
        self.viewPort = newPort

        self.viewPort.pack()
        self.viewPort.loop()


    def create_liveCell(self, _cellCoord): # TODO refactor?

        self.universe.create_LiveCell_if_Coord_is_Void_or_Dead(
                          _cellCoord )


    def switchState(self, _event):
        print("Switch State")

        newPort = self.viewPort.switchState()
        self.viewPort.clear_viewPort()
        self.viewPort.destroy()
        self.viewPort = None
        self.viewPort = newPort
        self.viewPort.pack()
        #self.viewport.update()
        self.viewPort.loop()



''' END '''


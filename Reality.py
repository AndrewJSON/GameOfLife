
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
import State as st

#import matplotlib.pyplot as plt
#import numpy as np

import tkinter as tk
import colors as col
#import gc


# TODO
'''
*Implement class Reality as class Reality(TK)
'''


class Reality:

    def __init__(self, _universe):

        self.universe = _universe
        self.top      = tk.Tk()
        self.top.title( "Game of Life" )
        self.viewPort = vp.ViewPort( self.top, _universe, self )
        self.viewPort.pack()

        self.state = None


    def editState(self):

        self.state = st.EditState( self.viewPort, self.universe )
        self.state.loop()


    def runState(self):

        self.state = st.RunState( self.viewPort, self.universe )
        self.state.loop()


    def create_liveCell(self, _cellCoord): # TODO refactor?

        self.universe.create_LiveCell_if_Coord_is_Void_or_Dead(
                          _cellCoord )


    def switchState(self, _event):

        print("Switch State")
        self.state = self.state.switchState()
        #gc.collect()
        self.state.loop()


''' END '''


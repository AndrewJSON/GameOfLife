
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


class Reality:

    def __init__(self, _universe):

        self.universe = _universe
        self.top      = tk.Tk()
        self.top.title( "Game of Life" )
        self.viewPort = vp.ViewPort( self.top, _universe, self )
        self.viewPort.pack()

        self.IS_INIT_STATE = False


    def initPhase(self):

        self.IS_INIT_STATE = True
        #self.bindEvents()
        self.top.mainloop()


    def bindEvents(self):
        self.viewPort.bind("<Button-1>", self.callback)


    def callback(self, _event):
        print("callback at", _event.x, _event.y)


    def update(self, _no_of_gen):

        for i in range(0, _no_of_gen):

            print("Generation:", i)
            self.top.after(900)
            self.update_ViewPort()
            self.universe.update()

        self.top.mainloop()


    def update_ViewPort(self):

        self.viewPort.update_viewPort()
        self.top.update()


    def create_liveCell(self, _cellCoord): # TODO renfactor

        if self.IS_INIT_STATE:
            self.universe.create_LiveCell_if_Coord_is_Void_or_Dead(
                          _cellCoord )

        self.update_ViewPort()


''' END '''


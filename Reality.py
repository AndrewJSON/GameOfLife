
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
        self.IS_EDIT_STATE = False

    def editPhase(self):

        while (self.IS_EDIT_STATE):
            #pass
            self.update_ViewPort()
            self.top.after(100)
            #for i in range(0,10):
            #    print("edit phase")

        self.runPhase()


    def runPhase(self):

        self.top.update()
        while( not self.IS_EDIT_STATE ):

            self.top.after(500)
            self.update_ViewPort()
            self.universe.update()

        self.editPhase()


    def bindEvents(self):
        self.viewPort.bind("<Button-1>", self.callback)


    def callback(self, _event):
        print("callback at", _event.x, _event.y)


    def update(self, _no_of_gen):

        for i in range(0, _no_of_gen):

            print("Generation:", i)
            self.top.after(500)
            self.update_ViewPort()
            self.universe.update()

        self.top.mainloop()


    def update_ViewPort(self):

        self.viewPort.update_viewPort()
        #self.top.update() # FIXME


    def create_liveCell(self, _cellCoord): # TODO refactor

        self.universe.create_LiveCell_if_Coord_is_Void_or_Dead(
                          _cellCoord )


''' END '''


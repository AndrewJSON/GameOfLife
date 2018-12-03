
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
        self.viewPort = vp.ViewPort( self.top, _universe )
        self.viewPort.pack()


    def update(self, _no_of_gen):

        for i in range(0, _no_of_gen):
            print("Generation:", i)
            #self.top.after(500)
            self.top.after(500)
            self.universe.update()
            self.viewPort.update_viewPort()
            self.top.update()

        self.top.mainloop()


''' END '''


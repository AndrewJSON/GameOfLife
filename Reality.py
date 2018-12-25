
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

import tkinter as tk
import colors as col


class Reality(tk.Tk):

    def __init__(self, _universe, _creator, _evaluator):

        tk.Tk.__init__( self )
        self.universe     = _universe

        self.title( "Game of Life" )
        self.viewPort = vp.ViewPort( self, _creator, _evaluator )
        self.viewPort.pack()

        self.state = None


    def editState(self):

        self.state = st.EditState( self )
        self.state.loop()


    def runState(self):

        self.state = st.RunState( self )
        self.state.loop()


    def create_liveCell(self, _cellCoord):
        self.envirCreator.create_initial_LiveCell( _cellCoord )

    def update_viewPort(self):
        self.viewPort.update_viewPort()


    def update_universe(self):
        self.universe.update()


    def switchState(self, _event):  #TODO rename to switchTimeState

        self.state = self.state.switchState()
        self.state.loop()


''' END '''


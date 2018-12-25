
''' 
 * State.py
 *
 *   Created on:         04.12.2018
 *   last modified on:   -
 *   Author:             Andrew Jason Bishop
 *
 * General description:
 *   xxx
'''

# TODO rename to Time

class State:

    def __init__(self, _reality):
        self.reality = _reality


# ---- ---- RUN ---- ----

class RunState(State):

    def __init__(self, _reality):
        State.__init__(self, _reality )


    def loop(self):

        while(True):
            self.reality.update_viewPort()
            self.reality.update_universe()
            self.reality.after(500)


    def switchState(self):

        self.reality.viewPort.bind( "<Button-1>",
                                    self.reality.viewPort.new_lifeCell)
        return EditState( self.reality )


# ---- ---- EDIT ---- ----

class EditState(State):

    def __init__(self, _reality):
        State.__init__(self, _reality )


    def loop(self):

        self.reality.update_viewPort()
        self.reality.mainloop()


    def switchState(self):

        self.reality.viewPort.unbind("<Button-1>")
        return RunState( self.reality )


''' END '''


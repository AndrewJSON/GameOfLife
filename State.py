
''' 
 * State.py
 *
 *   Created on:         13.11.2018
 *   last modified on:   -
 *   Author:             Andrew Jason Bishop
 *
 * General description:
 *   xxx
'''


class State:

    def __init__(self, _viewPort, _universe):
        self.viewPort = _viewPort
        self.universe = _universe


# ---- ---- RUN ---- ----

class RunState(State):

    def __init__(self, _viewPort, _universe):
        State.__init__(self, _viewPort, _universe )
        self.viewPort.unbind("<Button-1>")


    def loop(self):

        while(True):
            self.viewPort.update_viewPort()
            self.universe.update()
            self.viewPort.after(500)


    def switchState(self):
        return EditState(self.viewPort, self.universe)


# ---- ---- EDIT ---- ----

class EditState(State):

    def __init__(self, _viewPort, _universe):

        State.__init__(self, _viewPort, _universe )
        self.viewPort.bind("<Button-1>", self.viewPort.create_lifeCell)


    def loop(self):
        self.viewPort.update_viewPort()
        self.viewPort.mainloop()


    def switchState(self):
        return RunState(self.viewPort, self.universe)


''' END '''


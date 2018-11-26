
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

import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk
import colors as col


class Reality:

    def __init__(self):
        pass


    def separated_coords_as_lists(self, _positions):

        coords = np.asarray( _positions )
        x = coords.real.astype(int)
        y = coords.imag.astype(int)

        return x, y


    def plot_distinct_cells(self, _lives, _whiteSpaces ):

        a = np.zeros(shape=(20,20), dtype=int)

        z = []
        x, y = self.separated_coords_as_lists( _lives )
        x += 3
        y += 4

        for i in range(0, len(_lives)):
            z.append(3.)

        a[x,y] = z
   
        z = []
        x, y = self.separated_coords_as_lists( _whiteSpaces )
        x += 3
        y += 4

        for i in range(0, len(_whiteSpaces)):
            z.append(1.)

        a[x,y] = z

        plt.imshow(a)
        plt.pause(0.5)  # time per frame


    def plotMatrix(self, _positions):

        z = []
        x, y = self.separated_coords_as_lists( _positions )
        x += 3
        y += 4

        for i in range(0, len(_positions)):
            z.append(1)
   
        a = np.zeros(shape=(20,20), dtype=int)
        a[x,y] = z

        plt.imshow(a)
        plt.pause(1.)
        #plt.colorbar()
        #plt.show()


    def plotScatter(self, _positions):

        x, y = self.separated_coords_as_lists( _positions )
        plt.scatter(x,y, color='red')
        plt.show()


    def demos(self):
        x = [0,0,1,3]
        y = [0,3,0,3]
        z = [5,5,5,5]

        za = 0.0 * np.empty((4,4))
        za[x,y] = z
        print(za)
        plt.imshow(za);
        plt.colorbar()
        plt.show()




'''
plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()

Note some of the changes:

    Call plt.pause(0.05) to both draw the new data and it runs the GUI's event loop (allowing for mouse interaction).
'''


def do_fuck(_parent):
    _parent.geometry("300x200")
    _parent.title("does fuck")
    myLabel = tk.Label(_parent, text="my fuck label")
    myLabel.pack()


def draw_stuff(_parent):

    canvas = tk.Canvas(_parent, width=200, height=100)
    canvas.pack()

    bline = canvas.create_line(0,0,200,50, fill=col.gn)
    rline = canvas.create_line(0,100,200,50, fill=col.rt)
    rt = canvas.create_rectangle(25,25, 130 , 60, fill=col.gn)


if __name__ == '__main__':


    top = tk.Tk()
    top.geometry("300x200")
    #do_fuck(top)
    draw_stuff(top)
    #top.grid()
    top.mainloop()


''' END '''


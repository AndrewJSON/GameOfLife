# GameOflife

 * README.md

 *   Created on:         17.11.2018
 *   Author:             Andrew Jason Bishop

 * Conways Game Of Life, Python3 based

This is an implementation of Conways Game of Life in Python3 using the
traditional four conway rules.

And yes, it can be implementet in less than 50 lines of code. But for me it is
also a coding exercise, ciefly focusing on code structure, modularity and
reusable code.

The cells are stored in a single or multiple dictionaries. By using
dictionaries the space is basically a sparse matrix and has no borders.
If ClusterSpace.py is used, the cell are spread among several SpaceClusters,
depending on their coordinates and the size of a SpaceCluster.

Stored are live cells surrounded by dead cells in their nearest hood only.
So dead cells can emerge into live cells when the conway rules are applied.

A new generation is generated by an update done by the Universe.py module.
Each update consists of two cyles:

The first cycle evaluates what is going to happen for every cell, according to
the conway rules. The changes are indicated by the enumeration CellTransition,
stored in the Enums.py file. In the final cycle the transitions are performed.
Live cells turn into dead cells and vice versa.

In order to keep the memory usage low, there is one additional rule: A dead
cell with no live neighbor is beeing deleted.

Yet, the graphical output is implementet only tentatively by using matplotlib.
This rude coding can be found in Reality.py.

#TODO:
*implement cluster defrag
*implement improved graphics


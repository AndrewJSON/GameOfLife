
''' 
 * Space.py
 *
 *   Created on:         10.11.2018
 *   last modified on:   -
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import SpaceCluster as sc

from Enums import *

import math as m
import numpy as np


class ClusterSpace:

    def __init__(self, _clusterSize=8):

        self.spaceClusters     = {}
        self.clusterSize       = _clusterSize

        self.clusterCoords     = []
        self.cellCoords        = []


    def get_all_cellCoords(self):

        self.updateCellCoords_and_defrag_clusters()
        return self.cellCoords


    def updateCellCoords_and_defrag_clusters(self):

        self.cellCoords.clear()
        self.updateClusterCoords()

        for clusterCoord in self.clusterCoords:
            self.append_coords_or_delete_empty_cluster( clusterCoord )


    def get_cell_count(self):
        return len(self.cellCoords)


    def updateClusterCoords(self):
        self.clusterCoords = list( self.spaceClusters.keys() )


    def append_coords_or_delete_empty_cluster(self, _clusterCoord):

        cellCoords = self.get_all_CellCoords_from_Cluster( _clusterCoord )
        #print("cluster:", _clusterCoord, "\ncells:", cellCoords)

        if len( cellCoords ):
             self.cellCoords += cellCoords
        else:
            self.remove_Cluster( _clusterCoord )


    def get_all_CellCoords_from_Cluster(self, _clusterCoord):

        cluster = self.spaceClusters[_clusterCoord]
        return cluster.get_all_cellCoords()


    def derive_ClusterCoord_from_Cell(self, _cell):

        cellCoord = _cell.getCellCoord()
        return self.derive_ClusterCoord_from_CellCoord( cellCoord )


    def derive_ClusterCoord_from_CellCoord(self, _cellCoord ): #TODO

        cluster_r = np.floor( _cellCoord.real / self.clusterSize )
        cluster_i = np.floor( _cellCoord.imag / self.clusterSize )

        return complex(cluster_r, cluster_i)


    def isCellCoordOccupied(self, _coord):
        # returns True or False if cluster or cell are not present

        clusterCoord = self.derive_ClusterCoord_from_CellCoord( _cellCoord )

        if self.isClusterPresent( clusterCoord ):
            return self.spaceClusters[clusterCoord].isCellCoordOccupied( _cellCoord )
        else:
            #print("cluster not present")
            return False


    def getCell(self, _cellCoord):

        clusterCoord = self.derive_ClusterCoord_from_CellCoord( _cellCoord )

        if self.isClusterPresent( clusterCoord ):
            return self.spaceClusters[clusterCoord].getCell( _cellCoord )

        else:
            #print("cluster not present")
            return None


    def removeCell(self, _cellCoord):

        clusterCoord = self.derive_ClusterCoord_from_CellCoord( _cellCoord )

        try:
            self.spaceClusters[clusterCoord].removeCell( _cellCoord )
        except:
            print("cluster not found")


    def placeCell(self, _cell):

        clusterCoord = self.derive_ClusterCoord_from_Cell( _cell )

        if not self.isClusterPresent( clusterCoord ):
            newSpaceCluster = sc.SpaceCluster()
            self.spaceClusters[clusterCoord] = newSpaceCluster

        self.spaceClusters[ clusterCoord ].placeCell( _cell )


    def isClusterPresent(self, _clusterCoord):
        return (_clusterCoord in self.spaceClusters)


    def remove_Cluster(self, _coord):

        try:
            print("***removing cluster", _coord)
            del self.spaceClusters[_coord]
        except:
            print("No cluster to delete")


''' END '''


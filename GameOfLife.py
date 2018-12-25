
''' 
 * GameOfLife.py
 *
 *   Created on:         10.11.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import Universe       as un
import ClusterSpace   as cs
import SpaceCluster   as sc
import LifeCycler     as lc
import EnvirCreator   as ec
import EnvirEvaluator as ee

import Reality      as rt
import Patterns     as pt
from Enums import *

#import matplotlib.pyplot as plt


USE_CLUSTER_SPACE = True

def init_with_pattern(_pattern):

    print("Initial live cells:")

    for cell in _pattern:
        myEnvirCreator.create_initial_LiveCell( cell )
        print( cell)


def wireUp():

    myLifeCycler.setCreator( myEnvirCreator )
    myLifeCycler.setEvaluator( myEnvirEvaluator )

    myEnvirCreator.setLifeCycler( myLifeCycler )
    myEnvirCreator.setEvaluator( myEnvirEvaluator )
    print("wired up")


if __name__ == '__main__':

    if USE_CLUSTER_SPACE:
        mySpace    = cs.ClusterSpace()
    else:
        mySpace    = sc.SpaceCluster()


    myLifeCycler     = lc.LifeCycler(mySpace)
    myEnvirCreator   = ec.EnvirCreator(mySpace)
    myEnvirEvaluator = ee.EnvirEvaluator(mySpace)

    wireUp()

    myUniverse = un.Universe( mySpace )
    myReality  = rt.Reality( myUniverse,
                             myEnvirCreator,
                             myEnvirEvaluator )

    init_with_pattern( pt.glider )

    myReality.runState()
    #myReality.editState()


''' END '''


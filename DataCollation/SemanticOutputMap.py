# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:54:25 2019

@author: Guy
"""
import random
import Semantic_Class as semantics
from abc import ABC, abstractmethod

class SemanticMap():
    
    def __init__(self, mapDict = None):
        
        if mapDict == None:
            self._generateDummyMapping
        
        else:
            self._mapDict = mapDict
    
    def _generateDummyMapping(self, dataSize = 5):
        
        self._mapDict = {}
        for i in range(dataSize):
            self._mapDict[i] = RandomSemanticClass
        
def RandomSemanticClass():
    possibleTypes = (semantics.Binary("button{0}".format(random.randint(1,100))),
                     semantics.LCDDisplay("LCD{0}".format(random.randint(1,100))),)
    
    return random.choice(possibleTypes)

        
if __name__ == '__main__':
    print(RandomSemanticClass().name)
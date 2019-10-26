# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:54:25 2019

@author: Guy
"""

class SemanticMap():
    
    def __init__(self, mapDict = None):
        
        if mapDict = None:
            self._generateDummyMapping
        
        else:
            self._mapDict = mapDict
    
    def _generateDummyMapping(self, dataSize = 5):
        
        self._mapDict = {}
        
        
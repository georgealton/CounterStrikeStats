'''
Created on 10 Jan 2014

@author: george
'''

import wx.grid as gridlib

class SimpleGrid(gridlib.Grid):
    def showJustGrid(self):
        self.DisableDragColSize()
        self.DisableDragCell()
        self.DisableDragRowSize()
        self.DisableDragGridSize()
        self.SetRowLabelSize(0)
        self.SetColLabelSize(0)

class MainGrid(gridlib.Grid):
    '''
    classdocs
    '''
    def __init__(self): 
        self.showJustGrid()
        
           
    def showJustGrid(self):
        self.DisableDragColSize()
        self.DisableDragCell()
        self.DisableDragRowSize()
        self.DisableDragGridSize()
        self.SetRowLabelSize(0)
        self.SetColLabelSize(0)
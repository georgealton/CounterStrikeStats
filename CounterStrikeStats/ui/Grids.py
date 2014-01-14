'''
Created on 10 Jan 2014

@author: george
'''

import wx.grid as gridlib

class SimpleGridMixin(gridlib.Grid):
    def simplifyGrid(self):
        self.DisableDragColSize()
        self.DisableDragCell()
        self.DisableDragRowSize()
        self.DisableDragGridSize()
        self.SetRowLabelSize(0)
        self.SetColLabelSize(0)

class Main(SimpleGridMixin, gridlib.Grid):
    '''
    classdocs
    '''
    def __init__(self, parent):
        gridlib.Grid.__init__(self, parent) 
        self.simplifyGrid()
        
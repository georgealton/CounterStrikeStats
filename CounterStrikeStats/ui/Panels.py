'''
Created on 10 Jan 2014

@author: george
'''
from wx import Panel
from Grids import MainGrid

class SimplePanel(Panel):
    
    def __init__(self, parent):
        Panel.__init__(self, parent)
        
        
        grid = self.addGrid()
        
        
    def addGrid(self):
        return MainGrid(self)
    
    def getGrid(self):
        return self.grid
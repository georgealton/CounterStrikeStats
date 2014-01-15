'''
Created on 10 Jan 2014

@author: george
'''
from wx import Panel, RED


class Main(Panel):
    
    def __init__(self, parent):
        Panel.__init__(self, parent)
        
        #self.grid = Grids.Main(self)
        self.BackgroundColour = RED
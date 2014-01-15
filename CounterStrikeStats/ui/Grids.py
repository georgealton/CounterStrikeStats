'''
Created on 10 Jan 2014

@author: george
'''
from SQLAchemy import Player
from wx.grid import Grid

class SimpleGridMixin(Grid):
    def simplifyGrid(self):
        self.DisableDragColSize()
        self.DisableDragCell()
        self.DisableDragRowSize()
        self.DisableDragGridSize()
        self.SetRowLabelSize(0)
        self.SetColLabelSize(0)

class Main(SimpleGridMixin, Grid):
    '''
    classdocs
    '''
    def __init__(self, parent):
        

        Grid.__init__(self, parent) 
        self.createPlayerGrid()
        self.simplifyGrid()
    
    ## Testing!
    def createPlayerGrid(self):
        players = Player().getAll()
        
        playerattrs = ['lastName', 'kills', 'deaths']
        columns = len(playerattrs)
        rows = len(players)
        self.CreateGrid(rows, columns)
        row=0
         
        for player in players:
            for v in playerattrs:
                column = playerattrs.index(v)
                self.SetCellValue(row, column, str(getattr(player, v)))
                self.SetReadOnly(row, column, True)
            row+=1
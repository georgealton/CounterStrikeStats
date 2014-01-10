'''
Created on 10 Dec 2013

@author: george
'''
if __name__ == '__main__':

    try : 
        from Frames import WXFrame
        from SQLAchemy import Player
        import wx
        import wx.grid as gridlib
    
    except ImportError as e : 
        raise e
    
    APP_TITLE = "CounterStrike Stats"
    
    app = wx.App(False)

    try : 
        players = Player().getAll()
        
        playerattrs = ['lastName', 'kills', 'deaths']
        columns = len(playerattrs)
        rows = len(players)
        
        frame = WXFrame(None, APP_TITLE)
        grid = gridlib.Grid(frame.mypanel) 
        grid.CreateGrid(rows, columns)
        row=0
        
        for player in players:
            for v in playerattrs:
                column = playerattrs.index(v)
                grid.SetCellValue(row, column, str(getattr(player, v)))
                grid.SetReadOnly(row, column, True)
            row+=1
           
        def showJustGrid(grid):
            grid.DisableDragColSize()
            grid.DisableDragCell()
            grid.DisableDragRowSize()
            grid.DisableDragGridSize()
            grid.SetRowLabelSize(0)
            grid.SetColLabelSize(0)
         
        showJustGrid(grid)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid, 1)        
        frame.SetSizer(sizer)
        sizer.Fit(frame.mypanel)
       


        app.MainLoop()
    
    except Exception as e:
        print e
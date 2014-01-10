'''
Created on 10 Dec 2013

@author: george
'''
import MySQLdb
try : 
    from MainFrame import WXFrame
    from SQLAchemy import *
    import wx
    import wx.grid as gridlib

except Exception as e : 
    print e

if __name__ == '__main__':
    
    try : 
        app = wx.App(False)
        frame = WXFrame(None,"CounterStrike Stats")
        panel = wx.Panel(frame)
        grid = gridlib.Grid(panel)  
          
    except Exception as e  :
        print(e)
    
    try : 
        players = Player().getAll()
        print(players)
        playerattrs = ['name', 'kills', 'deaths']
        
        columns = len(playerattrs)
        rows = len(players.list)
        
        grid.CreateGrid(rows, columns)
        row=0
        for player in players.list:
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
        sizer.Add(grid,1)        
        frame.SetSizer(sizer)
        sizer.Fit(panel)
       


        app.MainLoop()
    
    except Exception as e:
        print e
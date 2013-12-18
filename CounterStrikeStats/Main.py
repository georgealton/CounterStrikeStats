'''
Created on 10 Dec 2013

@author: george
'''
import MySQLdb
try : 
    from HLModule import Players
    from MainFrame import WXFrame
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
        p = Players()

        extractKeys = ['lastName', 'kills', 'deaths']

        grid.CreateGrid(len(p.all), len(extractKeys))
        i=0
        for row in p.all:
            for u in range(len(extractKeys)):
                grid.SetCellValue(i, u, str(row[extractKeys[u]]))
                grid.SetReadOnly(i, u, True)
            i+=1
           
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
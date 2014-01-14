'''
Created on 14 Dec 2013

@author: george
'''
import wx 
import Grids
import Panels
import MenuBars


class WXFrame(wx.Frame):

    def __init__(self, parent, title):
        '''
        Constructor
        '''
        
        wx.Frame.__init__(self, parent,id=wx.ID_ANY, title=title, size=(800,600))
        
        self.sb = self.CreateStatusBar()
        self.SetMenuBar(MenuBars.Main())  # Adding the MenuBar to the Frame content.
        self.mypanel = Panels.Main(self)
        self.Show(True)
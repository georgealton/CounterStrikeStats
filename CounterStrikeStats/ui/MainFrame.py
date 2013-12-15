'''
Created on 14 Dec 2013

@author: george
'''
import wx 


class WXFrame(wx.Frame):

    def __init__(self, parent, title):
        '''
        Constructor
        '''
        
        wx.Frame.__init__(self, parent,id=wx.ID_ANY, title=title, size=(800,600))
        
        self.sb = self.CreateStatusBar()
        
        # Setting up the filemenu.
        filemenu = wx.Menu()
        menuSettings = filemenu.Append(wx.ID_PREFERENCES, "S&ettings", "Adjust Program Settings")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        
        
        viewmenu = wx.Menu()
        self.toggle_statusbar = viewmenu.Append(wx.ITEM_CHECK,'Show StatusBar', 'Show Statusbar', kind=wx.ITEM_CHECK)
        viewmenu.Check(self.toggle_statusbar.GetId(), True)
        
        
        
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(viewmenu, "&View")
        
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        
        
        self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.onExit, menuExit)
        self.Bind(wx.EVT_MENU, self.onSettings, menuSettings)        
        self.Bind(wx.EVT_MENU, self.onToggleStatusBar, self.toggle_statusbar)
        self.Show(True)
        
        
        
    def onAbout(self,e):
        print self
    
    def onExit(self,e):
        self.Close(True)
    
    def onSettings(self,e):
        pass
    
    def onToggleStatusBar(self,e):
        if self.toggle_statusbar.IsChecked():
            self.sb.Show()
        else:
            self.sb.Hide()
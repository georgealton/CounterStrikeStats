'''
Created on 13 Jan 2014

@author: george
'''
from wx import Menu, ID_PREFERENCES, ID_ABOUT, ID_EXIT, EVT_MENU, ITEM_CHECK, ID_NETWORK

class File(Menu):
    
    def __init__(self, parent):
        Menu.__init__(self)
        
        self.parent = parent
        
        self.connect = self.Append(ID_NETWORK, "C&onnect", "Open Connection To DB")   
        self.settings = self.Append(ID_PREFERENCES, "S&ettings", "Adjust Program Settings")   
        self.about = self.Append(ID_ABOUT, "&About","Information about this program")
        self.AppendSeparator()
        self.exit = self.Append(ID_EXIT,"E&xit"," Terminate the program")
        
        self.Bind(EVT_MENU, self.onConnect, self.connect)
        self.Bind(EVT_MENU, self.onSettings, self.settings)
        self.Bind(EVT_MENU, self.onAbout, self.about)
        self.Bind(EVT_MENU, self.onExit, self.exit)
        
    def onAbout(self,e):
        print self
    
    def onExit(self,e):
        self.parent.GetFrame().Close(True)
    
    def onSettings(self,e):
        print self 
    
    def onConnect(self, e):
        print 'Connection'
        # importing here will cause the module to load the connection
        import SQLAlchemy

class View(Menu):
    def __init__(self, parent):
        Menu.__init__(self)

        self.parent = parent
        self.statusbartoggler = self.Append(ITEM_CHECK,'Show StatusBar', 'Show Statusbar', kind=ITEM_CHECK)
        self.Check(self.statusbartoggler.GetId(), True)
        
        self.Bind(EVT_MENU, self.onToggleStatusBar, self.statusbartoggler)

    def onToggleStatusBar(self,e):
        if self.statusbartoggler.IsChecked():
            self.parent.GetFrame().GetStatusBar().Show()
        else:
            self.parent.GetFrame().GetStatusBar().Hide()
'''
Created on 13 Jan 2014

@author: george
'''
from wx import Menu, ID_PREFERENCES, ID_ABOUT, ID_EXIT, EVT_MENU, ITEM_CHECK

class File(Menu):
    
    def __init__(self, parentFrame):
        Menu.__init__(self)
        
        self.parentFrame = parentFrame
        
        self.settings = self.Append(ID_PREFERENCES, "S&ettings", "Adjust Program Settings")   
        self.about = self.Append(ID_ABOUT, "&About"," Information about this program")
        self.AppendSeparator()
        self.exit = self.Append(ID_EXIT,"E&xit"," Terminate the program")
        
        self.Bind(EVT_MENU, self.onSettings, self.settings)
        self.Bind(EVT_MENU, self.onAbout, self.about)
        self.Bind(EVT_MENU, self.onExit, self.exit)
        
    def onAbout(self,e):
        print self
    
    def onExit(self,e):
        self.parentFrame.Close(True)
    
    def onSettings(self,e):
        print self 


class View(Menu):
    def __init__(self, parentFrame):
        Menu.__init__(self)

        self.parentFrame = parentFrame
        self.statusbartoggler = self.Append(ITEM_CHECK,'Show StatusBar', 'Show Statusbar', kind=ITEM_CHECK)
        self.Check(self.statusbartoggler.GetId(), True)
        
        self.Bind(EVT_MENU, self.onToggleStatusBar, self.statusbartoggler)

    def onToggleStatusBar(self,e):
        if self.statusbartoggler.IsChecked():
            self.parentFrame.GetStatusBar().Show()
        else:
            self.parentFrame.GetStatusBar().Hide()
'''
Created on 14 Dec 2013

@author: george
'''
from wx import Frame, ID_ANY
import Panels
import MenuBars


class Main(Frame):

    def __init__(self, parent, title):
        '''
        Constructor
        '''
        
        Frame.__init__(self, parent,id=ID_ANY, title=title, size=(800,600))
        
        self.sb = self.CreateStatusBar()
        
        self.SetMenuBar(MenuBars.Main())  # Adding the MenuBar to the Frame content.
        self.mypanel = Panels.Main(self)
        
        self.Centre()
        self.Show(True)
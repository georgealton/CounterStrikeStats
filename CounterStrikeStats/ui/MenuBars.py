'''
Created on 13 Jan 2014

@author: george
'''
from wx import MenuBar
import Menus

class Main(MenuBar):
    def __init__(self):
        MenuBar.__init__(self)
        
        self.Append(Menus.File(self),"&File")
        self.Append(Menus.View(self), "&View")
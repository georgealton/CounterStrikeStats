'''
Created on 10 Dec 2013

@author: george
'''
if __name__ == '__main__':

    try : 
        import Frames
        import wx
    except ImportError as e : 
        raise e

    try : 
        
        app = wx.App(False)
        frame = Frames.Main(None,  "CounterStrike Stats")
        app.MainLoop()
    
    except Exception as e:
        print e
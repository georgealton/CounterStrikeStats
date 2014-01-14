'''
Created on 10 Dec 2013

@author: george
'''
if __name__ == '__main__':

    try : 
        import wx
        import Frames
    except ImportError as e : 
        raise e
    
    try : 
        css = wx.App(False)
        frame = Frames.Main(None,  "CounterStrike Stats")
        css.MainLoop()
    except Exception as e:
        print e
        quit()
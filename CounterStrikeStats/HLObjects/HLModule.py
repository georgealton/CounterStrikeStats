'''
Created on 13 Dec 2013

@author: george
'''
from DatabaseConnector import Connector as dbc

class HLStatsDB(object):
    #Share this connection with all objects may want to open up more of these in the future
    conn = dbc("root", "pharos1", "10.97.158.244", "cs-stats")
    
    # We're only allowed ONE active cursor so we need this to be used by all subclasses
    # multiple cursors will block each other
    cursor = conn.getCursor()
        
    def __init__(self):
        '''
        Constructor
        '''
        

class Players(HLStatsDB):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.cursor.execute("SELECT * FROM hlstats_Players")
        self.all = self.cursor.fetchall() 
            

class Player(HLStatsDB):
    def __init__(self):
        pass


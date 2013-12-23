'''
Created on 13 Dec 2013

@author: george
'''
from DatabaseConnector import Connector as dbc

class HLStatsDB(object):
    #Share this connection with all objects may want to open up more of these in the future
    try :
        conn = dbc("root", "pharos1", "10.97.158.244", "cs-stats")
    except Exception as e :
        raise e
    # We're only allowed ONE active cursor so we need this to be used by all subclasses
    # multiple cursors will block each other
    cursor = conn.getCursor()
        
    def __init__(self):
        '''
        Constructor
        '''
        

    @property
    def tablename(self):
        return self._tablename 

class Players(HLStatsDB):
    '''
    classdocs
    '''
    
    _tablename = "hlstats_Players"
    
    def __init__(self):
        '''
        Constructor
        '''
        self.list = [] # Holds list of Player Objects
        
        self.cursor.execute("SELECT * FROM " + self.tablename)
        
        # TODO instead of doing a fetchall we need to make this do a fetchone 
        # and add individually because, fetchall could take a long time, especially if 
        # we move 
        self.all = self.cursor.fetchall()
        self.cursor.close() 
        for players in self.all :
            if players['hideranking'] != 1 : # filters out Bots as defined by hlstats
                self.list.append(Player(
                                         name = players['lastName'],
                                         playerid = players['playerId'],
                                         kills  = players['kills'],
                                         deaths = players['deaths'],
                                         skill = players['skill']
                                         )
                                 )
        
            

class Player(HLStatsDB):
    _tablename = "hlstats_Players"
    
    def __init__(self, name="", playerid="", skill=0, kills=0, deaths=0):
        self.name = name
        self.playerid = playerid
        self.kills = kills
        self.deaths = deaths
        self.skill = skill
        
    def __gt__(self, other):
        if isinstance(other, Player):
            return self.skill > other.skill
        else : 
            return False
    
    def __lt__(self, other):
        if isinstance(other, Player):
            return self.skill < other.skill
        else : 
            return False 
    
    def __str__(self):
        return self.name + " [" + str(self.skill) + "]"
    
        
class Weapon(HLStatsDB):
    _tablename = "hlstats_Weapons"
    
    def __init__(self):
        pass

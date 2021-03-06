'''
Created on 02 Jan 13

@author: WJHoward
'''



#SQL alchemy
from sqlalchemy import create_engine, MetaData, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Enum, Float
from dbsettings import DB_USER, DB_PASS, DB_ADDR, DB_NAME, DB_TYPE

try:
    print 'LOADED SQLALCHEMY'
    engine = create_engine(
            DB_TYPE + "://" + DB_USER + ":" + DB_PASS + '@' + DB_ADDR + '/' + DB_NAME,
            isolation_level="READ UNCOMMITTED"
        )
    
    #engine.echo = True # Display the executed SQL
    metadata = MetaData(engine) #A table catalogue
    #Need a session
    Session = sessionmaker(bind=engine)
    session = Session()
 
 
   
#http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html#declare-a-mapping
#   
# Classes mapped using the Declarative system are defined in terms of a 
# base class which maintains a catalog of classes and tables relative to 
# that base - this is known as the declarative base class. Our application 
# will usually have just one instance of this base in a commonly imported 
# module. We create the base class using the declarative_base() 
    Base = declarative_base()
    
except Exception as e:
    raise e


#contains the link table between players and ribbons
player_ribbon_assoction = Table('hlstats_Players_Ribbons', 
                                Base.metadata, 
                                Column('playerId', Integer, ForeignKey('hlstats_Players.playerId')),
                                Column('ribbonId', Integer, ForeignKey('hlstats_Ribbons.ribbonId')))

class Player(Base):
    __tablename__ = 'hlstats_Players'
    
    playerId = Column(Integer, primary_key=True)
    last_event = Column(Integer)
    connection_time = Column(Integer)
    lastName = Column(String)
    lastAddress = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    flag = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    clan = Column(String, ForeignKey('hlstats_Clans.clanId'))
    kills = Column(Integer)
    deaths = Column(Integer)
    suicides = Column(Integer)
    skill = Column(Integer)
    shots = Column(Integer)
    hits = Column(Integer)
    teamKills = Column(Integer)
    fullName = Column(String)
    email = Column(String)
    homepage = Column(String)
    icq = Column(Integer)
    game = Column(String, ForeignKey('hlstats_Games.code'))
    hideranking = Column(Integer)
    headshots = Column(Integer)
    last_skill_change = Column(Integer)
    displayEvents = Column(Integer)
    kill_streak = Column(Integer)
    death_streak = Column(Integer)
    blockavatar = Column(Integer)
    activity = Column(Integer)
    createdate = Column(Integer)
    
    player_game = relationship("Game", backref="hlstats_Players")
    player_clan  = relationship("Clan", backref="hlstats_Players")
    player_ribbons = relationship("Ribbon",secondary=player_ribbon_assoction, backref="players")

    @classmethod
    def getAll(self):
        return session.query(self).filter(self.hideranking != 1).order_by(self.skill.desc()).all()
    
    def __repr__(self):
        return str(self.lastName)
    
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

class Weapon(Base):
    __tablename__ = "hlstats_Weapons"
    
    weaponId = Column(Integer, primary_key=True)
    game = Column(String, ForeignKey('hlstats_Games.code'))
    code = Column(String)
    name = Column(String)
    modifier = Column(Float)
    kills = Column(Integer)
    headshots = Column(Integer)
    
    relationship("Game", backref="hlstats_Weapons")
    
    def __repr__(self):
        return str(self.name)
          
    def __gt__(self, other):
        if isinstance(other, Weapon):
            return self.kills > other.kills
        else :
            return False
        
    def __lt__(self, other):
        if isinstance(other, Weapon):
            return self.kills < other.kills
        else :
            return False


class Game(Base):
    __tablename__ = "hlstats_Games"
    
    code = Column(String, primary_key=True)
    name = Column(String)
    hidden = Column(Enum([0,1]))
    realgame = Column(String)
    
    def __repr__(self):
        return str(self.name)


class Award(Base):
    __tablename__ = "hlstats_Awards"
    
    awardId = Column(Integer, primary_key=True)
    awardType = Column(String) ##not sure what this is 
    game = Column(String, ForeignKey('hlstats_Games.code'))
    name = Column(String)
    verb = Column(String)
    d_winner_id = Column(Integer)
    d_winner_count = Column(Integer)
    g_winner_id = Column(Integer)
    g_winner_count = Column(Integer)
    
    relationship("Game", backref="hlstats_Awards")
    
    def __repr__(self):
        return str(self.name)

    
class Clan(Base):
    __tablename__ = "hlstats_Clans"
    
    clanId = Column(Integer, primary_key=True)
    tag = Column(String)
    name = Column(String)
    homepage = Column(String)
    game = Column(String, ForeignKey('hlstats_Games.code'))
    
    relationship("Game", backref="hlstats_Clans")
    
    def __repr__(self):
        return str(self.tag + ' ' + self.name)


class Ribbon(Base):
    __tablename__ = "hlstats_Ribbons"
    
    ribbonId = Column(Integer, primary_key=True)
    awardCode = Column(String)
    awardCount = Column(String)
    special = Column(Integer)
    game = Column(String, ForeignKey('hlstats_Games.code'))
    image = Column(String)
    ribbonName = Column(String)
    
    relationship("Game", backref="hlstats_Ribbons")
    
    def __repr__(self):
        return str(self.ribbonName)

class Team(Base):
    __tablename__ = "hlstats_Teams"
    
    teamId = Column(Integer, primary_key=True)
    game = Column(String, ForeignKey('hlstats_Games.code'))
    code = Column(String)
    name = Column(String)
    hidden = Column(Enum([0,1]))
    
    def __repr__(self):
        return str(self.name)

class Action(Base):
    __tablename__ = "hlstats_Actions"
    
    id = Column(Integer, primary_key=True)
    game = Column(String, ForeignKey('hlstats_Games.code'))
    code = Column(String)
    reward_player = Column(Integer) ## amount of skillchange
    reward_team = Column(Integer) ## amount of skillchange
    team = Column(String)
    description = Column(String)
    count = Column(Integer)
    
    relationship("Game", backref="hlstats_Actions")
    
    def __repr__(self):
        return str(self.description)
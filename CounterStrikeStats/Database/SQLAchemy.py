'''
Created on 02 Jan 13

@author: WJHoward
'''



#SQL alchemy
from sqlalchemy import create_engine, MetaData, Table, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import *

try:
    engine = create_engine(
                "mysql://root:pharos1@10.97.158.244/cs-stats",
                isolation_level="READ UNCOMMITTED"
            )
    
    engine.echo = True # Display the executed SQL
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


class Player(Base):
    __tablename__ = 'hlstats_Players'
    
    playerid = Column(Integer, primary_key=True)
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
    
    plays = relationship("Game", backref="hlstats_Players")
    

class Weapon(Base):
    __tablename__ = "hlstats_Weapons"
    
    weaponId = Column(Integer, primary_key=True)
    game = Column(String, ForeignKey('hlstats_Games.code'))
    code = Column(String)
    name = Column(String)
    modifier = Column(Float)
    kills = Column(Integer)
    headshots = Column(Integer)


class Game(Base):
    __tablename__ = "hlstats_Games"
    
    code = Column(String, primary_key=True)
    name = Column(String)
    hidden = Column(Enum)
    realgame = Column(String)

class Award(Base):
    __tablename__ = "hlstats_Players_Awards"
    
    awardId = Column(Integer, primary_key=True)
    awardType = Column(String) ##not sure what this is
    game = Column(String, ForeignKey('hlstats_Games.code'))
    name = Column(String)
    verb = Column(String)
    d_winner_id = Column(Integer)
    d_winner_count = Column(Integer)
    g_winner_id = Column(Integer)
    g_winner_count = Column(Integer)
    


x = session.query(Player.lastName).all()
print x
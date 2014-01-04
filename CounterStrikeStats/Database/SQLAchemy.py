'''
Created on 02 Jan 13

@author: WJHoward
'''



#SQL alchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker
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



# Try some stuff
players = Table('hlstats_Players', metadata, autoload=True)
result = session.query(players).all()

s = players.select(players.c.hideranking != 1)
result = s.execute()

for row in result:
    print row.lastName

class Player(Base):
    __tablename__ = 'hlstats_Player'
    
    id = Column(Integer, primary_key=True)
    

class Weapon(Base):
    __tablename__ = "hlstats_Weapons"
    
    id = Column(Integer, primary_key=True)
    
    
    

#print s

#for row in result:
#    print str(row)
#row = query.all()

#print "Row" + str(row)
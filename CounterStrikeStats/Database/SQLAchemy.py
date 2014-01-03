'''
Created on 02 Jan 13

@author: WJHoward
'''



#SQL alchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

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
    
    
except Exception as e:
    raise e



# Try some stuff
players = Table('hlstats_Players', metadata, autoload=True)
result = session.query(players).all()

s = players.select(players.c.hideranking != 1)
result = s.execute()
print result

for row in result:
    print row
#print s

#for row in result:
#    print str(row)
#row = query.all()

#print "Row" + str(row)
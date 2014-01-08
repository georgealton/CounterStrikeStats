'''
Created on 10 Dec 2013

@author: george
'''
try : 
    import MySQLdb
    from dbsettings import *

except ImportError as ie:
    raise ie

class Connector(object):
    '''
    classdocs
    '''


    def __init__(self, user=None, passwd=None, host=None, db=None):
        '''
        Constructor
        '''
        self.user = user
        self.passwd = passwd
        self.host = host
        self.db = db
        
        self.connection = None
        
    
    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, user):
        self._user = user
    
    @property
    def host(self):
        return self._host
    @host.setter
    def host(self, host):
        self._host = host
        
    @property
    def passwd(self):
        return self._passwd
    @passwd.setter
    def passwd(self, passwd):
        self._passwd = passwd
    
    @property
    def db(self):
        return self._db
    @db.setter
    def db(self, db):
        self._db = db
      
    @property        
    def connection(self):
        return self._connection
    @connection.setter
    def connection(self, name):
        try :
            self._connection = MySQLdb.connect(user = self.user, passwd = self.passwd, host = self.host, db = self.db) 
        except Exception as e :
            self._connection = None
            raise e
    @connection.deleter
    def connection(self):
        if self.connection is not None:
            self.connection.close()
                 
    def getCursor(self):
        return self.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor) 
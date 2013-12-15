'''
Created on 14 Dec 2013

@author: george
'''
import json
from httplib import HTTPConnection
import urllib

class WebAPICaller(object):
    '''
    classdocs
    '''
    PORT = 80
    CALL_METHOD = "GET"


    def __init__(self, url):
        '''
        Constructor
        '''
        self.url = url
        self._iface = ""
        self._method = ""
        self._extra = ""
        self._params = None
        self.port = WebAPICaller.PORT
        self.httpmethod = WebAPICaller.CALL_METHOD
    
  
    def sendCall(self):
        
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        params = self.params
        callurl = "/" + self.iface + self.method + self.extra 
        httpmethod = self.httpmethod
       
        try :  
            connection = HTTPConnection(self.url, self.port)
            
            if httpmethod == "GET" :
                connection.request(httpmethod, callurl + "?" + params)
            elif httpmethod == "POST" :
                connection.request(httpmethod, callurl, params, headers)
            else :
                raise ValueError("Unknown HTTP Method " + str(httpmethod))
           
            response = connection.getresponse().read()
            return response 
            
        except Exception as e : 
            raise e
        finally:
            connection.close()
            
        
        return response
    
    
    @property
    def iface(self):
        return self._iface
    @iface.setter
    def iface(self, name):
        self._iface = name + "/"
    
    @property
    def method(self):
        return self._method 
    @method.setter
    def method(self, name):
        self._method = name + "/"
    
    @property
    def extra(self):
        return self._extra
    @extra.setter
    def extra(self, extra):
        for i in extra :
            self._extra +=  i + "/"
    
    @property 
    def params(self):
        return self._params 
    @params.setter
    def params(self, params):
        self._params = urllib.urlencode(params)


class SteamAPICaller(WebAPICaller):
    '''
    classdocs
    '''
    
    STEAM_API_KEY = "6ACD0FCADEA5029D7DE52608A7C711DF"
    STEAM_API_HOST = "api.steampowered.com"
    
    @staticmethod
    def steamIDToCommunityID(i):
        u = str(i).split(":")
        return (int(u[1]) * 2) + 0x0110000100000000 + int(u[0])

    def call(self):
        return json.loads(self.sendCall())
    
    @property
    def params(self):
        return self._params
    @params.setter
    def params(self, params):
        if 'key' not in params:
            raise ValueError("Steam API Key is Required")
        else :
            self._params = urllib.urlencode(params)

#Example    
#caller = SteamAPICaller(SteamAPICaller.STEAM_API_HOST)
#caller.iface ="ISteamUser"
#caller.method = "GetPlayerSummaries"
#caller.extra = ["v0002"]
#caller.params = {"key" : SteamAPICaller.STEAM_API_KEY, "steamids" : "76561198060331549"}
#response = caller.call()
#print response

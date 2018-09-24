from pyteamcity import TeamCity
import json

def jprint(*args):
    print(json.dumps(args, indent=4))
if __name__=='__main__':
    teamcityUser = 'admin'
    teamcityPassword = 'iniT1234'
    teamcityServer = '127.0.0.1'
    teamcityPort = 8111
    teamcityProtocol = 'http'

    myApp = TeamCity(username=teamcityUser, password=teamcityPassword, server=teamcityServer, port=teamcityPort,
                     protocol=teamcityProtocol)
    print(myApp.create_project("test project 2"))
    print(myApp.create_group("test group 2"))

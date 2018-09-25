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
    print(myApp.get_parent_groups("TEST_GROUP_2"))
    print(myApp.set_parent_group("TEST_GROUP_2", "ALL_USERS_GROUP", "TEST_GROUP"))

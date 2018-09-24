from pyteamcity import TeamCity

if __name__=='__main__':
    teamcityUser = 'admin'
    teamcityPassword = 'iniT1234'
    teamcityServer = '127.0.0.1'
    teamcityPort = 8111
    teamcityProtocol = 'http'

    myApp = TeamCity(username=teamcityUser, password=teamcityPassword, server=teamcityServer, port=teamcityPort,
                     protocol=teamcityProtocol)
    print(myApp.base_url)

from pyteamcity import TeamCity
import json

def jprint(*args):
    print(json.dumps(args, indent=4))

def plan(tc, project_name):
    #Create project
    tc.create_project(project_name)
    #Create groups
    tc.create_groups_for_project(project_name)
    #Create hierarchy
    tc.set_parent_hierarchy(project_name)

if __name__=='__main__':
    teamcityUser = 'admin'
    teamcityPassword = 'iniT1234'
    teamcityServer = '127.0.0.1'
    teamcityPort = 8111
    teamcityProtocol = 'http'

    tc = TeamCity(username=teamcityUser, password=teamcityPassword, server=teamcityServer, port=teamcityPort,
                     protocol=teamcityProtocol)

    #Generate names
    project_name = "My Super Project"
    plan(tc, project_name)

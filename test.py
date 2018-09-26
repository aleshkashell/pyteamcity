from pyteamcity import TeamCity
import json
import sys
import logging
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)
def jprint(*args):
    print(json.dumps(args, indent=4))

def plan(tc, project_name):
    if (len(project_name.replace(' ', ''))) > 15:
        print("Name of project too long", file=sys.stderr)
        return
    #Create project
    tc.create_project(project_name)
    #Create groups
    tc.create_groups_for_project(project_name)
    #Create hierarchy
    tc.set_parent_hierarchy(project_name)
    #Assign roles
    tc.assign_default_roles(project_name)

if __name__=='__main__':
    teamcityUser = 'admin'
    teamcityPassword = 'iniT1234'
    teamcityServer = '127.0.0.1'
    teamcityPort = 8111
    teamcityProtocol = 'http'

    tc = TeamCity(username=teamcityUser, password=teamcityPassword, server=teamcityServer, port=teamcityPort,
                     protocol=teamcityProtocol)

    #Generate names
    project_name = "BA Arena"
    plan(tc, project_name)

    #plan(tc, project_name)
    #print(tc.assign_role(group_name=group_name, project_name=project_name, role='PROJECT_VIEWER'))

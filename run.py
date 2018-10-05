from pyteamcity import TeamCity
import json
import sys
import logging
import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument('--tcuser', action='store', type=str, default='admin')
    parser.add_argument('--tcpass', action='store', type=str, default='iniT1234')
    parser.add_argument('--tchost', action='store', type=str, default='127.0.0.1')
    parser.add_argument('--tcport', action='store', type=str, default='8111')
    parser.add_argument('--tcprotocol', action='store', type=str, default='http')
    parser.add_argument('--project_name', action='store', type=str, default='http')

    parameters = parser.parse_args()

    tc = TeamCity(username=parameters.tcuser, password=parameters.tcpass, server=parameters.tchost,
                  port=parameters.tcport, protocol=parameters.tcprotocol)

    #Generate names
    project_name = "BA Arena"
    plan(tc, parameters.project_name)

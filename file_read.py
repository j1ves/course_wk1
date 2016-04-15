#!/usr/bin/env python

import yaml, json
from pprint import pprint as pp

def read_yaml_file(filename):
    with open(filename, 'r') as f:
        data = yaml.load(f)
        f.close
    print "-"*20
    print "yaml file"
    print "-"*20
    pp(data)



def read_json_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        f.close
    print "-"*20
    print "json file"
    print "-"*20
    pp(data)




read_yaml_file('script_yaml.yaml')
read_json_file('script_json.json')
    

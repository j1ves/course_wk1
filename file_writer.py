#!/usr/bin/env python
import json, yaml

list = [1,2,3,4,5,{'test':'blah','test2':'blah2'}]

def write_yaml(filename,data):
    with open(filename, 'w') as f:
        f.write(yaml.dump(data, default_flow_style=False))
        f.close

def write_json(filename,data):
    with open(filename, 'w') as f:
        json.dump(data, f)
        f.close


write_yaml('script_yaml.yaml',list)
write_json('script_json.json',list)


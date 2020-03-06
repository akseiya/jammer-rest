#!/usr/bin/env python3

import requests, os, sys, yaml

def reverb(verb_str):
    verbs = {
        'PUT':    requests.put,
        'POST':   requests.post,
        'DELETE': requests.delete
    }
    return verbs[verb_str]

args = sys.argv
args.pop(0)

special_verb = args[0].upper()
data = False
if not special_verb in ['PUT', 'DELETE', 'POST']:
    verb = requests.get
else:
    verb_word = args.pop(0).upper()
    verb = reverb(verb_word)
    if verb_word  in ['PUT', 'POST']:
        data = yaml.safe_load(sys.stdin)
        sys.stderr.write("Data accepted.\n")

path = args.pop(0)
root = os.environ.get('JMBK_URI') or "http://0.0.0.0:5000/"
uri = root + path

json = data or None

req = verb(uri, json=json)

print(yaml.dump(req.json(), indent=4))

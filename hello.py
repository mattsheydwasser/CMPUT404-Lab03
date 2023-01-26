#!/usr/bin/env python3


import os, cgitb
import json

cgitb.enable()

# print all environment variables as json dict
print('Content-Type: application/json')
print()
print(json.dumps(dict(os.environ), indent=2))

# print the users browser settings as html
# print('Content-Type: text/html')
# print()
# print(f"<p>HTTP_USER_AGENT = {os.environ["HTTP_USER_AGENT"]} </p>")




#!/usr/bin/env python3


import os, cgitb
import json

cgitb.enable()
print('Content-Type: application/json')
print()
print(json.dumps(dict(os.environ), indent=2))

# print('Content-Type: text/html')
# print()
# print(f"<p>HTTP_USER_AGENT = {os.environ} </p>")




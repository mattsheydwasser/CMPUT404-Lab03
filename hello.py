#!/usr/bin/env python3
import os, cgitb

cgitb.enable()
for each in os.environ:
    print(os.environ[each])


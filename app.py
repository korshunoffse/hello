#!/usr/bin/env python3

import datetime
import os

def pr():
    now =datetime.datetime.now()
    print ("Hello {0}".format(now))


if __name__== "__main__":
    if "REQUEST_URI" in os.environ:
        print("Content-type: text-html\n\n")
    pr()

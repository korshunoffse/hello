#!/usr/bin/env python3

import datetime

def pr():
    now =datetime.datetime.now()
    print ("Hello {0}".format(now))


if __name__== "__main__":
    print("Content-type: text-html\n\n")
    pr()

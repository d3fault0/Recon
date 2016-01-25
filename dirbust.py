#!/usr/bin/python

import sys
import os
import subprocess

if len(sys.argv) != 4:
    print "Usage: dirbust.py <target url> <scan name>"
    sys.exit(0)

url = str(sys.argv[1])
name = str(sys.argv[2])
port = str(sys.argv[3])
folder = "./wordlists"

found = []
print('\033[1;34m[*]  Starting DIRBUSTER scan for {0}\033[1;m'.format(url))
for filename in os.listdir(folder):
    outfile = " -o " + "./results/" + name + "/" + name + "_dirb_" + filename + "_" + port
    DIRBSCAN = "dirb %s %s/%s %s -S -r" % (url, folder, filename, outfile)
    try:
        results = subprocess.check_output(DIRBSCAN, shell=True)
        resultarr = results.split("\n")
        for line in resultarr:
            if "+" in line or "==>" in line:
                 if line not in found:
                    found.append(line)
    except:
        pass

try:
    if found[0] != "":
        print('\033[1;32m[*]  Dirbuster found the following items...\033[1;m')
        for item in found:
            if ("CODE:200" in item or "DIRECTORY" in item):
                print "\033[1;32m    {0}\033[1;m".format(item)
except:
    print('\033[1;34m[*]  No items found during dirb scan of {0}\033[1;m'.format(url))







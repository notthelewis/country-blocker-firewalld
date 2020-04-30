#!/usr/bin/env python3.8

import os
import subprocess

basedir = os.getcwd()
shell_script = basedir + "/ipblock.sh"

def _block_ip(ip_range, protocol):
    a = ip_range
    p = protocol
    b = subprocess.Popen([shell_script, a, p], stdout=subprocess.PIPE)
    c = b.stdout.readline()
    return(c)

for subdir, dirs, files in os.walk(basedir):
    for file in files:
        filepath = subdir + os.sep + file
        if subdir.endswith("/v4") and filepath.endswith(".zone"):
            print(filepath)
            _block_ip(filepath, 'ipv4')


        if subdir.endswith("/v6") and filepath.endswith(".zone"):
            print(filepath)
            _block_ip(filepath, 'ipv6')



# 20/1/2023  Sulaiman Alhasawi
# If you dont have dnp3-discover , replace it with path/to/dnp3-info.nse

#!/usr/bin/env python

# Import modules
import subprocess

# Set up the command to search for DNP3 devices
cmd = "nmap -sU -p 20000-20500 --script dnp3-discover --open <remote server ip> > dnp3_devices.txt"

# Execute the command
subprocess.call(cmd, shell=True)

# Read the output of the command
with open('dnp3_devices.txt', 'r') as f:
    for line in f:
        if 'DNP3' in line:
            print (line)

#!/usr/bin/env python

# This version (V1) checks if there are ics ports open for a given host !
# This tool checks for open ICS protocols such as : Siemens, Modbus, Fox, DNP3 and  Rockwell . I will add more in the future
# Feel free to edit it. Suggestions are welcomed !
# Author:  @alhasawi , Sulaiman Alhasawi

#usage: python icsfinder.py -host host/ip
#Note: If you have python 3.x , use icsfinder-v3.py

import socket
import sys
import argparse

def check_ics(host):
    ics_ports = {'Siemens':102,'Modbus':502,'Fox':1911,'Fox':4911,'DNP3':20000,'Rockwell-EtherNetIp':44818} # ALl ports are TCP , except 'BACnet':47808 which is a UDP and is not included in the list !

    try:
        for key, port in ics_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5.0)
            result = sock.connect_ex((args.host,port))
            if result == 0:
               print "Port {} {}: 	 Open (TCP)".format(port,key)
            sock.close()

    except KeyboardInterrupt:
     print "You pressed Ctrl+C"
     sys.exit()

    except socket.gaierror:
     print 'Hostname could not be resolved. Exiting'
     sys.exit()

    except socket.error:
     print "Couldn't connect to server"
     sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scan an ICS port')
    parser.add_argument('-host', required=True, type=str, help='ip or hostname')
    args = parser.parse_args()
    host = args.host
    check_ics(host)

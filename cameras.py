# We want to map the camera MAC to IP using data collected from Wireshark

# Wireshark filter is: ip.dst == 255.255.255.255 and udp.port == 8848 
# Port 8848 UDP is used by MESSOA IP cameras as a heartbeat. Every few 
# seconds they send a small comma separated string: 
# $MessoaIPCamera,ipaddress,subnetmask,macaddress,port

# Input
# takes output from Wireshark file saved as plain text and parses it
# for IP to MAC mapping

# Output 
# CSV: MAC, IP

# --------------------

import re
import os
import sys
import csv

def create_list(line_num, data_line):
    "gets data information to write record to a file"
    # INPUT
    # data line number i.e. 0010, 0020, 0030, 0040
    # information to append to record 
    # we're using a dictionary data structure to avoid duplicate records
    # and we'll use the MAC as the key in the key:value pair


    global record
    global macpat
    global ippat
    global cameras
    
    if line_num == "0010":
    # this is a new data record of a camera
    # start new string record of the camera details
        record = data_line
    else: 
        # append to the string
        record = record + data_line

    if line_num == "0030":
    # This is the last data line with information we need -
    # find the MAC so we can see if this is a duplicate device - 
    # if not, add it to our list of devices and map its IP to it

        # look for mac address in record
        mac = macpat.search(record)
        if mac:
            mac_add = mac.group(0)
            # find the IP address in the record
            ip = ippat.search(record)
            ip_add = ip.group(0)

            # see if the MAC address is already in our list of devices
            # add it if not
            if mac_add not in cameras:
                cameras[mac_add] = ip_add
    return

# open pcap text file and parrse it to get the data we need
# look for the lines with the data
# data lines start with 4 digits followed by a space and then up to 16 hex pairs
# there are never more tha 5 lines of data in these messages: 
# 0000, 0010, 0020, 0030, 0040
# line 0000 always has the string "$MessoaIPCamera," so might as well skip it
# line 0040 always has the TCP/UDP port, so might as well skip that too
p = re.compile(r'(00[1-3]0)\s+')
# pattern for MAC
macpat = re.compile(r'([0-9a-fA-F]{2}:?){6}')
# pattern for IPv4
ippat = re.compile(r'([0-9]{1,3}\.?){4}')
# initialize record string to an empty string
record = ""
# initialize cameras dictionary to an empty dictionary
cameras = dict()

# open the file to read with the pcap in plain text
with open(input("Enter file to read: "),'r') as f:
    line = f.readline()
    while line:
        # look for data lines
        m = p.match(line)
        # parse data lines to get the information we want
        if m:
            # remove trailing \n from all data lines
            data_line = re.sub(r'\n',"",line)
            # remove hex data
            data_line = re.sub(r'(00[1-4]0)\s+((\w){2}(\s?))+',"",data_line)
            # remove all spaces in the line
            data_line = data_line.replace(" ", "")
            # sent line number and parsed data to add to list
            create_list(m.group(1), data_line)
        line = f.readline()
# write device list to a CSV file
with open(input("Enter filename to write: "),'w') as csvfile:
    devices = csv.writer(csvfile)
    # add header row
    devices.writerow(["MAC", "IP"])
    for key, val in cameras.items():
        devices.writerow([key, val]) 


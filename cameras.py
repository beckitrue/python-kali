# We want to map the camera MAC to IP using data collected from Wireshark
# 
# Wireshark filter is: ip.dst == 255.255.255.255 and udp.port == 8848 
# Port 8848 UDP is used by MESSOA IP cameras as a heartbeat. Every few 
# seconds they send a small comma separated string: 
# $MessoaIPCamera,ipaddress,subnetmask,macaddress,port

# Input
# takes output from Wireshark file saved as plain text and parses it
# for IP to MAC mapping

# Output 
# CSV MAC, IP, subnetmask, port 

# --------------------
# stuff to do to make this better - right now I fix it in Excel

# ask for location of data file - need to fix this to be interactive
#data_file = input ('path to file: ')
#print ('data file is: '+ data_file)

# need to get location of file to write to 

# need to put records in an indexed list or something index by MAC
# ----------------------

# open file and parrse it to get the data we need

# we're going to use regex
import re
import os

def append_data(line_num, data_line):
    "gets data information to write record to a file"
    # INPUT
    # data line number i.e. 0010, 0020, 0030, 0040
    # information to append to record 

    # if line is 0010, this is a new record so send a new line to file
    if line_num == "0010":
        record = "\n"+data_line
    else: 
        record = data_line
    print (record)
    # open the file to write to
    fmap.write(record)
    return

# look for the lines with the data
# data lines start with 4 digits followed by a space and then up to 16 hex pairs
# there are never more tha 5 lines of data in these messages: 
# 0000, 0010, 0020, 0030, 0040
# line 0000 always has the string "$MessoaIPCamera," so might as well skip it
p = re.compile(r'(00[1-4]0)\s+')

# open the file with the pcap in plain text
with open('/Users/becki/Desktop/pcaps/mapping.txt', 'a') as fmap, open('/Users/becki/Desktop/pcaps/cameras1', 'r') as f:
    line = f.readline()
    while line:
        m = p.match(line)
        if m:
            # remove trailing \n from all data lines
            data_line = re.sub(r'\n',"",line)
            # remove hex data
            data_line = re.sub(r'(00[1-4]0)\s+((\w){2}(\s?))+',"",data_line)
            # remove all spaces in the line
            data_line = data_line.replace(" ", "")
            append_data(m.group(1), data_line)
        line = f.readline()
f.closed()
fmap.closed()
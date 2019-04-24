#!/usr/bin/python

from packet_parser import *                             #Adds Elliots packet parser
#When I get Jacks code, import that too

files = ['Node1.txt','Node2.txt','Node3.txt','Node4.txt']       #List of files with the packet data we want
rqsent = 0
rqrecv = 0
rpsent = 0
rprecv = 0

def main():
    for f in files:
        if f == 'Node1.txt':
            ip = '192.168.100.1'
        if f == 'Node2.txt':
            ip == '192.168.100.2'
        if f == 'Node3.txt':
            ip = '192.168.200.1'
        if f == 'Node4.txt':
            ip == '192.168.200.2' 
        packetFile= 'blah'                               #pass f through Jacks functions
        packets = parse(packetFile)                      #Use Jacks output with elliots parse function
        for packet in packets:
            if packet[14] == '8' and packet[12]==ip:
                rqsent +=1                              #of echo requests sent (type 8)
            if packet[14] == '0'and packet[12]==ip: 
                rpsent +=1                              #of echo replies sent (type 0)
            if packet[14] == '8' and packet[13]==ip:
                rqrecv+=1                               #of echo requests recieved
            if packet[14] == '0' and packet[13]==ip:
                rpsent +=1                              #of echo replies recieved
            #Total echo request bytes sent
            #Total echo request bytes recv
            #Total echo request data sent
            #Total echo request data recv
        return
#!/usr/bin/python

from packet_parser import *                                 #Adds Elliots packet parser
from Packet_Filtering import *                               #When I get Jacks code, import that too

files = ['Node1.txt','Node2.txt','Node3.txt','Node4.txt']       #List of files with the packet data we want

def main():
    for f in files:
        rqsent = int(0)
        rqrecv = int(0)
        rpsent = int(0)
        rprecv = int(0)
        totrqdata = int(0)
        totrpdata = int(0)
        bytesrecv = int(0)
        bytesent = int(0)
        if f == 'Node1.txt':
            ip = '192.168.100.1'
        elif f == 'Node2.txt':
            ip = '192.168.100.2'
        elif f == 'Node3.txt':
            ip = '192.168.200.1'
        elif f == 'Node4.txt':
            ip = '192.168.200.2' 
        read(f)                                                 #pass f through Jacks functions
        packets = parse('goodstuff.txt')                        #Use Jacks output with elliots parse function
        for packet in packets:
            if packet[14] == '8' and packet[12]==ip:
                rqsent += 1                                     #of echo requests sent (type 8)
                totrqdata += int(packet[18])                    #Total echo request data sent
                bytesent += int(packet[18]) + 42                #Total bytes sent
            if packet[14] == '0'and packet[12]==ip: 
                rpsent += 1                                     #of echo replies sent (type 0)
                totrpdata += int(packet[18])                    #Total echo reply data sent
                bytesent += int(packet[18]) + 42                #Total bytes sent
            if packet[14] == '8' and packet[13]==ip:
                rqrecv+= 1                                      #of echo requests recieved
                totrqdata += int(packet[18])                    #Total echo request data recieved
                bytesrecv += int(packet[18]) + 42               #Total bytes received
            if packet[14] == '0' and packet[13]==ip:
                rprecv += 1                                     #of echo replies recieved
                totrpdata += int(packet[18])                    #Total echo reply data recieved
                bytesrecv += int(packet[18]) + 42               #Total bytes received
        return

if __name__ == '__main__':
    main()
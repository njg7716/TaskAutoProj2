#!/usr/bin/python

from packet_parser import *                                     #Adds Elliots packet parser
from packet_filtering import *                                  #When I get Jacks code, import that too

files = ['Node1.txt']       #List of files with the packet data we want

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
        sumtime = float(0)
        i = int(0)
        delay = float(0)
        tothops = int(0)
        if f == 'Node1.txt':
            ip = '192.168.100.1'
        elif f == 'Node2.txt':
            ip = '192.168.100.2'
        elif f == 'Node3.txt':
            ip = '192.168.200.1'
        elif f == 'Node4.txt':
            ip = '192.168.200.2' 
        read(f)                                                     #pass f through Jacks functions
        packets = parse('goodstuff.txt')                            #Use Jacks output with elliots parse function
        while i < len(packets):
            if packets[i][14] == '8' and packets[i][12]==ip:
                rqsent += 1                                         #of echo requests sent (type 8)
                totrqdata += int(packets[i][18])                    #Total echo request data sent
                bytesent += int(packets[i][18]) + 42                #Total bytes sent
                time1 = float(packets[i][20])
                temp = packets[i+1]
                time2 = temp[20]
                sumtime += time2 - time1
            if packets[i][14] == '0'and packets[i][12]==ip: 
                rpsent += 1                                         #of echo replies sent (type 0)
                totrpdata += int(packets[i][18])                    #Total echo reply data sent
            if packets[i][14] == '8' and packets[i][13]==ip:
                rqrecv+= 1                                          #of echo requests recieved
                totrqdata += int(packets[i][18])                    #Total echo request data recieved
                bytesrecv += int(packets[i][18]) + 42               #Total bytes received
                time1 = float(packets[i][20])
                temp = packets[i+1]
                time2 = temp[20]
                delay = time2 - time1
                ttl = int(packets[i][9])
                tothops = 128 - ttl
            if packets[i][14] == '0' and packets[i][13]==ip:
                rprecv += 1                                         #of echo replies recieved
                totrpdata += int(packets[i][18])                    #Total echo reply data recieved
                bytesrecv += int(packets[i][18]) + 42               #Total bytes received
        avgtime = sumtime/rqsent                                    #Average Round Trip Time
        rqthroughput = (totrqdata/sumtime)/1000                     #Echo Request Throughput in kB/sec
        goodput = (bytesent/sumtime)/1000                           #Echo Request Goodput (kB/sec)
        delay = delay/float(rqrecv)                                 #Average Reply Delay
        avghops = tothops/rqrecv                                    #Average number of Hops Per Echo Request

        output = open('output.csv', 'a+')
        output.write(f + '\n\n')
        output.write('Echo Requests Sent, Echo Requests Received, Echo Replies Sent, Echo Replies Received\n')
        output.write(rqsent+','+rqrecv+','+rpsent+','+rprecv+'\n')
        output.write('Echo Requests Bytes Sent (bytes), Echo Requests Data Sent (bytes)')
        output.write(bytesent +','+totrqdata)
        output.close()
        i += 1

        return

if __name__ == '__main__':
    main()
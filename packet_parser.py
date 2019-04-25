InputFile = 'example.txt'


def parse(InputFile) :
    bigarray = []
    #print 'called parse function in packet_parser.py'
    f = open(InputFile)
    line = f.readline()
    while line:
        if line != '\n' and line != '':
            line = f.readline()
            line = line.split()
            time = line[1]
            #print(line)
            line = f.readline()
            #print(line)
            line = f.readline()
            #print(line)
            buildarray = []
            while  line != '\n' and line != '':
                #print(line)
                x = line.strip()
                x = x.split(' ')
                #print(x)
                x = x[2:-3]
                #print(x)
                counter = 0
                for i in x:
                    if i == '':
                        counter += 1
                        if counter == 2:
                            break
                    if i != '':
                        buildarray.append(i)
                line = f.readline()
            line = f.readline()
            #print(buildarray)
            addinfo(buildarray, bigarray, time)
        #line = f.readline()
        #line = f.readline()
    f.close()
    #print(bigarray)
    return(bigarray)


def addinfo(framearray, bigarray, time) :
    DestinationMAC = framearray[0] + ':' + framearray[1] + ':' + framearray[2] + ':' + framearray[3] + ':' + framearray[4] + ':' + framearray[5]
    SourceMAC = framearray[6] + ':' + framearray[7] + ':' + framearray[8] + ':' + framearray[9] + ':' + framearray[10] + ':' + framearray[11]
    EthernetType = int('0x' + framearray[12] + framearray[13], 0)
    IPVersion = int('0x' + framearray[14][0], 0)
    IHL = int('0x' + framearray[14][1],0)
    DSCPECN = int('0x' + framearray[15], 0)
    PacketLength = int('0x' + framearray[16] + framearray[17], 0)
    Identification = int('0x' + framearray[18] + framearray[19], 0)
    FlagsFragmentOffset = int('0x' + framearray[20] + framearray[21], 0)
    TimeToLive = int('0x' + framearray[22], 0)
    Protocol = int('0x' + framearray[23], 0)
    HeaderChecksum = int('0x' + framearray[24] + framearray[25], 0)
    SourceIPAddress = str(int('0x' + framearray[26], 0)) + '.' + str(int('0x' + framearray[27], 0)) + '.' + str(int('0x' + framearray[28], 0)) + '.' + str(int('0x' + framearray[29], 0))
    DestinationIPAddress = str(int('0x' + framearray[30], 0)) + '.' + str(int('0x' + framearray[31], 0)) + '.' + str(int('0x' + framearray[32], 0)) + '.' + str(int('0x' + framearray[33], 0))
    ICMPType = int('0x' + framearray[34], 0)
    ICMPCode = int('0x' + framearray[35], 0)
    ICMPChecksum = int('0x' + framearray[36] + framearray[37], 0)
    ICMPRestofHeader = int('0x' + framearray[38] + framearray[39] + framearray[40] + framearray[41], 0)
    ICMPDataLength = PacketLength - 28
    ICMPData = ''
    time = float(time)
    q = 0
    while q < ICMPDataLength:
        ICMPData += (chr(int('0x' + framearray[42 + q], 0)))
        q += 1

    """
    print('')
    print('DestinationMAC ' + str(DestinationMAC))
    print('SourceMAC ' + str(SourceMAC))
    print('EthernetType ' + str(EthernetType))
    print('IPVersion ' + str(IPVersion))
    print('IHL ' + str(IHL))
    print('DSCPECN ' + str(DSCPECN))
    print('PacketLength ' + str(PacketLength))
    print('Identification ' + str(Identification))
    print('FlagsFragmentOffset ' + str(FlagsFragmentOffset))
    print('TimeToLive ' + str(TimeToLive))
    print('Protocol ' + str(Protocol))
    print('HeaderChecksum ' + str(HeaderChecksum))
    print('SourceIPAddress ' + str(SourceIPAddress))
    print('DestinationIPAddress ' + str(DestinationIPAddress))
    print('ICMPType ' + str(ICMPType))
    print('ICMPCode ' + str(ICMPCode))
    print('ICMPChecksum ' + str(ICMPChecksum))
    print('ICMPRestofHeader ' + str(ICMPRestofHeader))
    print('ICMPDataLength ' + str(ICMPDataLength))
    print('ICMPData ' + str(ICMPData))
    print('Time ' + str(time))
    print('')
    """
    bigarray.append([DestinationMAC, SourceMAC, EthernetType, IPVersion, IHL, DSCPECN, PacketLength, Identification, FlagsFragmentOffset, TimeToLive, Protocol, HeaderChecksum, SourceIPAddress, DestinationIPAddress, ICMPType, ICMPCode, ICMPChecksum, ICMPRestofHeader, ICMPDataLength, ICMPData, time])

#parse(InputFile)

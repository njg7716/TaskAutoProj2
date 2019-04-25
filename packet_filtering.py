import sys, os

def read(f):
        with open(f) as flie:
                for i, l in enumerate(flie):
                        pass
        size = i + 1
        print size
        h = 0

        f = open(f,'r')
        line = f.readline().strip()
        #print line

        space = "\n"
        clue = open('goodstuff.txt','w')
        clue.write(space)

        while h < size:
                if(line.find("No.") == 0):
                        line = f.readline().strip()
                        #print line
                        #print line.find("Echo (ping) reply")
                        if(line.find("Echo (ping) reply") != -1 or line.find("Echo (ping) request") != -1):
                                g = 0
                                while True:
                                        clue.write(line+space)
                                        line = f.readline().strip()
                                        if(len(line) == 0 and g > 1):
                                                clue.write(space)
                                                break
                                        g += 1
                line = f.readline().strip()

                #print line
                h += 1





hold = sys.argv[1]

read(hold)


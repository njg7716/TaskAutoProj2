import sys, os

def read(f):
        with open(f) as flie:
                for i, l in enumerate(flie):
                        pass
        size = i + 1
        h = 0

        f = open(f,'r')
        line = f.readline().strip()
        No = line
	

        space = "\n"
        clue = open('goodstuff.txt','w')
        
        while h < size:
                if(line.find("No.") == 0):
                        line = f.readline()
                        if(line.find("Echo (ping) reply") != -1 or line.find("Echo (ping) request") != -1):
                                g = 0
				clue.write(No+space)
                                while True:
					if(g == 0):
				                clue.write(line)
						g += 1
						line = f.readline().strip()
					else:
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


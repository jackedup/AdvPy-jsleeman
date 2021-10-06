import sys

paircount = 0;
linenum = 0
numberlist = []
def getRanges(a,b):
	newlist = []
	for x in range(int(a), int(b)+1):
		newlist.append(x)
	numberlist.append(newlist)

def checkOverlap():
	for x in numberlist:
		for y in x:
			numb = 0
			for a in numberlist:
				for b in a:
					if (b == y):
						numb = numb + 1
						if (numb >= paircount):
							return True
							
	return False
line1 = True;

for line in sys.stdin:
	if(line1):
		paircount = int(line)
		line1 = False
	else:
		getRanges(line.split()[0], line.split()[1])
		linenum+=1
	if(linenum == paircount):
		if (checkOverlap()):
			print("gunilla has a point")
		else:
			print("edward is right")
		quit()


		

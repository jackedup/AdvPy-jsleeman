import sys

paircount = 0
linenum = 0
numberlist = []
def getRanges(a,b):
	newlist = []
	for x in range(int(a), int(b)+1):
		newlist.append(x)
	numberlist.append(newlist)

def checkOverlap():
	global paircount
	global numberlist
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

line1 = True
def initVars():
	global line1
	global linenum
	global paircount
	global numberlist
	line1 = True
	linenum = 0
	paircount = 0
	numberlist = []
def eval(line):
	global line1
	global linenum
	global paircount
	global numberlist
	if(line1):
		paircount = int(line)
		line1 = False
	else:
		getRanges(line.split()[0], line.split()[1])
		linenum+=1
	if(linenum == paircount):
		if (checkOverlap()):
			initVars()
			return("gunilla has a point")
		else:
			initVars()
			return("edward is right")
	return None

if __name__ == '__main__':
	for lin in sys.stdin:
		result = eval(lin)
		if (result != None):
			print(result)
		

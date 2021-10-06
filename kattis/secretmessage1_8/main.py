import sys
linecount =0
firstline = True
for line in sys.stdin:
	if (firstline):
		linecount = int(line)
		firstline = False
	else:

		linelen = len(line) -1
		squarew = 1;
		puzzle = []
		#print(linelen)
		while(squarew*squarew < linelen):
			squarew+=1
		i = 0
		temp = []

		for ch in line:
			if (ch == "\n"):
				break
			if (i < squarew -1):
				temp.append(ch)
				i=i+1
			else:
				temp.append(ch)
				puzzle.append(temp)
				temp = []
				i = 0
		
		for num in range(linelen, squarew*squarew):
			if (i <	squarew -1):
				temp.append('*')
				i+=1
			else:
				temp.append('*')
				puzzle.append(temp)
				temp = []
				i = 0
		
		word = ""
		
		#for i in puzzle:
		#	print(i, end='')
		#	print()
		
		for x in range(0,squarew):
			for y in range(squarew,0, -1):
					if(puzzle[y-1][x] != '*'):
						print(puzzle[y-1][x], end='')
		print()
		
			

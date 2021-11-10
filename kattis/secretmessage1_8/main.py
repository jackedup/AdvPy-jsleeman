import sys
linecount = 0
firstline = True

def eval(line):
    global linecount
    global firstline
    if (firstline):
        linecount = int(line)
        firstline = False
        return
    else:

        linelen = len(line) -1
        squarew = 1
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
            if (i <    squarew -1):
                temp.append('*')
                i+=1
            else:
                temp.append('*')
                puzzle.append(temp)
                temp = []
                i = 0
        
        word = ""
        
        #for i in puzzle:
        #    print(i, end='')
        #    print()
        tempout = ""
        for x in range(0,squarew):
            for y in range(squarew,0, -1):
                    if(puzzle[y-1][x] != '*'):
                        tempout += puzzle[y-1][x]
        return tempout
if __name__ == '__main__':
    for lin in sys.stdin:
        if(firstline):
            eval(lin) #burns off number of lines since I dont use it
        else:
            print(eval(lin))
		
			

import sys
def eval(line, h, w, n):
	brickline = line.split()
	totalh =0
	totalw =0
	for brick in brickline:
		if (totalw + int(brick) == w):
			totalh +=1	
			totalw += int(brick)
			if (totalw == w and totalh == h):
				return("YES")
			totalw = 0
		elif (totalw + int(brick) > w):
			return("NO")
		else:
			totalw += int(brick)
	return("NO")	

if __name__ == "__main__":

	firstline = sys.stdin.readline().split()
	h = int(firstline[0])
	w = int(firstline[1])
	n = int(firstline[2])
	print(eval(sys.stdin.readline(), h, w, n))
	
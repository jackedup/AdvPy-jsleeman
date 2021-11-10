import sys

def convertchar(ch):
	if(ch == "a"):
		return "@"
	elif(ch == "b"):
		return 8
	elif(ch == 'c'):
		return '('
	elif(ch == 'd'):
		return '|)'
	elif(ch == 'e'):
		return '3'
	elif(ch == 'f'):
		return '#'
	elif(ch == 'g'):
		return '6'
	elif(ch == 'h'):
		return '[-]'
	elif(ch == 'i'):
		return '|'
	elif(ch == 'j'):
		return '_|'
	elif(ch == 'k'):
		return '|<'
	elif(ch == 'l'):
		return '1'
	elif(ch == 'm'):
		return '[]\/[]'
	elif(ch == 'n'):
		return '[]\[]'
	elif(ch == 'o'):
		return '0'
	elif(ch == 'p'):
		return '|D'
	elif(ch == 'q'):
		return '(,)'
	elif(ch == 'r'):
		return '|Z'
	elif(ch == 's'):
		return '$'
	elif(ch == 't'):
		return '\'][\''
	elif(ch == 'u'):
		return '|_|'
	elif(ch == 'v'):
		return '\/'
	elif(ch == 'w'):
		return '\/\/'
	elif(ch == 'x'):
		return '}{'
	elif(ch == 'y'):
		return '`/'
	elif(ch == 'z'):
		return '2'
	else:
		return ch
def eval(line):
	result = ""			
	for ch in line:
		result += (convertchar(ch.lower()))
	return result
if __name__ == '__main__':
	for line in sys.stdin:
		print(eval(line))
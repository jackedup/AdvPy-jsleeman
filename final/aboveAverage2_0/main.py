import sys
C =0

persons = []
linenum =0
def eval(input):
    global linenum
    aboveaveragepercent = 0.0
    outputstring = ""
    for line in input.split("\n"):
        if linenum == 0:
            print(line)
            C = line[0]
            linenum += 1
        elif line.strip():
           # if linenum > 1:
            #    outputstring += '\n'
            linenum += 1
            print(line)
            line.strip()
            list = line.split(" ")
            print(list)
            n = int(list[0])
            del list[0]
            print(list)
            #calculate the average
            total = 0
            for item in list:
                total += int(item)
            average = total / int(n)

            #check if score is above average
            aboveaverage = 0
            for item in list:
                if int(item) > average:
                    aboveaverage += 1
            
            #calc above average percent
            aboveaveragepercent = format(round(((aboveaverage / n) * 100),3), '.3f')
            outputstring += str(aboveaveragepercent) + "%\n"
    return(outputstring)

if __name__ == '__main__':
    kattisin = ""
    for line in sys.stdin:
        kattisin += line
    print(eval(kattisin))
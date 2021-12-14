import sys

persons = []
linenum =0
def eval(input):
    global linenum
    aboveaveragepercent = 0.0
    outputstring = ""
    input = input.split()
    C = int(input[0])
    del input[0]
    for i in range(0, C):
        N = int(input [0])
        del input[0]
        total = 0
        gradeList = []
        for j in range(0,N):
            newGrade = int(input[0])
            del input[0]
            gradeList.append(newGrade)
            total += int(newGrade)
            average = total / int(N)
            #check if score is above average
            aboveaverage = 0
        for item in gradeList:
            if int(item) > average:
                aboveaverage += 1
        
        #calc above average percent
        aboveaveragepercent = format(round(((aboveaverage / N) * 100),3), '.3f')
        outputstring += str(aboveaveragepercent) + "%\n"
    return(outputstring)

if __name__ == '__main__':
    kattisin = ""
    for line in sys.stdin:
        kattisin += line
    print(eval(kattisin))
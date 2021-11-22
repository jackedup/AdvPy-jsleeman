import sys
def eval(line):
    result = 0
    nums = line.split(',')
    numsize = len(nums)
    for num in nums:
        if num != '' and num != '\n':
            result += int(num) * (60**(numsize -1))
        numsize -= 1
    return result

if __name__ == '__main__':
    firstline = True
    for line in sys.stdin:
        if firstline:
            firstline = False
        else:
            print(eval(line))
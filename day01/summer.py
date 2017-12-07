

def getWeirdSum(s):
    if s[-1] == s[0]:
        sum = int(s[-1])
    else:
        sum = 0
    lastchar = s[0]
    for char in s[1:]:
        if char == lastchar:
            sum += int(lastchar)
        lastchar = char
    return sum

def getWeirdSum2(s):
    offset = len(s) / 2
    sum = 0
    for i in range(len(s)):
        if s[i] == s[(i+offset)%len(s)]:
            sum += int(s[i])
    return sum

def runTest(s, ans):
    sum = getWeirdSum(s)
    if sum == ans:
        print('test pass: ' + s + ' = ' + str(sum))
    else:
        print('test failed: '+s+' got '+str(sum)+'(ans='+str(ans)+')')
        return False
    return True

def runTest2(s, ans):
    sum = getWeirdSum2(s)
    if sum == ans:
        print('test pass: ' + s + ' = ' + str(sum))
    else:
        print('test failed: '+s+' got '+str(sum)+'(ans='+str(ans)+')')
        return False
    return True

def runTests():
    tests = [('1122',3), ('1111',4), ('1234',0), ('91212129',9)]
    for (captcha,sum) in tests:
        if not runTest(captcha, sum):
            return False
    return True

def runTests2():
    tests2 = [('1212',6), ('1221',0), ('123425',4), ('123123',12),('12131415',4)]
    for (captcha,sum) in tests2:
        if not runTest2(captcha, sum):
            return False
    return True


def solveMine():
    import sys
    filename = 'mycaptcha.txt'
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    sum = getWeirdSum(open(filename).read().strip())
    print('my captcha sum = ' + str(sum))

def solveMine2():
    import sys
    filename = 'mycaptcha2.txt'
    #if len(sys.argv) == 2:
    #    filename = sys.argv[1]
    sum = getWeirdSum2(open(filename).read().strip())
    print('my captcha2 sum = ' + str(sum))


def run():
    if runTests():
        solveMine()

def run2():
    if runTests2():
        solveMine2()


if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 01 ---')
    #run()
    run2()

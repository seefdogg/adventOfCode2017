

def getWeirdSum(s):
    lastchar = s[0]
    sum = 0
    for char in s[1:]:
        if char == lastchar:
            sum += int(lastchar)
        lastchar = char
    if lastchar == s[0]:
        sum += int(lastchar)
    return sum

def runTest(s, ans):
    sum = getWeirdSum(s)
    if sum == ans:
        print('test pass: ' + s + ' = ' + str(sum))
    else:
        print('test failed: '+s+' got '+str(sum)+'(ans='+str(ans)+')')
        return False
    return True

def runTests():
    tests = {'1122':3, '1111':4, '1234':0, '91212129':9}
    for key in tests.keys():
        if not runTest(key, tests[key]):
            return False
    return True

def run():
    if runTests():
        sum = getWeirdSum(open('mycaptcha.txt').read())
        print('my captcha sum = ' + str(sum))

if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 01 ---')
    run()

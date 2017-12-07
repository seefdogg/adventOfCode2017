
def calcChecksum(lines):
    sum = 0
    for line in lines:
        min = 500000000
        max = 0
        for num in line.split():
            num = int(num)
            if num < min:
                min = num
            if num > max:
                max = num
        sum += max - min
    return sum

def calcChecksum2(lines):
    sum = 0
    for line in lines:
        nums = line.split()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (int(nums[i]) % int(nums[j]) == 0):
                    sum += int(nums[i]) / int(nums[j])
    return sum

def readfile(name):
    return open(name).readlines()

def run():
    tests = [(readfile('testinput.txt'),18)]
    for (data,checksum) in tests:
        res = calcChecksum(data)
        if res != checksum:
            print('test failed: returned '+str(res)+', correct = '+str(checksum))
        else:
            print('test passed')
    res = calcChecksum(readfile('input1.txt'))
    print('my checksum is ' + str(res))

def run2():
    tests = [(readfile('testinput2.txt'),9)]
    for (data,checksum) in tests:
        res = calcChecksum2(data)
        if res != checksum:
            print('test failed: returned '+str(res)+', correct = '+str(checksum))
        else:
            print('test passed')
    res = calcChecksum2(readfile('input2.txt'))
    print('my checksum2 is ' + str(res))

if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 02 ---')
    run2()


def run(data):
    numlines = len(data)
    offsets = []
    for line in data:
        offsets.append(int(line))

    i = 0
    steps = 0
    while (i >= 0) and (i < numlines):
        offsets[i] = offsets[i] + 1
        i += offsets[i] - 1
        steps += 1
    print('num steps to escape part one is '+str(steps))

def run2(data):
    numlines = len(data)
    offsets = []
    for line in data:
        offsets.append(int(line))

    i = 0
    steps = 0
    while (i >= 0) and (i < numlines):
        change = 1
        if offsets[i] >= 3:
            change = -1
        offsets[i] = offsets[i] + change
        i += offsets[i] - change
        steps += 1
    print('num steps to escape part two is '+str(steps))


if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 05 ---')
    data = open('input1.txt').readlines()
    run(data)
    run2(data)

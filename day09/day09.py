
def run(data):
    garbage = False
    depth = 0
    ignore = False
    score = 0
    garbageChars = 0
    for c in data:
        if ignore:
            ignore = False
            continue
        if garbage:
            if c == '!':
                ignore = True
            elif c == '>':
                garbage = False
            else:
                garbageChars += 1
        else: # not garbage
            if c == '{':
                depth += 1
            elif c == '}':
                score += depth
                depth -= 1
            elif c == '<':
                garbage = True
    return (score, garbageChars)

if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 09 ---')
    data = open('input1.txt').read()
    (score, garbageChars) = run(data)
    print('(part 1) score is '+str(score))
    print('(part 2) garbage chars = '+str(garbageChars))


def distance(x, y):
    return abs(x) + abs(y) - ((abs(x)+1)/2)

def run(moves):
    x = 0
    y = 0
    maxdist = 0
    for m in moves:
        m = m.strip()
        if m == 'n':
            y -= 1
        elif m == 'ne':
            if (abs(x) % 2) == 1:
                y -= 1
            x += 1
        elif m == 'se':
            if (abs(x) % 2) == 0:
                y += 1
            x += 1
        elif m == 's':
            y += 1
        elif m == 'sw':
            if (abs(x) % 2) == 0:
                y += 1
            x -= 1
        elif m == 'nw':
            if (abs(x) % 2) == 1:
                y -= 1
            x -= 1
        else:
            print('error')
            quit()
        curdist = distance(x,y)
        if curdist > maxdist:
            maxdist = curdist

    print('({:d},{:d})'.format(x,y))
    return (distance(x,y), maxdist)


if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 11 ---')
    fname = 'input1.txt'
    import sys
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    f = open(fname)
    data = f.read().split(',')
    f.close()
    (steps, maxdist) = run(data)
    print('(part 1) number of steps away: '+str(steps))
    print('(part 2) max distance away: '+str(maxdist))

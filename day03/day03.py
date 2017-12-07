
MY_NUM = 347991
GOING_RIGHT = 0
GOING_UP    = 1
GOING_LEFT  = 2
GOING_DOWN  = 3

def run(n):
    #print('running for n='+str(n))
    x = 0
    y = 0
    maxy = 0
    miny = 0
    minx = 0
    maxx = 0
    direction = GOING_RIGHT
    for i in range(2, n+1):
        #if i % 1000 == 0:
        #    print('['+str(i)+'] x='+str(x)+', y='+str(y))
        if direction == GOING_RIGHT:
            x += 1
            if x > maxx:
                direction = GOING_UP
                maxx = x
        elif direction == GOING_UP:
            y += 1
            if y > maxy:
                direction = GOING_LEFT
                maxy = y
        elif direction == GOING_LEFT:
            x -= 1
            if x < minx:
                direction = GOING_DOWN
                minx = x
        elif direction == GOING_DOWN:
            y -= 1
            if y < miny:
                direction = GOING_RIGHT
                miny = y
    return abs(x) + abs(y)

def getGridVal(grid, x, y):
    if (x,y) in grid:
        return grid[(x,y)]
    else:
        return 0

def getSum(grid, x, y):
    sum = 0
    sum += getGridVal(grid, x-1, y)
    sum += getGridVal(grid, x-1, y-1)
    sum += getGridVal(grid, x, y-1)
    sum += getGridVal(grid, x+1, y-1)
    sum += getGridVal(grid, x+1, y)
    sum += getGridVal(grid, x+1, y+1)
    sum += getGridVal(grid, x, y+1)
    sum += getGridVal(grid, x-1, y+1)
    return sum

def run2(n):
    #print('running for n='+str(n))
    grid = {(0,0):1} # dictionary, (x,y):value
    x = 0
    y = 0
    maxy = 0
    miny = 0
    minx = 0
    maxx = 0
    direction = GOING_RIGHT
    cursum = 1
    while cursum <= n:
        if direction == GOING_RIGHT:
            x += 1
            if x > maxx:
                direction = GOING_UP
                maxx = x
        elif direction == GOING_UP:
            y += 1
            if y > maxy:
                direction = GOING_LEFT
                maxy = y
        elif direction == GOING_LEFT:
            x -= 1
            if x < minx:
                direction = GOING_DOWN
                minx = x
        elif direction == GOING_DOWN:
            y -= 1
            if y < miny:
                direction = GOING_RIGHT
                miny = y
        grid[(x,y)] = getSum(grid, x, y)
        cursum = getGridVal(grid, x, y)
        print('x='+str(x)+' ,y='+str(y)+' sum='+str(cursum))
        if cursum > n:
            return cursum



if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 03 ---')
    import sys
    ans = 0
    if len(sys.argv) == 2:
        #ans1 = run(int(sys.argv[1]))
        ans2 = run2(int(sys.argv[1]))
    else:
        #ans1 = run(MY_NUM)
        ans2 = run2(MY_NUM)
    #print('(answer 1) the distance is '+str(ans))
    print('(answer 2) the first number is '+str(ans2))


def printBins(bins):
    s = '{:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d} ' +\
        '{:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d}'
    print(s.format(bins[0],bins[1],bins[2],bins[3],
                   bins[4],bins[5],bins[6],bins[7],
                   bins[8],bins[9],bins[10],bins[11],
                   bins[12],bins[13],bins[14],bins[15]))

def copyAndInsert(patterns, bins):
    b = []
    for i in range(16):
        b.append(bins[i])
    patterns.append(b)

def run(bins):
    for i in range(16):
        bins[i] = int(bins[i])

    done = False
    allocs = 0
    #printBins(bins)
    patterns = []
    copyAndInsert(patterns,bins)
    firsttime = 0
    while not done:
        allocs += 1
        maxx = -1
        highbin = 0
        for i in range(16):
            if bins[i] > maxx:
                highbin = i
                maxx = bins[highbin]
        bins[highbin] = 0
        i = (highbin+1) % 16
        while maxx > 0:
            bins[i] += 1
            i = (i + 1) % 16
            maxx -= 1
        if bins == [1,1,0,15,14,13,12,10,10,9,8,7,6,4,3,5]:
            if firsttime == 0:
                firsttime = allocs
        if bins in patterns:
            print('saw duplicate pattern after '+str(allocs)+' allocations')
            print('answer to part two is '+str(allocs-firsttime))
            done = True
        copyAndInsert(patterns,bins)
        #printBins(bins)
    return allocs

if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 06 ---')
    data = open('input1.txt').read().split()
    run(data)

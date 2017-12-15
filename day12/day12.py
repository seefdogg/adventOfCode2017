

def crawlnode(progmap, p, visited):
    #print('called for '+str(p))
    progs = progmap[p]
    for pr in progs:
        crawl = False
        if pr not in visited:
            crawl = True
        visited.add(pr)
        if crawl:
            crawlnode(progmap, pr, visited)

def run(lines):
    MAGIC_PROGRAM = 0
    progmap = {}
    for line in lines:
        items = line.split()
        cncprogs = []
        for prog in items[2:]:
            cncprogs.append(int(prog.strip(',')))
        progmap[int(items[0])] = cncprogs

    visited = set()
    crawlnode(progmap, MAGIC_PROGRAM, visited)
    return len(visited)

def run2(lines):
    progmap = {}
    for line in lines:
        items = line.split()
        cncprogs = []
        for prog in items[2:]:
            cncprogs.append(int(prog.strip(',')))
        progmap[int(items[0])] = cncprogs

    allsets = []
    for p in progmap.keys():
        visited = set()
        s = crawlnode(progmap, p, visited)
        if visited not in allsets:
            allsets.append(visited)
    #print allsets
    return len(allsets)

if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 12 ---')
    fname = 'input1.txt'
    import sys
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    f = open(fname)
    lines = f.readlines()
    f.close()
    ans = run(lines)
    print('(part 1) ans: '+str(ans))
    ans2 = run2(lines)
    print('(part 2) ans: '+str(ans2))

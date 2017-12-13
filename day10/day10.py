def hex2digit(n):
    h = hex(n)[2:]
    if len(h) == 1:
        h = '0' + h
    return h

def run2(lens):
    xlens = [17,31,73,47,23]
    NUM_ROUNDS = 64
    SIZE = 256

    ar = []
    for i in range(SIZE):
        ar.append(i)

    for x in xlens:
        lens.append(x)
    skip = 0
    pos = 0
    for rnd in range(NUM_ROUNDS):
        for length in lens:
            reversePartial(ar, pos, length)
            pos += length + skip
            skip += 1

    #for k in ar:
    #    print k

    densehash = []
    section = 0
    for section in range(16):
        xval = 0
        for j in range((section*16), (section*16)+16):
            xval ^= ar[j]
        densehash.append(xval)

    #for k in densehash: print hex(k)

    hash  = ''
    for v in densehash:
        hash += hex2digit(v)
    assert len(hash) == 32
    print('part 2, hash is '+hash)


def showList(a, desc):
    print(desc)
    for i in range(min(10,len(a))):
        print(str(a[i]))

def reversePartial(a, offset, n):
    #print('offset type is ' + str(type(offset)))
    #print('n type is ' + str(type(n)))
    if (offset+n) < len(a):
        tmp = []
        for i in range(offset,offset+n):
            tmp.append(a[i])
        for j in range(len(tmp)):
            a[offset+n-1-j] = tmp[j]
    else:
        b = []
        for i in range(len(a)):
            b.append(a[(i+offset)%len(a)])
        reversePartial(b, 0, n)
        for i in range(len(a)):
            a[(i+offset)%len(a)] = b[i]

def run(lens):
    for i in range(len(lens)):
        lens[i] = int(lens[i])

    SIZE = 256
    ar = []
    for i in range(SIZE):
        ar.append(i)

    skip = 0
    i = 0
    for length in lens:
        reversePartial(ar, i, length)
        i += length + skip
        skip += 1
    return ar[0]*ar[1]


if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 10 ---')
    f = open('input1.txt')
    data = f.read().split(',')
    f.close()
    ans = run(data)
    print('(part 1) product is '+str(ans))

    import sys
    fname = 'input1.txt'
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    print('processing '+fname)
    data = open(fname).read().strip()
    bites = []
    for c in data:
        bites.append(ord(c))
    run2(bites)

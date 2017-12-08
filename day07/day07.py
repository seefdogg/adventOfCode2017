

def run1(lines):
    bottoms = []
    tops = []
    for line in lines:
        a = line.split()
        bottoms.append(a[0])
        for i in range(3, len(a)):
            tops.append(a[i].strip(','))
    for line in lines:
        a = line.split();
        if a[0] not in tops:
            print(a[0] + ' must be on the bottom..')

class Node:
    def __init__(self, n, weight):
        self.name = n
        self.weight = weight

def getDepth(towers, name):
    if name not in towers:
        return 0

    maxx = -1
    for t in towers[name]:
        c = getDepth(towers, t)
        if c > maxx:
            maxx = c
    #print('depth at '+name+' is '+str(1+maxx))
    return 1 + maxx

def getWeight(nodes, towers, name):
    weight = nodes[name]
    if name in towers:
        for t in towers[name]:
            weight += getWeight(nodes, towers, t)
    return weight

def traverse(nodes, towers, name):
    if name in towers:
        subtows = len(towers[name])
        print('----- '+name+' has '+str(subtows)+' subtowers')
        subweights = {}
        for s in towers[name]:
            w = getWeight(nodes,towers,s)
            print(s+' has weight = '+str(w))
            if w in subweights:
                subweights[w] += 1
            else:
                subweights[w] = 1

        if len(subweights) == 1:
            print('all towers in '+name+' are good.. problem IN THIS ONE!')

        if subtows == 2:
            vals = subweights.values()
            if vals[0] == vals[1]:
                print('uh oh.. should not happen')
                quit()
            else:
                print('problem in one with two subtowers')
                quit()

        # more than 2 subtowers
        if 1 not in subweights.values():
            print('uh oh again')
            quit()

        foundit = False
        for s in towers[name]:
            if subweights[getWeight(nodes, towers, s)] == 1:
                if foundit:
                    print('uh oh 3 '+s)
                    quit()
                print('problem is in '+s)
                foundit = True
                traverse(nodes, towers, s)

        else:
            print('uh oh again')
            quit()



        for s in towers[name]:
            traverse(nodes, towers, s)


def run2(lines, filtered):
    nodes = {}
    for line in lines:
        a = line.split()
        #nodes.append(Node(a[0]], a[1].strip('()')))
        nodes[a[0]] = int(a[1].strip('()'))

    towers = {}
    for line in filtered:
        a = line.split()
        subs = []
        for i in range(3, len(a)):
            subs.append(a[i].strip(','))
        towers[a[0]] = subs

    maxx = -1
    bottom = ''
    for n in nodes:
        c = getDepth(towers, n)
        if c > maxx:
            maxx = c
            bottom = n

        w = getWeight(nodes, towers, n)
        #print('weight of '+n+' = '+str(w))

    print('bottom is '+bottom+' with '+str(maxx)+' layers')
    b = bottom
    traverse(nodes, towers, bottom)


if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 07 ---')
    filtered = open('filtered1.txt').read().splitlines()
    data = open('input1.txt').read().splitlines()
    #run1(filtered)
    run2(data, filtered)

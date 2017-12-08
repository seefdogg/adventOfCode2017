

class Instr:
    def __init__(self, line):
        items = line.split()
        self.reg = items[0]
        self.delta = int(items[2])
        if items[1] == 'dec':
            self.delta *= -1
        self.condreg = items[4]
        self.condrest = ' '.join(items[5:])


def run(rawdata):
    regs = {}
    maxval = -10000000
    for line in rawdata:
        ins = Instr(line)
        if ins.reg not in regs:
            regs[ins.reg] = 0
        if ins.condreg not in regs:
            regs[ins.condreg] = 0
        cond = str(regs[ins.condreg]) + ' ' + ins.condrest;
        if eval(cond):
            regs[ins.reg] += ins.delta
            if regs[ins.reg] > maxval:
                maxval = regs[ins.reg]

    maxx = regs.values()[0]
    for r in regs.keys():
        if regs[r] > maxx:
            maxx = regs[r]
            print('new max is '+r+' with value '+str(regs[r]))

    print('part 2, max value ever was '+str(maxval))

if __name__ == '__main__':
    print('--- Advent of Code 2017: Day 07 ---')
    data = open('input1.txt').readlines()
    run(data)

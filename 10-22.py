import re

class Noop:
    pass

class Addx:
    def __init__(self,val):
        self.num = val
        self.wait = 1
    def __str__(self):
        return "addx " + str(self.num)
    def __repr__(self):
        return "addx " + str(self.num)

def process(file):
    f = open(file,'r')
    cycle = 1
    reg = 1
    waiting = []
    total = 0
    checks = [20, 60, 100, 140, 180, 220]
    while True:
        line = f.readline()
        addx_search = re.search("addx ([-\d]+)",line)
        if re.search("noop",line):
            waiting.append(Noop())
            pass
        elif addx_search:
            waiting.append(Addx(int(addx_search.group(1))))

        el = waiting[0]
        if isinstance(el,Noop):
            waiting = waiting[1:]
        elif el.wait == 0:
            reg += el.num
            waiting = waiting[1:]
        else:
            el.wait -= 1

        
        
        cycle += 1

        for i in checks:
            if cycle == i:
                #print(cycle, ":", reg)
                total += reg * cycle

        #print("Cycle: ",cycle," reg: ",reg)

        if len(waiting) == 0:
            break
    return total



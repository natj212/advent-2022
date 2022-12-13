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
    print()
    f = open(file,'r')
    cycle = 1
    reg = 1
    waiting = []
    current_line = "#"
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

        if reg - 1 == cycle or reg == cycle or reg + 1 == cycle:
            current_line = current_line + "#"
        else:
            current_line = current_line + "."

        cycle += 1

        if cycle >= 40:
            print(current_line)
            cycle = 0
            current_line = ""

        if len(waiting) == 0:
            break
    


process("10-22-input.txt")

import re

class Modnum:
    def __init__(self, mods,num) -> None:
        self.mods = mods
        self.residues = []
        self.original = num
        for m in self.mods:
            self.residues.append(num % m)
    def __str__(self) -> str:
        return "Original" + str(self.original)
    
    def __repr__(self) -> str:
        return "Original" + str(self.original)
    

    def add(self,val):
        for i in range(0,len(self.mods)):
            self.residues[i] += val % self.mods[i]
            self.residues[i] = self.residues[i] % self.mods[i]
        

    def mult(self,val):
        for i in range(0,len(self.mods)):
            self.residues[i] = self.residues[i] * (val % self.mods[i]) % self.mods[i]
    

    def sqr(self):
        for i in range(0,len(self.mods)):
            self.residues[i] = (self.residues[i] * self.residues[i]) % self.mods[i]
        

    def divide3(self):
        for i in range(0,len(self.mods)):
            self.residues[i] = self.residues[i] // 3


def process(file):
    file_lines = []
    monkey = 0
    tempc = []
    collection = []
    operations = []
    mods = []
    true_throws = []
    false_throws = []
    monkey_count = [0] * 10
    rmonkey = "Monkey (\d+)"
    rstart = "Starting items:(.+)"
    roperation = "Operation: new = old (.) (.+)"
    rtest = "Test: divisible by (\d+)"
    rtrue = "If true: throw to monkey (\d+)"
    rfalse = "If false: throw to monkey (\d+)"


    f = open(file,'r')
    for line in f:
        file_lines.append(line)
        
    for line in file_lines:
        if re.search(rmonkey,line):
            monkey = int(re.search(rmonkey,line).group(1))
        elif re.search(rstart,line):
            
            c = list(map(int,re.search(rstart,line).group(1).split(",")))
            tempc.append(c)
        elif re.search(roperation,line):
            r = re.search(roperation,line)
            if r.group(2) == 'old':
                operations.append(('^',''))
            else:
                operations.append((r.group(1),r.group(2)))
        elif re.search(rtest,line):
            mods.append( int(re.search(rtest,line).group(1)))
        elif re.search(rtrue, line):
            true_throws.append(int(re.search(rtrue,line).group(1)))
        elif re.search(rfalse,line):
            false_throws.append(int(re.search(rfalse,line).group(1)))

    
    for el in tempc:
        collection.append(list(map(lambda x : Modnum(mods,x),el)))
        

    for round in range(10000):
        for monkey in range(0,len(operations)):
            for s in collection[monkey].copy():
                monkey_count[monkey] += 1
                
                if operations[monkey][0] == '+':
                    s.add(int(operations[monkey][1]))
                elif operations[monkey][0] == '*':
                    s.mult(int(operations[monkey][1]))
                elif operations[monkey][0] == '^':
                     s.sqr()
                #s.divide3()
                if s.residues[monkey] == 0:
                    collection[true_throws[monkey]].append(s)
                    collection[monkey].remove(s)
                else:
                    collection[false_throws[monkey]].append(s)
                    collection[monkey].remove(s)
    return monkey_count
                    

result = process("11-22-input.txt")
result.sort(reverse=True)
print(result[0] * result[1])

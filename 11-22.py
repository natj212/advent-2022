import re


def process(file):
    file_lines = []
    monkey = 0
    collection = []
    operation = ""
    test = 0
    true_throw = 0
    false_throw = 0
    monkey_count = [0] * 10
    rmonkey = "Monkey (\d+)"
    rstart = "Starting items:(.+)"
    roperation = "Operation: (.+)"
    rtest = "Test: divisible by (\d+)"
    rtrue = "If true: throw to monkey (\d+)"
    rfalse = "If false: throw to monkey (\d+)"

    for _ in range(10):
        collection.append([])

    f = open(file,'r')
    for line in f:
        file_lines.append(line)

    
    for round in range(20):
        
        for line in file_lines:
            if re.search(rmonkey,line):
                monkey = int(re.search(rmonkey,line).group(1))
            elif re.search(rstart,line):
                if round == 0:
                    exec("collection[monkey] = collection[monkey] + [" + re.search(rstart,line).group(1) + "]")
            elif re.search(roperation,line):
                operation = re.search(roperation,line).group(1)
            elif re.search(rtest,line):
                test = int(re.search(rtest,line).group(1))
            elif re.search(rtrue, line):
                true_throw = int(re.search(rtrue,line).group(1))
            elif re.search(rfalse,line):
                false_throw = int(re.search(rfalse,line).group(1))
            elif len(line) <= 2:
                for s in collection[monkey].copy():
                    monkey_count[monkey] += 1
                    ldic = {'old' : s}
                    exec(operation,ldic)
                    new = ldic['new']
                    worry = new // 3
                    if worry % test == 0:
                        collection[true_throw].append(worry)
                        collection[monkey].remove(s)
                    else:
                        collection[false_throw].append(worry)
                        collection[monkey].remove(s)
    return monkey_count
                    

result = process("11-22-input.txt")
result.sort()
print(result)

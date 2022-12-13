import re


def process(file):
    file_lines = []
    monkey = 0
    collection = []
    operations = []
    tests = []
    true_throws = []
    false_throws = []
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
        
    for line in file_lines:
        if re.search(rmonkey,line):
            monkey = int(re.search(rmonkey,line).group(1))
        elif re.search(rstart,line):
            exec("collection[monkey] = collection[monkey] + [" + re.search(rstart,line).group(1) + "]")
        elif re.search(roperation,line):
            operations.append( re.search(roperation,line).group(1))
        elif re.search(rtest,line):
            tests.append( int(re.search(rtest,line).group(1)))
        elif re.search(rtrue, line):
            true_throws.append(int(re.search(rtrue,line).group(1)))
        elif re.search(rfalse,line):
            false_throws.append(int(re.search(rfalse,line).group(1)))

    for round in range(20):
        for monkey in range(0,len(operations)):
            for s in collection[monkey].copy():
                monkey_count[monkey] += 1
                ldic = {'old' : s}
                exec(operations[monkey],ldic)
                new = ldic['new']
                worry = new // 3
                if worry % tests[monkey] == 0:
                    collection[true_throws[monkey]].append(worry)
                    collection[monkey].remove(s)
                else:
                    collection[false_throws[monkey]].append(worry)
                    collection[monkey].remove(s)
    return monkey_count
                    

result = process("11-22-input.txt")
result.sort()
print(result)

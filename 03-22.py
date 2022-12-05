def find_mistake(str):
    compa = str[:int((len(str)/2))]
    compb = str[int((len(str)/2)):]
    for l in compa:
        if l in compb:
            return l

def get_sum(file):
    f = open(file)
    count = 0
    for x in f:
        count += get_num(find_mistake(x))
    f.close()
    return count

def get_num(l):
    if ord(l) >= 97:
        return ord(l) - 96
    else:
        return ord(l) - 38

def get_badge(a, b, c):
    for l in a:
        if l in b and l in c:
            return l

def get_badge_sum(file):
    f = open(file)
    count = 0
    lines = []
    for x in f:
        lines.append(x)
        if len(lines) >= 3:
            count += get_num(get_badge(lines[0],lines[1],lines[2]))
            lines.clear()
    return count

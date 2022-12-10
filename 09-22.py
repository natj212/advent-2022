import math
import re

def move_closest(h,t):
    minn = 20
    min_dir = (0,0)
    for x in range(-1,2,1):
        for y in range(-1,2,1):
            d = get_distance(h, add(t,(x,y)))
            if d < minn:
                minn = d
                min_dir = (x,y)
    return min_dir
        

def get_distance(h,t):
    return math.sqrt(pow(t[0] - h[0],2) + pow(t[1] - h[1],2))


def add(a,b):
    return (a[0]+b[0],a[1]+b[1])

def get_moves(file):
    lst = []
    f = open(file,"r")
    
    for line in f:
        reg = re.search("([RLUD]) (\d+)",line)
        d = None
        if reg.group(1) == 'R':
            d = (1,0)
        elif reg.group(1) == 'L':
            d = (-1,0)
        elif reg.group(1) == 'D':
            d = (0,-1)
        elif reg.group(1) == 'U':
            d = (0,1)
        lst.append((d,int(reg.group(2))))
    return lst

def run(file):
    moves = get_moves(file)
    h = (0,0)
    t = (0,0)
    visited = set()
    for m in moves:
        count = m[1]
        while count > 0:
            h = add(h,m[0])
            if get_distance(h,t) >= 2:
                t = add(t,move_closest(h,t))
                visited.add(t)
            count -= 1
            #print("H:",h," ","T:",t)
    return visited

def get_once(m):
    count = 0
    for v in m.values():
        if v == 1:
            count +=1
    return count
    
print(len(run("09-22-input.txt")))
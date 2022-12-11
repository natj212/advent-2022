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
    return pow(t[0] - h[0],2) + pow(t[1] - h[1],2)


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
    knots = [(0,0)] * 10
    visited = set()
    for m in moves:
        count = m[1]
        while count > 0:
            knots[0] = add(knots[0],m[0])
            for i in range(0,9):
                if get_distance(knots[i],knots[i+1]) >= 4:
                    knots[i+1] = add(knots[i+1],move_closest(knots[i],knots[i+1]))
            visited.add(knots[9])
            count -= 1
    return len(visited)


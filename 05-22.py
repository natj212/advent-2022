import re

def get_stacks(file):
    stacks = []
    for line in file:
        index = 0
        while line:
            str = line[:4]
            line = line[4:]
            if re.search(" \d  ",str):
                return stacks
            elif re.search("    ",str):
                if len(stacks) <= index:
                    stacks.append([])
                index += 1
            elif re.search("\[[A-Z]\]",str):
                if len(stacks) <= index:
                    stacks.append([])
                stacks[index].append(re.search("\[([A-Z])\]",str).group(1))
                index += 1

def get_moves(file):
    moves = []
    for line in file:
        reg = re.search("move (\d+) from (\d+) to (\d+)",line)
        if reg:
            moves.append((int(reg.group(1)),int(reg.group(2)),int(reg.group(3))))
    return moves

f = open("05-22-input.txt","r")
stacks = get_stacks(f)
moves = get_moves(f)

def do_move(stacks,move):
    temp = stacks[move[1]-1][:move[0]]
    # Comment out for part 2
    #temp.reverse()
    stacks[move[1]-1] = stacks[move[1]-1][move[0]:]
    stacks[move[2]-1] = temp + stacks[move[2]-1]

def do_moves(stack,moves):
    for m in moves:
        do_move(stack,m)

def get_top(stacks):
    return list(map(lambda x : x[0],stacks))

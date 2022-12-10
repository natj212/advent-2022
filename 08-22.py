f = open("08-22-input.txt","r")

grid = []

for line in f:
    grid.append(list(map(lambda x : int(x),filter(lambda x : x != '\n',line))))

def check_visible(grid,y,x):
    tree = grid[y][x]
    if len(list(filter(lambda el : el >= tree,grid[y][:x]))) == 0:
        return True
    if len(list(filter(lambda el : el >= tree,grid[y][x+1:]))) == 0:
        return True

    vert = list(map(lambda el : el[x],grid))
    if len(list(filter(lambda el : el >= tree,vert[:y]))) == 0:
        return True
    if len(list(filter(lambda el : el >= tree,vert[y+1:]))) == 0:
        return True

def get_num(grid,y,x):
    tempa = 0
    tempb = 0
    tempc = 0
    tempd = 0
    tree = grid[y][x]
    for i in range(x-1,-1,-1):
        tempa += 1
        if grid[y][i] >= tree:
            break
    for i in range(x+1,len(grid[y])):
        tempb += 1
        if grid[y][i] >= tree:
            break
    vert = list(map(lambda el : el[x],grid))

    for i in range(y-1,-1,-1):
        tempc += 1
        if vert[i] >= tree:
            break
    for i in range(y+1,len(vert)):
        tempd += 1
        if vert[i] >= tree:
            break
    return (tempa * tempb * tempc * tempd)
    
            
highest = 0
for y in range(len(grid)):
    for x in range(len(grid)):
        highest = max(highest,get_num(grid,y,x))

print(highest)
    


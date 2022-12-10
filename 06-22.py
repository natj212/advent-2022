import sys
sys.setrecursionlimit(4100)

def get_marker(str,count):
    if len(str) < 14:
        return None
    elif check_unique(str[0:14]):
        return count
    else:
        return get_marker(str[1:],count + 1)
    
def check_unique(str):
    for c in str:
        if str.count(c) > 1:
            return False
    return True

f = open("06-22-input.txt","r")

data = f.read()

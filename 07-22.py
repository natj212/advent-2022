import re

class Dir:
    upper_dir = None
    size = 0
    
    
    def __init__(self,name):
        self.name = name
        self.files = {}
        self.folders = {}
        
    def create_sub(self, name):
        s = Dir(name)
        self.folders[name] = s
        s.upper_dir = self

    def add_file(self, name, size):
        self.files[name] = size
        current_dir = self
        while current_dir:
            current_dir.size += int(size)
            current_dir = current_dir.upper_dir
    def get_dir(self,name):
        return self.folders[name]
    def get_upper(self):
        return self.upper_dir

def create_dir(file):
    f = open(file,'r')
    f.readline()
    root = Dir("/")
    cur_dir = root
    for line in f:
        if re.search("\$ cd [A-Za-z]",line):
            d = re.search("\$ cd (.+)",line).group(1)
            cur_dir = cur_dir.get_dir(d)
        elif re.search("^dir",line):
            d = re.search("^dir (.+)",line).group(1)
            cur_dir.create_sub(d)
        elif re.search("^\d",line):
            r = re.search("^(\d+) (.+)",line)
            cur_dir.add_file(r.group(2),r.group(1))
        elif re.search("^\$ cd ..",line):
            cur_dir = cur_dir.get_upper()
    return root
            
def calc(d):
    size = 0
    if int(d.size) <= 100000:
        size = int(d.size)
    for item in d.folders.values():
        size += calc(item)
    return size

def calc2(d,mini):
    #print(d.size)
    if int(d.size) >= 268565:
        mini = min(mini, int(d.size))

    for item in d.folders.values():
        mini = calc2(item,mini)
    return mini
    

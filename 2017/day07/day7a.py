import sys

class Program:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        self.parent = None
        self.children = []

    def __str__(self):
        s = self.name + " " + "(" + str(self.weight) + ")"
        if len(self.children) > 0:
            s += " -> "
            for name in self.children:
                s += " " + name
        return s

def process_line(line):
    w = line.split()
    if len(w) == 2:   # pbga (66)
        name = w[0]
        weight = int(w[1].replace("(","").replace(")",""))
        p = Program(name,weight)
    else:             # fwft (72) -> ktlj, cntj, xhth
        name = w[0]
        weight = int(w[1].replace("(","").replace(")",""))
        p = Program(name,weight)
        for i in range(len(w) - 3):
            name = w[i+3].replace(",","")
            p.children.append(name)
    return p

def read_data(fname):
    data = {}
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        p = process_line(line)
        name = p.name
        data[name] = p
    f.close()
    return data
    
def add_parents(data):
    for name in data:
        p = data[name]
        for ch_name in p.children:
            c = data[ch_name]
            c.parent = name

def process(data):
    #for name in data:
    #    print(name + " " + str(data[name]))
    add_parents(data)
    for name in data:
        p = data[name]
        if p.parent == None:
            print("No parent: " + name)

def day7(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day7 input.txt") 
    else:
    	day7(sys.argv[1])


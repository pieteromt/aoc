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

def check_sums(sums):
    sum0 = sums[0]
    for sum in sums:
        if sum != sum0:
            return False
    return True

def check_balance(data, root, level):
    p = data[root]
    print(" " * (4*level), end='')
    print(root + " weight: " + str(p.weight))
    sum = p.weight
    sums = []
    if len(p.children) > 0:
        for name in p.children:
            c = data[name]
            si = check_balance(data, name, level+1)
            sums.append(si)
            sum += si
        if check_sums(sums):
            status = "OK"
        else:
            status = "NOK"
        print(" " * (4*level), end='')
        print(root + " sum: " + str(sum) + " = " + str(p.weight) + " + " + str(sums) + " " + status)
    return sum

# % python3 day7b.py input.txt  | grep 1784
#             eionkb sum: 1784 = 1079 + [235, 235, 235] OK
#         ycpcv sum: 8964 = 72 + [1777, 1777, 1784, 1777, 1777] NOK
# 1784 should be 1777, 7 too high, so 1079 should be 1072

def process(data):
    add_parents(data)
    for name in data:
        p = data[name]
        if p.parent == None:
            break
    check_balance(data, name, 0)

def day7(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day7 input.txt") 
    else:
    	day7(sys.argv[1])


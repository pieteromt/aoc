import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data = list(map(int,w))
    f.close()
    return data
    
class Node:
    def __init__(self):
        self.children = []
        self.meta = []

def parse_node(data, idx):
    nr_children = data[idx]
    idx += 1
    nr_meta = data[idx]
    idx += 1
    node = Node()
    for i in range(nr_children):
        idx, child = parse_node(data, idx)
        node.children.append(child)
    for i in range(nr_meta):
        node.meta.append(data[idx])
        idx += 1
    return idx, node

def calc_sum(node):
    sum = 0
    for n in node.meta:
        sum += n
    for child in node.children:
        sum += calc_sum(child)
    return sum

def process(data):
    idx, root = parse_node(data,0)
    sum = calc_sum(root)
    print("Sum = " + str(sum))

def day8(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day8 input.txt") 
    else:
    	day8(sys.argv[1])

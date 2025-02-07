import sys

class Node:
    def __init__(self,name):
        self.name = name
        self.deps = []

    def __str__(self):
        return self.name + " " + str(self.deps)

def read_data(fname):
    nodes = {}
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        s0 = w[1]
        s1 = w[7]
        if not s0 in nodes:
            nodes[s0] = Node(s0)
        if not s1 in nodes:
            nodes[s1] = Node(s1)
        nodes[s1].deps.append(s0)
    f.close()
    return nodes
    
# to create a picture, use:
# dot -Tpng -o day7.png day7.dot
def save_dot(fname, nodes):
    f = open(fname,"w")
    f.write("digraph {\n")
    for node in nodes:
        n = nodes[node]
        for d in n.deps:
            f.write('"'+ d +'" -> "'+ n.name +'"' + '\n')
    f.write("}\n")
    f.close()

def remove_node(nodes,name):
    nodes.pop(name)
    for node in nodes:
        n = nodes[node]
        if name in n.deps:
            n.deps.remove(name)

def calc_order(nodes):
    nodeps = []
    for node in nodes:
        n = nodes[node]
        if len(n.deps) == 0:
            nodeps.append(n.name)
    nodeps.sort()
    name = nodeps[0]
    print(name,end='')
    remove_node(nodes,name)
    if len(nodes)>0:
        calc_order(nodes)
    else:
        print("")

def process(nodes):
    #for node in nodes:
    #    print(nodes[node])
    #save_dot("day7.dot", nodes)
    calc_order(nodes)

def day7(fname):
    nodes = read_data(fname)
    process(nodes)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day7 input.txt") 
    else:
    	day7(sys.argv[1])

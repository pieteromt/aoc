import sys

class Node:
    def __init__(self,name):
        self.name = name
        self.deps = []

    def __str__(self):
        return self.name + " " + str(self.deps)

class Worker:
    def __init__(self,nr):
        self.nr = nr
        self.busy = False
        self.step = None
        self.time = 0

    def start(self,step):
        if self.busy:
            print("error: worker " + str(self.nr) + " is busy!")
            exit()
        self.busy = True
        self.step = step
        self.time = 60 + (ord(step) - ord('A')) + 1   # real
        #self.time = (ord(step) - ord('A')) + 1         # test

    def tick(self):
        done = None
        if self.busy:
            #print("worker " + str(self.nr) + " working on step " + self.step)
            self.time -= 1
            if self.time == 0:
                #print("worker " + str(self.nr) + " finished working on step " + self.step)
                done = self.step
                self.busy = False
                self.step = None
        return done

    def __str__(self):
        s = "worker " + str(self.nr)
        if self.busy:
            s += " is working on step " + self.step + ", remaining time is " + str(self.time)
        else:
            s += " is idle"


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

def init_workers(cnt):
    workers = []
    for nr in range(cnt):
        workers.append(Worker(nr+1))
    return workers

def nr_of_free_workers(workers):
    cnt = 0
    for w in workers:
        if not w.busy:
            cnt += 1
    return cnt

def all_free(workers):
    return nr_of_free_workers(workers) == len(workers)

def get_free_worker(workers):
    for w in workers:
        if not w.busy:
            return w
    return None

def step_busy(workers, step):
    for w in workers:
        if w.busy and w.step == step:
            return True
    return False

def get_candidates(nodes):
    nodeps = []
    for node in nodes:
        n = nodes[node]
        if len(n.deps) == 0:
            nodeps.append(n.name)
    nodeps.sort()
    return nodeps

# returns False if no more work
def do_tick(t, nodes, workers):
    for w in workers:
        step = w.tick()   # returns name of step if finished
        if step != None:
            remove_node(nodes,step)
    if len(nodes) == 0:  # we're done
        return False
    nodeps = get_candidates(nodes)
    while (len(nodeps) > 0) and (nr_of_free_workers(workers) > 0):
        name = nodeps.pop(0)
        if not step_busy(workers,name):
            worker = get_free_worker(workers)
            worker.start(name)
    print("{:3d}".format(t) + "   ", end='')
    for w in workers:
        if w.busy:
            print("{:3s}".format(w.step), end='')
        else:
            print("{:3s}".format("."), end='')
    print("")
    return True

def process(nodes):
    #workers = init_workers(2)    # test
    workers = init_workers(5)   # real
    t = 0
    while do_tick(t, nodes, workers):
        t += 1
    print("time: " + str(t))

def day7(fname):
    nodes = read_data(fname)
    process(nodes)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day7 input.txt") 
    else:
    	day7(sys.argv[1])

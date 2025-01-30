import sys
import math

class Particle:
    def __init__(self,p,v,a):
        self.x = p[0]
        self.y = p[1]
        self.z = p[2]
        self.vx = v[0]
        self.vy = v[1]
        self.vz = v[2]
        self.ax = a[0]
        self.ay = a[1]
        self.az = a[2]

    def __str__(self):
        s = "p=<"+str(self.x)+","+str(self.y)+","+str(self.z)+">, "
        s += "v=<"+str(self.vx)+","+str(self.vy)+","+str(self.vz)+">, "
        s += "a=<"+str(self.ax)+","+str(self.ay)+","+str(self.az)+">"
        return s

# p=<1500,413,-535>,
def get_tuple(line):
    line = line.replace('<',' ').replace('>',' ')
    line = line.split()
    vals = line[1].split(',')
    return tuple(map(int,vals))

# p=<1500,413,-535>, v=<-119,22,36>, a=<-5,-12,3>
def add_particle(line):
    w = line.split()
    p = get_tuple(w[0])
    v = get_tuple(w[1])
    a = get_tuple(w[2])
    return Particle(p,v,a)

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        part = add_particle(line)
        data.append(part)
    f.close()
    return data
    
def do_tick(data, coll):
    coor = {}
    rm = set()
    for i in range(len(data)):
        p = data[i]
        p.vx += p.ax
        p.vy += p.ay
        p.vz += p.az
        p.x += p.vx
        p.y += p.vy
        p.z += p.vz
        t = (p.x,p.y,p.z)
        if t in coor:
            rm.add(coor[t])
            rm.add(i)
        else:
            coor[t] = i
    return coll.union(rm)

def process(data):
    coll = set()
    for t in range(100):
        coll = do_tick(data, coll)
    nr = len(coll)
    #print("collisions: " + str(nr))
    print("remaining:  " + str(len(data) - nr))

def day20(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day20 input.txt") 
    else:
    	day20(sys.argv[1])


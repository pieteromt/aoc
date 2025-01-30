import sys

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

# there are multiple particles with the same minimum acceleration
# so we need to look at their velocities too
def closest(data):
    min_a = 99999
    for i in range(len(data)):
        part = data[i]
        a = abs(part.ax) + abs(part.ay) + abs(part.az)
        if a < min_a:
            min_a = a
    min_v = 99999
    min_i = 0
    for i in range(len(data)):
        part = data[i]
        a = abs(part.ax) + abs(part.ay) + abs(part.az)
        if a == min_a:
            #print("min_a: " + str(min_a) + " for particle " + str(i) + " --> " + str(data[i]))
            v = abs(part.vx) + abs(part.vy) + abs(part.vz)
            if v < min_v:
                min_v = v
                min_i = i
    #print("min_v: " + str(min_v) + " for particle " + str(min_i) + " --> " + str(data[min_i]))
    print("particle " + str(min_i))

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        part = add_particle(line)
        data.append(part)
    f.close()
    return data
    
def process(data):
    #for d in data:
    #    print(d)
    closest(data)

def day20(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day20 input.txt") 
    else:
    	day20(sys.argv[1])


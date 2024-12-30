import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 15:
            name = w[0]
            speed = int(w[3])
            duration = int(w[6])
            rest = int(w[13])
            data.append((name,speed,duration,rest))
        else:
            print("error: " + str(len(w)))
            exit()
    f.close()
    return data

def calc_dist(d, sec):
    name,speed,duration,rest = d
    period = duration + rest
    nr_per = sec//period
    remain = sec%period
    dist = nr_per * speed * duration
    if remain >= duration:
        dist += speed * duration
    else:
        dist += speed * remain
    return dist

def process(data,sec):
    d_max = -1
    n_max = None
    for d in data:
        name = d[0]
        dist = calc_dist(d,sec)
        print(name + " " + str(dist))
        if dist > d_max:
            d_max = dist
            n_max = name
    print("Maximum: " + n_max + " " + str(d_max))

def day14(fname):
    data = read_data(fname)
    process(data,2503)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day14 input.txt") 
    else:
    	day14(sys.argv[1])


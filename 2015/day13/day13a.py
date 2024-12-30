import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 11:
            p1 = w[0]
            p2 = w[10][:-1] # strip dot
            val = int(w[3])
            if w[2] == "lose":
                val = -val
            data.append((p1,p2,val))
        else:
            print("error: len = " + str(len(w)))
            exit()
    f.close()
    return data

def get_guests(data):
    guests = set()
    for d in data:
        guests.add(d[0])
        guests.add(d[1])
    return guests

# tuple generator
def all_tuples(locs):
    if len(locs) == 1:
        yield (locs.pop(),)
    else:
        for loc in locs:              # loc is the startlocation
            lc = locs.copy()
            lc.remove(loc)
            for t in all_tuples(lc):  # lc is the rest of the locations
                yield (loc,) + t

# p1 would gain/lose happiness units by sitting next to p2
def get_happ(data,p1,p2):
    for d in data:
        if (d[0] == p1) and (d[1] == p2):
            return d[2]
    print("error: " + p1 + " " + p2)
    exit()

# calc happiness for all guests in tuple
def calc_happiness(data,t):
    happ = 0
    nr = len(t)
    for i in range(nr):
        i_prev = (i + nr - 1)%nr
        i_next = (i + 1)%nr
        h_prev = get_happ(data, t[i], t[i_prev])
        h_next = get_happ(data, t[i], t[i_next])
        happ += h_prev + h_next
    return happ

def process(data):
    guests = get_guests(data)
    h_max = -1
    t_max = None
    for t in all_tuples(guests):
        happ = calc_happiness(data,t)
        if happ > h_max:
            h_max = happ
            t_max = t
    print("Maximum: " + str(h_max) + " " + str(t_max))

def day13(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day13 input.txt") 
    else:
    	day13(sys.argv[1])


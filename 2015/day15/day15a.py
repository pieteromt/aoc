import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 11:
            name = w[0][:-1]
            capacity = int(w[2][:-1])
            durability = int(w[4][:-1])
            flavor = int(w[6][:-1])
            texture = int(w[8][:-1])
            calories = int(w[10])
            spoons = 0
            data.append([name,spoons,capacity,durability,flavor,texture,calories])
        else:
            print("error: " + str(len(w)))
            exit()
    f.close()
    return data

def calc_score(data):
    capacity,durability,flavor,texture,calories = 0,0,0,0,0
    for d in data:
        name,spoons,cap,dur,fla,tex,cal = d
        capacity   += spoons*cap
        durability += spoons*dur
        flavor     += spoons*fla
        texture    += spoons*tex
        calories   += spoons*cal
    if capacity<0:
        capacity=0
    if durability<0:
        durability=0
    if flavor<0:
        flavor=0
    if texture<0:
        texture=0
    if calories<0:
        calories=0
    return capacity*durability*flavor*texture

def all_tuples(nr,sp):
    if nr == 1:
        yield (sp,)
    else: 
        for sp0 in range(0,sp+1):
            for t in all_tuples(nr-1,sp-sp0):
                yield (sp0,) + t
    
def process(data):
    nr = len(data)
    s_max = -1
    t_max = None
    for t in all_tuples(nr,100):
        for i in range(0,nr):
            data[i][1] = t[i]  # spoons
        score = calc_score(data)
        #print(str(t) + " " + str(score))
        if score > s_max:
            s_max = score
            t_max = t
    print("Maximum: " + str(s_max) + " for " + str(t_max))

def day15(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day15 input.txt") 
    else:
    	day15(sys.argv[1])


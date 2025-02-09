import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    state = 0
    rules = {}
    for line in f:
        line = line.strip()
        if len(line) > 0:
            w = line.split()
            if state == 0:
                initial = w[2]
                state = 1
            else:
                rules[w[0]] = w[2]
    f.close()
    return initial, rules
    
def next_gen(plants, rules):
    ng = ".." 
    for i in range(len(plants)-4):
        r = plants[i:i+5]
        if r in rules:
            ch = rules[r]
        else:
            ch = "."
        ng += ch
    ng += ".."
    return ng
        
def calc_sum(plants, left_pad):
    sum = 0
    for i in range(len(plants)):
        if plants[i] == "#":
            sum += (i - left_pad)
    print("sum: " + str(sum))

def process(initial, rules):
    #print("initial state: " + initial)
    #for rule in rules:
    #    print(rule + " => " + rules[rule])
    left_pad = 10
    right_pad = 20
    plants = "."*left_pad + initial + "."*right_pad
    print(str(0) + ": " + plants)
    for i in range(20):
        plants = next_gen(plants, rules)
        print(str(i+1) + ": " + plants)
    calc_sum(plants, left_pad)

def day12(fname):
    initial, rules = read_data(fname)
    process(initial, rules)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day12 input.txt") 
    else:
    	day12(sys.argv[1])

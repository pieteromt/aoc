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
    return sum

# after 95 generations, the process converges to multiple sets of 2 plants
def calc_est_sum(i):
    return 13 + (i+21)*22    # for the real input
    #return 14 + (i-32)*20    # for the test input
    
def process(initial, rules):
    #print("initial state: " + initial)
    #for rule in rules:
    #    print(rule + " => " + rules[rule])
    nr_iter = 110
    left_pad = 10
    right_pad = nr_iter
    plants = "."*left_pad + initial + "."*right_pad
    #print(str(0) + ": " + plants)
    prev = 0
    for i in range(1,nr_iter+1):
        plants = next_gen(plants, rules)
        #print(str(i) + ": " + plants)
        sum = calc_sum(plants, left_pad)
        est_sum = calc_est_sum(i)
        delta = sum - prev
        prev = sum
        print(str(i) + ", est_sum: " + str(est_sum) + ", sum: " + str(sum) + ", delta: " + str(delta))
    i = 50000000000
    est_sum = calc_est_sum(i)
    print("After " + str(i) + " generations, the sum is " + str(est_sum))

def day12(fname):
    initial, rules = read_data(fname)
    process(initial, rules)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day12 input.txt") 
    else:
    	day12(sys.argv[1])

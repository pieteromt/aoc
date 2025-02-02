import sys

def read_data(fname):
    data = {}
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split('/')
        data[(int(w[0]),int(w[1]))] = 0  # unused
    f.close()
    return data
    
# find all unuseds tuple in data with value 'val' 
def find(data, val):
    tups = []
    for t in data:
        if data[t] == 0: # unused
            if (t[0] == val) or (t[1] == val):
                tups.append(t)
    return tups

def calc_strength(bridge):
    s = 0
    for t in bridge:
        s += (t[0] + t[1])
    return s

def other(t, val):
    if val == t[0]:
        return t[1]
    else:
        return t[0]

def max_strength(data, val, bridge, max_len):
    tups = find(data, val)
    if len(tups) == 0:
        if len(bridge) == max_len:
            return calc_strength(bridge)
        else:
            return 0   # only interested in longest bridges
    max_str = 0
    for t in tups:
        data[t] = 1  # in use
        bridge.append(t)
        strength = max_strength(data, other(t,val), bridge, max_len)
        if strength > max_str:
            max_str = strength
        data[t] = 0
        bridge.pop()
    return max_str

def max_length(data, val, bridge):
    tups = find(data, val)
    if len(tups) == 0:
        return len(bridge)
    max_len = 0
    for t in tups:
        data[t] = 1  # in use
        bridge.append(t)
        ln = max_length(data, other(t,val), bridge)
        if ln > max_len:
            max_len = ln
        data[t] = 0
        bridge.pop()
    return max_len

def process(data):
    #for d in data:
    #    print(str(d) + " " + str(data[d]))
    max_len = max_length(data, 0, [])
    print("max length = " + str(max_len))
    strength = max_strength(data, 0, [], max_len)
    print("strength = " + str(strength))

def day24(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day24 input.txt") 
    else:
    	day24(sys.argv[1])


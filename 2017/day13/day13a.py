import sys

def read_data(fname):
    data = {}
    mx = 0
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        layer = int(w[0].replace(':',''))
        data[layer] = [int(w[1]), 0, 1]
        if layer > mx:
            mx = layer
    f.close()
    return data, mx
    
def update_pos(data):
    for layer in data:
        rang  = data[layer][0]
        pos   = data[layer][1]  # 0 <= pos < rang
        dir   = data[layer][2]  # 1 or -1
        pos += dir
        data[layer][1] = pos
        if (pos == 0) or (pos == rang-1):
            dir = -dir
            data[layer][2] = dir

# packet starts moving (into the layers) at picosecond 'start'
def simulate(data, mx, start):
    packet_pos = -start
    severity = 0
    for t in range(start+mx+1):
        #print("picosecond " + str(t))
        #for layer in data:
        #    print(str(layer) + " ", end='')
        #    print(data[layer])
        #print("")
        if packet_pos in data:
            if data[packet_pos][1] == 0:
                #print("caught in layer " + str(packet_pos))
                severity += packet_pos * data[packet_pos][0]
        update_pos(data)
        packet_pos += 1
    return severity

def process(data, mx):
    severity = simulate(data, mx, 0)
    print("severity = " + str(severity))

def day13(fname):
    data, mx = read_data(fname)
    process(data, mx)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day13 input.txt") 
    else:
    	day13(sys.argv[1])


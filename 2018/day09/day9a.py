import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data.append((int(w[0]),int(w[6])))
    f.close()
    return data

def show_ring(player, ring, cur):
    print("[" + str(player+1) + "]  ",end='')
    for i in range(len(ring)):
        val = ring[i]
        if i == cur:
            print("(" + str(val) + ")  ",end='')
        else:
            print(" " + str(val) + "   ",end='')
    print("")   

def insert(scores, player, ring, cur, val):
    if val%23 == 0:
        idx = (cur+len(ring)-7)%len(ring)  # 7 counter-clockwise
        val7 = ring.pop(idx)
        score = val + val7
        cur = idx%len(ring)
        scores[player] += score
    else:
        idx = (cur+2)%len(ring)
        if idx == 0:
            ring.append(val)
            cur = len(ring)-1
        else:
            ring.insert(idx,val)
            cur = idx
    return cur

def process(t):
    nr_players, max_marble = t
    scores = [0] * nr_players
    ring = [0]
    cur = 0
    player = 0
    for val in range(1,max_marble+1):
        cur = insert(scores, player, ring, cur, val)
        #show_ring(player, ring, cur)
        player = (player+1)%nr_players
    high_score = 0
    for score in scores:
        if score > high_score:
            high_score = score
    print("High score = " + str(high_score))

def day9(fname):
    data = read_data(fname)
    for t in data:
        process(t)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day9 input.txt") 
    else:
    	day9(sys.argv[1])

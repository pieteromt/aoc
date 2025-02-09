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

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self
        self.next = self

def insert_before(lst, node):
    node.next = lst
    node.prev = lst.prev
    lst.prev = node
    node.prev.next = node
    return node

def remove_node(node):
    nxt = node.next
    prv = node.prev
    prv.next = nxt
    nxt.prev = prv

def show_ring(player, lst, cur):
    print("[" + str(player+1) + "]  ",end='')
    start = lst
    while True:
        val = lst.val
        if lst == cur:
            print("(" + str(val) + ")  ",end='')
        else:
            print(" " + str(val) + "   ",end='')
        lst = lst.next
        if lst == start:
            break
    print("")   

def insert(scores, player, cur, val):
    if val%23 == 0:
        cur = cur.prev.prev.prev.prev.prev.prev.prev
        val7 = cur.val
        nxt = cur.next
        remove_node(cur)
        scores[player] += val + val7
        cur = nxt
    else:
        cur = cur.next.next
        cur = insert_before(cur, Node(val))
    return cur

def process(t):
    nr_players, max_marble = t
    scores = [0] * nr_players
    lst = Node(0)
    cur = lst
    player = 0
    for val in range(1,max_marble+1):
        cur = insert(scores, player, cur, val)
        #show_ring(player, lst, cur)
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

import sys

#sys.setrecursionlimit(15000)

conn = []
comp = {}
triples = []
triples_t = []

def read_data(fname):
    global conn
    conn = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if line:
            words = line.split('-')
            conn.append((words[0],words[1]))
    f.close()

def make_comp():
    global comp
    for c in conn:
        c1, c2 = c
        if not c1 in comp:
            comp[c1] = [c2]
        else:
            comp[c1].append(c2)
        if not c2 in comp:
            comp[c2] = [c1]
        else:
            comp[c2].append(c1)

def sort_triple(c1,c2,c3):
    if c3 < c2:
        tmp = c2
        c2 = c3
        c3 = tmp
    if c2 < c1:
        tmp = c1
        c1 = c2
        c2 = tmp
    if c3 < c2:
        tmp = c2
        c2 = c3
        c3 = tmp
    return c1, c2 ,c3

def has_t(c1,c2,c3):
    return (c1[0] == 't') or (c2[0] == 't') or (c3[0] == 't')

def add_triple(c1,c2,c3):
    global triples, triples_t
    c1,c2,c3 = sort_triple(c1,c2,c3)
    tp = (c1,c2,c3)
    if not tp in triples:
        triples.append(tp)
        if has_t(c1,c2,c3):
            triples_t.append(tp)

def find_triple():
    for c1 in comp:
        ln = len(comp[c1])
        for i in range(0,ln):
            for j in range(i+1,ln):
                c2 = comp[c1][i]
                c3 = comp[c1][j]
                if c3 in comp[c2]:
                    add_triple(c1,c2,c3)

def day23(fname):
    read_data(fname)
    make_comp()
    find_triple()
    #for t in triples_t:
    #    print(str(t))
    print(len(triples_t))

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if (len(sys.argv)) > 1:
        fname = sys.argv[1]
        day23(fname)
    else:
        print("Usage: python day23 input.txt")

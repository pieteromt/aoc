import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        if len(w) == 7:
            stmt = (w[0], w[1], int(w[2]))
            cond = (w[4], w[5], int(w[6]))
            data.append((stmt, cond))
        else:
            print("error: " + line)
            exit()
    f.close()
    return data
    
# !=
# <
# <=
# ==
# >
# >=
def eval_cond(cache, cond):
    reg, cmp, val = cond
    if reg in cache:
        cur = cache[reg]
    else:
        cur = 0
        cache[reg] = cur
    if cmp == "!=":
        return cur != val
    elif cmp == "<":
        return cur < val
    elif cmp == "<=":
        return cur <= val
    elif cmp == "==":
        return cur == val
    elif cmp == ">":
        return cur > val
    elif cmp == ">=":
        return cur >= val
    else:
        print("error: " + cmp)
        exit()

max = -99999

def eval_stmt(cache, stmt):
    global max
    reg, op, val = stmt
    if reg in cache:
        cur = cache[reg]
    else:
        cur = 0
        cache[reg] = cur
    if op == "dec":
        cur -= val
    elif op == "inc":
        cur += val
    else:
        print("error: " + op)
        exit()
    cache[reg] = cur
    if cur > max:
        max = cur

def execute(cache, d):
    stmt, cond = d
    if eval_cond(cache, cond):
        eval_stmt(cache, stmt)

def process(data):
    cache = {}
    for d in data:
        execute(cache, d)
    for reg in sorted(cache.keys()):
        val = cache[reg]
        print(reg + " : " + str(val))
    print("Largest: " + str(max))

def day8(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day8 input.txt") 
    else:
    	day8(sys.argv[1])


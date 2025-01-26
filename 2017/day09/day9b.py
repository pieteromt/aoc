import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split()
        data.append(line)
    f.close()
    return data
    
garbage = 0

# d starts with '<'
def open_bracket(d):
    global garbage
    bracket = d[:1]
    rest = d[1:]
    while True:
        if rest.startswith('>'):
            # end of garbage found
            #print("end of garbage")
            rest = rest[1:]
            break
        elif rest.startswith('!'):
            exclam = rest[:1]
            ignore = rest[1:2]
            rest = rest[2:]
        else:
            rest = rest[1:] # skip garbage
            garbage += 1
    return rest

# d starts with '{'
def open_brace(d, level,score):
    brace = d[:1]
    rest  = d[1:]
    while True:
        if rest.startswith('}'):
            # end of group found
            #print("group found at level " + str(level))
            score += level
            rest = rest[1:]
            break
        elif rest.startswith('{'):
            rest, score = open_brace(rest, level+1, score)
        elif rest.startswith('<'):
            rest = open_bracket(rest)
        elif rest.startswith(','):
            rest = rest[1:]
        else:
            print("error: " + rest)
            exit()
    return rest, score

def process(data):
    global garbage
    for d in data:
        #print(d)
        garbage = 0
        rest, score = open_brace(d,1,0)
        print("garbage = " + str(garbage))

def day9(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day9 input.txt") 
    else:
    	day9(sys.argv[1])


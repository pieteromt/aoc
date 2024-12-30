import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data

def encode(s):
    result = '"'
    i = 0
    while i < len(s):
        c = s[i]
        if c == '"':
            result += '\\"'
        elif c == '\\':
            result += '\\\\'
        else:
            result += c
        i += 1
    result += '"'
    return result

def get_delta(s):
    result = encode(s)
    #print(s + " " + result)
    return len(result) - len(s)

def process(data):
    sum = 0
    for s in data:
        sum += get_delta(s)
    print("sum = " + str(sum))

def day8(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day8 input.txt") 
    else:
    	day8(sys.argv[1])


import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data

def decode(s):
    in_str = False
    result = ""
    i = 0
    while i < len(s):
        c = s[i]
        if c == '"':
            in_str = not in_str
        elif c == '\\':
            i += 1
            c = s[i]  # next char
            if c == '"' or c == '\\':
                result += c
            elif c == 'x':
                i += 1
                result += chr(int(s[i:i+2],16))  # read hex
                i += 1
            else:
                print("error: " + c)
                exit()
        else:
            result += c
        i += 1
    return result

def get_delta(s):
    result = decode(s)
    #print(s + " " + result)
    return len(s)-len(result)

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


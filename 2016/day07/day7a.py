import sys

def process_line(line):
    out = []
    ins = []
    while len(line) > 0:
        br = line.find("[")
        if br != -1:
            end = line.find("]")
            out.append(line[:br])
            ins.append(line[br+1:end])
            line = line[end+1:]
        else: # no bracket found anymore
            out.append(line)
            line = ""
    return (out,ins)  # outside, inside brackets

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(process_line(line))
    f.close()
    return data
    
def has_abba(s):
    for i in range(len(s)-3):
        if (s[i] == s[i+3]) and (s[i+1] == s[i+2]) and (s[i] != s[i+1]):
            return True
    return False

def has_abba_arr(arr):
    for s in arr:
        if has_abba(s):
            return True
    return False

def supports_tls(d):
    out,ins = d
    return has_abba_arr(out) and not has_abba_arr(ins)

def process(data):
    cnt = 0
    for d in data:
        if supports_tls(d):
            cnt += 1
    print("Supports TLS = " + str(cnt))

def day7(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day7 input.txt") 
    else:
    	day7(sys.argv[1])


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
    
def find_aba(s):
    aba = set()
    bab = set()
    for i in range(len(s)-2):
        if (s[i] == s[i+2]) and (s[i] != s[i+1]):
            aba.add(s[i:i+3])
            bab.add(s[i+1]+s[i]+s[i+1])
    return aba,bab

def find_all_bab(arr):
    all_aba = set()
    all_bab = set()
    for s in arr:
        aba,bab = find_aba(s)
        all_aba.update(aba)
        all_bab.update(bab)
    return all_bab

def supports_ssl(d):
    out,ins = d
    all_bab = find_all_bab(out)
    for bab in all_bab:
        for s in ins:
            if bab in s:
                return True
    return False

def process(data):
    cnt = 0
    for d in data:
        if supports_ssl(d):
            cnt += 1
    print("Supports SSL = " + str(cnt))

def day7(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day7 input.txt") 
    else:
    	day7(sys.argv[1])


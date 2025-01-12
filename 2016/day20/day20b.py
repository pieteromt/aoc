import sys

def read_data(fname):
    data = {}
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.split('-')
        start = int(w[0])
        end = int(w[1])
        size = end - start + 1
        data[start] = (start,size,end)
    f.close()
    return data
    
def process(data, max_ip):
    blocked = -1
    sum = 0
    for d in sorted(data.keys()):
        start, size, end = data[d]
        if start <= blocked+1:          # blocked+1 is the first unblocked IP
            if end > blocked:
                blocked = end
        else: # not blocked
            sum += start - (blocked+1)  # add free IPs
            blocked = end
    sum += max_ip - (blocked+1) + 1     # add free IPs at the end of the range 
    print("Non-blocked: " + str(sum))

def show_data(data):
    for d in sorted(data.keys()):
        print(str(d) + "  " + str(data[d]))

def day20(fname):
    data = read_data(fname)
    max_ip = 2**32 - 1
    process(data, max_ip)
    #show_data(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day20 input.txt") 
    else:
    	day20(sys.argv[1])


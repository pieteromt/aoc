import sys

data = []
cnt = 0
disk = []
count = 0
flen = []   # file lengths (idx,len)
xlen = []   # free lengths (idx, len)

idx_free = -1
idx_last = -1

def set_ch(r,c,val):
    global data
    row = data[r]
    new_row = row[:c] + val + row[c+1:]
    data[r] = new_row

def ch(row,col):
    if (row >= 0) and (row < rows) and (col >= 0) and (col < cols):
        return data[row][col]
    else:
        return "_"  # outside

def read_data(fname):
    global cnt, data, disk, count, idx_free, idx_last
    f = open(fname,"r")
    count = 0
    idx = 0
    fl = True
    while True:
        line = f.readline().strip()
        if line:
            if cnt == 0:
                cnt = len(line)
            for i in range(0,cnt):
                n = int(line[i])
                data.append(n)
                if fl:
                    idx_file = len(disk)
                    len_file = n
                    #print("file: idx = " + str(idx_file) + ", len = " + str(len_file))
                    flen.append((idx_file, len_file))
                    for j in range(0,n):
                        disk.append(idx)
                    idx_last = len(disk)-1
                    idx = idx + 1
                else:
                    if idx_free == -1:
                        idx_free = len(disk)
                    idx_x = len(disk)
                    len_x = n
                    #print("free: idx = " + str(idx_x) + ", len = " + str(len_x))
                    xlen.append((idx_x, len_x))
                    for j in range(0,n):
                        disk.append(-1)  # empty
                fl = not fl
        else:
            break
    count = len(disk)
    f.close()

def checksum():
    sum = 0
    for i in range(0,count):
        n = disk[i]
        if n != -1:
            sum = sum + i*n
    print("sum = " + str(sum))

# -1 if not found
def find_slot(ln,idx_file):  # ln = length of the file to be moved, idx of the file
    slot = -1
    nr = len(xlen)
    for i in range(0,nr):
        idx, len_free = xlen[i]
        if idx > idx_file:     # DON'T LOOK AT FREE SPACE TO THE RIGHT OF THE FILE!
            break
        if len_free >= ln:
            slot = i
            break
    return slot

def compact():
    global xlen, flen, disk
    n = len(flen)
    #print(disk)
    for i in range(n-1,-1,-1):
        idx, ln = flen[i]
        slot = find_slot(ln,idx)
        #print("slot: i = " + str(i) + ", len = " + str(ln) + ", slot = " + str(slot))
        if slot != -1:  # found
            idx_free = xlen[slot][0]
            #print("move " + str(i) + " to slot " + str(slot))
            for j in range(0,ln):
                disk[idx_free + j] = i
            for j in range(0,ln):
                disk[idx + j] = -1
            new_idx = xlen[slot][0] + ln
            new_len = xlen[slot][1] - ln
            xlen[slot] = (new_idx, new_len)
            flen[i] = None
            #print(disk)


def day9(fname):
    read_data(fname)
    #print(data)
    #print("count = " + str(cnt))
    #print(disk)
    #print("count = " + str(count) + ", free = " + str(idx_free) + ", last = " + str(idx_last))
    #print(flen)
    #print(xlen)
    compact()
    checksum()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day9 input.txt") 
    else:
    	day9(sys.argv[1])


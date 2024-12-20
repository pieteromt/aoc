import sys

data = []
cnt = 0
disk = []
count = 0

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
                    for j in range(0,n):
                        disk.append(idx)
                    idx_last = len(disk)-1
                    idx = idx + 1
                else:
                    if idx_free == -1:
                        idx_free = len(disk)
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

def compact():
    global disk, idx_free, idx_last
    #print(disk)
    #print("free = " + str(idx_free) + ", last = " + str(idx_last))
    while idx_free <= idx_last:
        disk[idx_free] = disk[idx_last]
        disk[idx_last] = -1
        while idx_free < count-1:
            idx_free = idx_free + 1
            if disk[idx_free] == -1:
                break
        while idx_last > 0:
            idx_last = idx_last - 1
            if disk[idx_last] != -1:
                break
        #print(disk)
        #print("free = " + str(idx_free) + ", last = " + str(idx_last))

def day9(fname):
    read_data(fname)
    #print(data)
    #print("count = " + str(cnt))
    #print(disk)
    #print("count = " + str(count) + ", free = " + str(idx_free) + ", last = " + str(idx_last))
    compact()
    checksum()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day9 input.txt") 
    else:
    	day9(sys.argv[1])


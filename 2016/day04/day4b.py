import sys

# input looks like: aaaaa-bbb-z-y-x-123[abxyz]
def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        w = line.replace('[',' ').replace(']','').split()  # get rid of []
        ww = w[0].split('-')
        id = int(ww[-1])
        name = "-".join(ww[:-1])
        checksum = w[1]
        data.append((name,id,checksum))
    f.close()
    return data
    
def decrypt(name,id):
    d_name = ""
    for c in name:
        if c == '-':
            d_name += ' '
        else:
            i = ord(c) - ord('a')  # 0..25
            d_i = (i + id)%26      # rotate
            d_name += chr(ord('a') + d_i)
    return d_name

def process(data):
    for t in data:
        name, id, checksum = t
        d_name = decrypt(name,id)
        if d_name == "northpole object storage":
            print("Sector ID = " + str(id))

def day4(fname):
    data = read_data(fname)
    process(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day4 input.txt") 
    else:
    	day4(sys.argv[1])


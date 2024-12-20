import sys

#sys.setrecursionlimit(1500)

arr = []

def read_data(fname):
    global arr
    arr = []
    f = open(fname,"r")
    while True:
        line = f.readline().strip()
        if line:
            words = line.split()
            for word in words:
                arr.append(int(word))
        else:
            break
    f.close()

def add_dic(d, val, cnt):
    if val in d:
        d[val] = d[val] + cnt
    else:
        d[val] = cnt

def do_blink(dic):
    new_dic = {}
    for val in dic:
        cnt = dic[val]
        if val == 0:
           val = 1
           add_dic(new_dic, val, cnt)
        else:
            s = str(val)
            ln = len(s)
            if ln%2 == 0:
                div = ln//2;
                val0 = int(s[:div])
                val1 = int(s[div:])
                add_dic(new_dic, val0, cnt)
                add_dic(new_dic, val1, cnt)
            else:
                val = val*2024
                add_dic(new_dic, val, cnt)
    return new_dic

def init_dict():
    dic = {}
    for val in arr:
        add_dic(dic, val, 1)
    return dic

def calc_sum(dic):
    sum = 0
    for val in dic:
        sum = sum + dic[val]
    print("sum = " + str(sum))

count = 75

def day11(fname):
    read_data(fname)
    dic = init_dict()
    for i in range(0,count):
        dic = do_blink(dic)
    calc_sum(dic)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day11 input.txt") 
    else:
    	day11(sys.argv[1])


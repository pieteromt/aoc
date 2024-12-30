import sys

import json

def read_data(fname):
    data = []
    f = open(fname,"r")
    data = json.load(f)
    f.close()
    return data

def do_string(item):
    #print(item)
    return 0

def do_number(item):
    #print(item)
    return item

def has_red(obj):
    for item in obj:
        if obj[item] == "red":
            return True
    return False

def do_object(obj):
    sum = 0
    if not has_red(obj):
        for item in obj:
            sum += process(obj[item])
    return sum

def do_array(arr):
    sum = 0
    for item in arr:
        sum += process(item)
    return sum

def process(item):
    if type(item) == list:
        return do_array(item)
    elif type(item) == dict:
        return do_object(item)
    elif type(item) == str:
        return do_string(item)
    elif type(item) == int:
        return do_number(item)
    else:
        print("error: " + str(type(item)))
        exit()

def day12(fname):
    data = read_data(fname)
    sum = process(data)
    print("sum = " + str(sum))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day12 input.txt") 
    else:
    	day12(sys.argv[1])


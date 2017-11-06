from collections import OrderedDict
from random import randrange
from timeit import timeit



count = 0


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def hash_sack(cap, items):
    global count
    keys = hashtable.keys()
    size = len(items)
    if cap not in keys:
        hashtable[cap] = []
    wrapped = wrapper(knapsack, cap, items, size)
    t = timeit(wrapped, number=1) * 1000
    count = 1
    result = (knapsack(cap, items, size), size)
    result = (result[0],result[1],t)
    hashtable[cap].append(result)


def dyno_hash_sack(cap, items):
    global count
    keys = dynohashtable.keys()
    size = len(items)
    if cap not in keys:
        dynohashtable[cap] = []
    wrappedd = wrapper(dynoknapsack, cap, items, size)
    dt = timeit(wrappedd, number=1) * 1000
    count = 1
    result = (dynoknapsack(cap, items, size), size)
    result = (result[0], result[1], dt)
    dynohashtable[cap].append(result)



def dynoknapsack(cap, items, size):
    storage = [[0 for x in range(cap + 1)] for x in range(size + 1)]
    for i in range(size + 1):
        for j in range(cap + 1):
            if i == 0 or j == 0:
                storage[i][j] = 0
            elif items[i - 1][0] <= j:
                storage[i][j] = max(items[i - 1][1] + storage[i - 1][j - items[i - 1][0]], storage[i - 1][j])
            else:
                storage[i][j] = storage[i - 1][j]
    return storage[size][cap]




def knapsack(cap, items, size):
    global count

    if size == 0 or cap == 0:
        count+=1
        return 0
    elif(items[size-1][0] > cap):
        count += 1
        return knapsack(cap, items, size - 1)
    else:

        return max(items[size - 1][1] + knapsack(cap - items[size - 1][0], items, size - 1), knapsack(cap, items, size - 1))

def random_sack():
    cap = randrange(20, 100)
    sum = 0
    sack = []
    while sum < (cap + randrange(cap + 150)):
        weight = randrange(5,int(cap/3))
        value = randrange(weight,weight+20)
        sum = sum + weight
        sack.append((weight,value))
    return cap, sack


hashtable = {}
# (weight, value)
dynohashtable = {}


all_sacks = [(50,[(10, 60), (20, 100), (30, 120)]),(25,[(24,24),(18,10),(18,10),(10,7)])]

for x in range(20):
    all_sacks.append(random_sack())

for sack in all_sacks:

    hash_sack(*sack)
    dyno_hash_sack(*sack)



def print_hash():
    keys = hashtable
    for key in keys:
        print('Cap: %s' %key)
        for x, y, z in hashtable[key]:
           # print("%s..... %s" %(x,y))
            print("\t\t(result : %s, number of elements: %s, time: %fms), " %(x,y,z,))
        print("\n")
def printdyno_hash():
    keys = dynohashtable
    for key in keys:
        print('Cap: %s' %key)
        for x, y, z in dynohashtable[key]:
           # print("%s..... %s" %(x,y))
            print("\t\t(result : %s, number of elements: %s, time: %fms), " %(x,y,z,))
        print("\n")
print("greedy")
printdyno_hash()

print("recursive")
print_hash()


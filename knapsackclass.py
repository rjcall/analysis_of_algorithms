


def dynoknapSack(cap, items, size):
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


val = [60, 100, 120]
wt = [10, 20, 30]

items = list(zip(wt,val))
W = 50
n = len(val)
print(dynoknapSack(W, items, n))

# This code is contributed by Bhavya Jain

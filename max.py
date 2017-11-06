

s=[3,2,5,6,7,8]



def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs), wrapped.calls

    wrapped.calls = -1
    return wrapped


@counted
def findmax(low, high):
    pos = 0
    if low == high:
        return low
    else:
        pos, c = findmax(low+1, high)
        if s[low] > s[pos]:
            pos = low
        return pos


print(len(s))

a,b = findmax(0, len(s)-1)

print(s[a])
print(b)


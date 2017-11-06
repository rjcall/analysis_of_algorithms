from timeit import Timer, timeit


def addit(x,y):

    return x+y

x = 10
y=10
t = Timer()

# outside the try/except
try:
    r = t.timeit(addit(x,y))    # or t.repeat(...)
    t.

except:
    t.print_exc()

print(r)
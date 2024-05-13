import numpy as np
import itertools

d = np.array([
    [0, 5, 2, 3],
    [4, 0, 2, 3],
    [4, 2, 0, 3],
    [7, 6, 8, 0]
])

def td(t, d):
    return sum(d[t[i % len(t)], t[(i + 1) % len(t)]] for i in range(len(t)))

def ac(d, s, na=10, ni=100, er=0.5, a=1.0, b=2.0):
    nc = len(d)
    ph = np.ones((nc, nc)) / nc
    for _ in range(ni):
        at = []
        for _ in range(na):
            c = s
            v = [c]
            u = list(range(nc))
            u.remove(c)
            while u:
                p = [(ph[c, n] ** a) * ((1.0 / d[c, n]) ** b) for n in u]
                p /= np.sum(p)
                n = np.random.choice(u, p=p)
                v.append(n)
                u.remove(n)
                c = n
            at.append(v)
        ph *= (1 - er)
        for t in at:
            for i in range(nc):
                ph[t[i % nc], t[(i + 1) % nc]] += 1.0 / td(t, d)
    bt = min(at, key=lambda x: td(x, d))
    if bt[-1] != s:
        bt.append(s)
    bd = td(bt, d)
    return bt, bd

def gt(nc):
    return list(itertools.permutations(range(nc)))

def ptwl(d):
    ts = gt(len(d))
    for t in ts:
        tl = td(t, d)
        print("Tour:", t, "Length:", tl)

sn = int(input("Enter the start node: "))
ptwl(d)
bt, bd = ac(d, sn)
print("Best tour:", bt)
print("Length of best tour:", bd)

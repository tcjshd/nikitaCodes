import random

def td(p, d):
    t = 0
    for i in range(len(p) - 1):
        t += d[p[i]][p[i+1]]
    t += d[p[-1]][p[0]]  
    return t

def tsp(nc, dm, sn, mi=10000, nr=10):
    bs = None
    bd = float('inf')
    for _ in range(nr):
        cp = list(range(nc))
        cp.remove(sn)  
        random.shuffle(cp)  
        cp.insert(0, sn)  
        cd = td(cp, dm)
        for _ in range(mi):
            np = cp.copy()
            i, j = random.sample(range(1, nc), 2)
            np[i], np[j] = np[j], np[i]
            nd = td(np, dm)
            if nd < cd:
                cp = np
                cd = nd
        if cd < bd:
            bs = cp
            bd = cd
    bs.append(sn)  
    return bs

def main():
    nc = int(input("Enter the number of cities: "))
    sn = int(input("Enter the starting node: "))
    print("Enter the distance matrix (matrix format, separated by spaces):")
    dm = []
    for _ in range(nc):
        r = list(map(int, input().split()))
        dm.append(r)
    sol = tsp(nc, dm, sn)
    print("Best Solution:", sol)
    print("Total Distance:", td(sol, dm))

if __name__ == "__main__":
    main()

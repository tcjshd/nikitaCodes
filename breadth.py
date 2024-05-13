n = int(input("Enter the number of Nodes:"))
m = int(input("Enter the number of Edges:"))

g = [[0]*n for _ in range(n)]    #2D Adjacency matrix initialized to 0
vis = [False]*n                  #Visited array initialized to False


# Queue for BFS
q = []
front = 0
back = 0

def pop():
    global front
    x = q[front]
    front += 1
    return x

def push(x):
    global back
    q.append(x)
    back += 1

def empty():
    return front == back


print("Enter the edges in format - source destination:")
for _ in range(m):
    u, v = map(int, input().split())
    g[u][v] = 1
    g[v][u] = 1  

src = int(input("Enter your Source node: "))
push(src)  # VVIP step Start from source node
vis[src] = True

print("BFS Result:")
while not empty():
    x = pop()
    print(x, end=" ")  
    for y in range(n):
        if g[x][y] == 1 and not vis[y]:
            push(y)
            vis[y] = True

n = int(input("Enter the number of Nodes:"))
m = int(input("Enter the number of Edges:"))

g = [[0]*n for _ in range(n)]    #2D Adjacency matrix initialized to 0
vis = [False]*n                  #Visited array initialized to False

def dfs(x):
    vis[x] = True
    print(x, end=" ")
    for y in range(n):
        if g[x][y] == 1 and not vis[y]:
            dfs(y)

print("Enter the edges:")
for _ in range(m):
    u, v = map(int, input().split())
    g[u][v] = 1
    g[v][u] = 1

src = int(input("Enter your Source node: "))
print("Applying DFS on graph\nYour result is: ", end="")
dfs(src)

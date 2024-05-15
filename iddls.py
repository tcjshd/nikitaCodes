n = int(input("Enter the number of Nodes:"))
m = int(input("Enter the number of Edges:"))

g = [[0]*n for _ in range(n)]    #2D Adjacency matrix initialized to 0

def dfs(x, limit):
    stack = [(x, 0)]
    visited = [False]*n

    while stack:
        node, current_depth = stack.pop()
        if not visited[node]:
            print(node, end=" ")
            visited[node] = True
            if current_depth < limit:
                for y in range(n):
                    if g[node][y] == 1:
                        stack.append((y, current_depth + 1))

print("Enter the edges:")
for _ in range(m):
    u, v = map(int, input().split())
    g[u][v] = 1
    g[v][u] = 1

src = int(input("Enter your Source node: "))
max_depth = int(input("Enter the maximum depth: "))
print("Applying IDDFS on graph\nYour result is: ", end="")
for depth_limit in range(max_depth + 1):
    print("\nDepth limit:", depth_limit)
    dfs(src, depth_limit)

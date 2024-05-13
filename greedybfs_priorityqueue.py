from queue import PriorityQueue

n = int(input("Enter the number of Nodes: "))
m = int(input("Enter the number of Edges: "))

g = [[0]*n for _ in range(n)]    # 2D Adjacency matrix initialized to 0
vis = [False]*n                  # Visited array initialized to False
heuristic = [0] * n              # Heuristic array initialized to 0


def best_first_search(src, target, n):
    pq = PriorityQueue()
    pq.put((0, src, 0))  # (heuristic, current node, total cost)
    vis[src] = True
     
    while not pq.empty():
        heuristic_cost, u, total_cost = pq.get()
        print(u, end=" ")
        if u == target:
            print(f"\nTotal Cost: {total_cost}")
            break

        for v in range(n):
            if g[u][v] > 0 and not vis[v]:
                vis[v] = True
                pq.put((heuristic[v], v, total_cost + g[u][v]))  
    print()



print("Enter the edges (format: 'node1 node2 cost'): ")
for _ in range(m):
    u, v, cost = map(int, input().split())
    g[u][v] = cost

print("Enter heuristic values for each node:")
for i in range(n):
    heuristic[i] = int(input(f"Enter heuristic value for node {i}: "))

src = int(input("Enter your Source node: "))
target = int(input("Enter your Target node: "))

print("Applying Greedy BFS on graph\nYour result is: ", end="")
best_first_search(src, target, n)

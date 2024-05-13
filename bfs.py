from collections import defaultdict, deque

def bfs(adj, start):
    q = deque([start])
    visited = set([start])

    print("BFS Result:")
    while q:
        node = q.popleft()
        print(node, end=' ')
        for neighbor in adj[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

def main():
    n = int(input("Enter the number of Nodes (n): "))
    adj = defaultdict(list)

    print("Enter the adjacency list:")
    for _ in range(n):
        node, *neighbors = map(int, input().split())
        adj[node].extend(neighbors)

    start = int(input("Enter your Source node: "))
    bfs(adj, start)

if __name__ == "__main__":
    main()

def dfs(node, adj, visited):
    visited[node] = True
    print(node, end=' ')
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited)

def main():
    n = int(input("Enter the number of Nodes (n): "))
    adj = [[] for _ in range(n)]
    visited = [False] * n

    print("Enter the adjacency list:")
    for i in range(n):
        nodes = list(map(int, input().split()))
        adj[i].extend(nodes[1:])  # Skip the first element (node number)

    start_node = int(input("Enter your Source node: "))
    print("Applying DFS on graph\nYour result is:", end=' ')
    dfs(start_node, adj, visited)

if __name__ == "__main__":
    main()

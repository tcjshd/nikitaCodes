graph = {}
heuristic = {}
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    edge_data = input("Enter edge and weight (format: 'node1 node2 weight'): ").split()
    node1, node2, weight = edge_data
    node1, node2 = node1.strip(), node2.strip()  # Remove any leading or trailing whitespace
    weight = int(weight)
    if node1 not in graph:
        graph[node1] = {}
    if node2 not in graph:
        graph[node2] = {}
    graph[node1][node2] = weight
    graph[node2][node1] = weight

for node in graph:
    h = int(input(f"Enter heuristic value for node {node}: "))
    heuristic[node] = h

visited = set()
visited.add(start)
path = [start]
current = start
path_cost = 0

while current != goal:
    min_cost = float('inf')
    neighbours = graph[current]
    for neighbour, weight in neighbours.items():
        cost = heuristic[neighbour] + weight  # Add heuristic and edge weight
        if cost < min_cost and neighbour not in visited:
            min_cost = cost
            best = neighbour
    path_cost += graph[current][best]  # Add edge weight to path cost
    path.append(best)
    visited.add(best)
    current = best

for node in path:
    print(f'{node}', end='->')
print(f'Stop (Path Cost: {path_cost})')

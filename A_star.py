graph = {}
while True:
    node = input("Enter node (or type 'done' to finish): ")
    if node == 'DONE':
        break
    edges = []
    while True:
        edge = input(f"Enter neighbor node and its cost for node {node} (or type 'done' to finish): ")
        if edge == 'DONE':
            break
        neighbor, cost = edge.split()
        edges.append([neighbor, int(cost)])
    graph[node] = edges
 
heuristics = {}
for node in graph:
    heuristic = int(input(f"Enter heuristic value for node {node}: "))
    heuristics[node] = heuristic

start = input("Enter start node: ")
goal = input("Enter goal node: ")

visited = set()
queue = [(start, heuristics[start], [start], 0)]

while queue:
    queue.sort(key=lambda x: x[1])
    current, est_cost, path, act_cost = queue.pop(0)
    if current == goal:
        print(f'The goal is reached')
        print(f'The path is: {path}')
        print(f'The cost is: {act_cost}')
        break
			
    if current not in visited:
        visited.add(current)
        neighbors = graph[current]
        for node, edge_cost in neighbors:
            if node not in visited:
                queue.append((node, est_cost - heuristics[current] + heuristics[node] + edge_cost, path + [node], act_cost + edge_cost))

from collections import deque
def topological_sort(vertices, adj):
    indegree = [0] * vertices
    topo_order = []  

    for i in range(vertices):
        for neighbor in adj[i]:
            indegree[neighbor] += 1
    queue = deque()

    for i in range(vertices):
        if indegree[i] == 0:
            queue.append(i)


    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)


    if len(topo_order) == vertices:
        return topo_order
    else:
        return "Graph contains a cycle. Topological sort not possible."

vertices = 6
adj = [
    [2, 3],    # Node 0
    [3, 4],    # Node 1
    [5],       # Node 2
    [],        # Node 3
    [5],       # Node 4
    []         # Node 5
]

topo_order = topological_sort(vertices, adj)
print("Topological Sort Order:", topo_order)

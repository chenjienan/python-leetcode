

def getCriticalPoint(nodes, edges):

    graph = createGraph(nodes, edges)
    time = 0

    visited = [False] * nodes               # index: node value: seen or not
    discovery = [float("inf")] * nodes      # index: node
    low = [float("inf")] * nodes            # index: node
    parent = [-1] * nodes                   # index: node value: parent node
    critical_points = [False] * nodes 

    for node in range(nodes):
        if not visited[node]:
            dfs(graph, node, time, visited, parent, low, discovery, critical_points)

    res = []
    for i, v in enumerate(critical_points):
        if v: res.append(i)
    
    return res

def dfs(graph, cur_node, time, visited, parent, low, discovery, critical_points):
    children = 0
    visited[cur_node] = True
    discovery[cur_node] = time
    low[cur_node] = time
    time += 1

    for nxt_node in graph[cur_node]:
        if not visited[nxt_node]:
            parent[nxt_node] = cur_node
            children += 1
            dfs(graph, nxt_node, time, visited, parent, low, discovery, critical_points)

            low[cur_node] = min(low[cur_node], low[nxt_node])

            if parent[cur_node] == -1 and children > 1:
                critical_points[cur_node] = True

            if parent[cur_node] != -1 and low[nxt_node] >= discovery[cur_node]:
                critical_points[cur_node] = True
        
        elif nxt_node != parent[cur_node]:
            low[cur_node] = min(low[cur_node], discovery[nxt_node])

def createGraph(nodes, edges):

    graph = {i : set() for i in range(nodes)}
    for n1, n2 in edges:
        graph[n1].add(n2)
        graph[n2].add(n1)

    return graph

nodes = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

print(getCriticalPoint(nodes, edges))
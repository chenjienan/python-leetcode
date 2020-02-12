def getCriticalConnections(nodes, edges):

    graph = createGraph(nodes, edges)
    time = 0
    
    nodes = nodes + 1

    visited = [False] * nodes               # index: node value: seen or not
    discovery = [float("inf")] * nodes      # index: node value: from root to node
    low = [float("inf")] * nodes            # index: node value: shortcut from root to node
    parent = [-1] * nodes                   # index: node value: parent node
    critical_connections = []

    for node in range(1, nodes):
      if not visited[node]:
        dfs(graph, node, time, visited, parent, low, discovery, critical_connections)
    
    return critical_connections

def dfs(graph, cur_node, time, visited, parent, low, discovery, critical_connections):    
    visited[cur_node] = True
    discovery[cur_node] = time
    low[cur_node] = time
    time += 1

    for nxt_node in graph[cur_node]:
      if not visited[nxt_node]:
        parent[nxt_node] = cur_node        
        dfs(graph, nxt_node, time, visited, parent, low, discovery, critical_connections)

        low[cur_node] = min(low[cur_node], low[nxt_node])

        if low[nxt_node] > discovery[cur_node]:
          critical_connections.append([cur_node, nxt_node])
      
      # update low of cur_node
      elif nxt_node != parent[cur_node]:
        low[cur_node] = min(low[cur_node], discovery[nxt_node])

def createGraph(nodes, edges):
  # nodes start from 1 to n
  graph = {i + 1: [] for i in range(nodes)}
  for n1, n2 in edges:
    graph[n1].append(n2)
    graph[n2].append(n1)

  return graph

n = 5
edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]

n = 6
edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]

n = 9
edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]


print(getCriticalConnections(n, edges))
# print(createGraph(n, edges))
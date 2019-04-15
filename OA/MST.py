# connect all city with least cost
numTotalAvailableCities = 6
numTotalAvailableRoads = 3
roadsAvailable = [[1, 4], [4, 5], [2, 3]]
numNewRoadsConstruct = 4
costNewRoadsConstruct = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]

# 这是个最小生成树（MST）问题。但要注意整个图中已经有一些边了，不是从0开始的最小生成树。
# 1. Union-Find所有已经有的路 in roadsAvailable list
# 2. 把所有可以建的路 in costNewRoadsConstruct list 按照 cost 排序放入 min-heap
# 3. 次从 min-heap 中拿出最小 cost 的路来接着 Union-Find整个图。每次需要Union的时候，累积目前为止的cost。
# 4. 当总的 edges 数目等于总的 vertices 数目减 1 时，整个图就被构建成了一颗树。这时累积的cost作为输出。


def getMinimumCostToConstruct(numTotalAvailableCities,
                              numTotalAvailableRoads,
                              roadsAvailable,
                              numNewRoadsConstruct,
                              costNewRoadsConstruct):
                    
    if numTotalAvailableCities < 2 or \
        numTotalAvailableRoads >= numTotalAvailableCities - 1:
        return 0

    # construct a graph with UnionFind
    cur_road_cnt = 0
    uf = UnionFind(numTotalAvailableCities)
    for pair in roadsAvailable:
        city1 = pair[0]
        city2 = pair[1]
        if not uf.query(city1, city2):
            uf.union(city1, city2)
            cur_road_cnt += 1

    # construct a heap with new roads
    import heapq
    h = []
    for newRoad in costNewRoadsConstruct:
        city1, city2, cost = newRoad[0], newRoad[1], newRoad[2]
        t = (cost, city1, city2)
        heapq.heappush(h, t)        # add new road according to cost
    
    new_road_cost = []
    # tree: total edges =  total vertices - 1
    # total edges = cur_road_cnt + net_road_cnt
    while h and len(new_road_cost) + cur_road_cnt < numTotalAvailableCities - 1:
        new_road = heapq.heappop(h)
        cost = new_road[0]
        city_x = new_road[1]
        city_y = new_road[2]

        if not uf.query(city_x, city_y):
            uf.union(city_x, city_y)
            new_road_cost.append(cost)

    if len(new_road_cost) + cur_road_cnt < numTotalAvailableCities - 1:
        return -1
    
    return sum(new_road_cost)

class UnionFind:

    def __init__(self, n):
        self.father = {}
        for i in range(1, n+1):
            self.father[i] = i

    def union(self, a, b):
        self.father[self.find(a)] = self.find(b)
            
    def find(self, node):
        path = []
        
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]
        
        for temp in path:
            self.father[temp] = node        
        return node

    def query(self, a, b):
        return self.find(a) == self.find(b)

print(getMinimumCostToConstruct(6,
                              3,
                              [[1, 4], [4, 5], [2, 3]],
                              4,
                              [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))
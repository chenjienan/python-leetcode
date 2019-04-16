# connect all city with least cost
# numTotalAvailableCities = 6
# numTotalAvailableRoads = 3
# roadsAvailable = [[1, 4], [4, 5], [2, 3]]
# numNewRoadsConstruct = 4
# costNewRoadsConstruct = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
numTotalAvailableCities = 5
numTotalAvailableRoads = 5
roadsAvailable = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
numNewRoadsConstruct = 3
costNewRoadsConstruct = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]



# 这是个最小生成树（MST）问题。但要注意整个图中已经有一些边了，不是从0开始的最小生成树。
# 1. Union-Find所有已经有的路 in roadsAvailable list
# 2. 把所有可以建的路 in costNewRoadsConstruct list 按照 cost 排序放入 min-heap
# 3. 次从 min-heap 中拿出最小 cost 的路来接着 Union-Find整个图。每次需要Union的时候，累积目前为止的cost。
# 4. 当总的 edges 数目等于总的 vertices 数目减 1 时，整个图就被构建成了一颗树。这时累积的cost作为输出。


def getMinimumCostToRepair(numTotalAvailableCities, 
                           numTotalAvailableRoads, 
                           roadsAvailable, 
                           numRoadsToBeRepaired, 
                           costRoadsToBeRepaired):
    # WRITE YOUR CODE HERE
    
    # if numTotalAvailableCities < 2 or numTotalAvailableRoads >= numTotalAvailableCities - 1:
    #     return 0
    
    existing_roads = roadsAvailable
    for road in costRoadsToBeRepaired:
        road_to_repair = [road[0], road[1]]
        existing_roads.remove(road_to_repair)
    
    cur_road_cnt = 0
    uf = UnionFindSet(numTotalAvailableCities)
    
    for pair in existing_roads:
        city_x = pair[0]
        city_y = pair[1]
        
        if not uf.query(city_x, city_y):
            uf.union(city_x, city_y)
            cur_road_cnt += 1
            
    import heapq
    h = []
    for new_road in costRoadsToBeRepaired:
        city_x, city_y, cost = new_road[0], new_road[1], new_road[2]
        t = (cost, city_x, city_y)
        heapq.heappush(h, t)
        
    repair_road_cost = []
    while h and len(repair_road_cost) + cur_road_cnt < numTotalAvailableCities - 1:
        new_road = heapq.heappop(h)
        cost, city_x, city_y = new_road[0], new_road[1], new_road[2]
        
        if not uf.query(city_x, city_y):
            uf.union(city_x, city_y)
            repair_road_cost.append(cost)
    
    if len(repair_road_cost) + cur_road_cnt < numTotalAvailableCities - 1:
        return -1
    
    return sum(repair_road_cost)


class UnionFindSet:
    
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
            
        for p in path:
            self.father[p] = node
        
        return node
    
    def query(self, a, b):
        return self.find(a) == self.find(b)

print(getMinimumCostToRepair(5,
                              5,
                              [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],
                              3,
                              [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
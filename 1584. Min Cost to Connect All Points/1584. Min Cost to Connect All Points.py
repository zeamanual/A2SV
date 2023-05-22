class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(i):
            if stat[i] == i:
                return i
            return find(stat[i])

        def union(rank, x, y):
            x_root = find(x)
            y_root = find(y)

            if rank[x_root] < rank[y_root]:
                stat[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                stat[y_root] = x_root
            else:
                stat[y_root] = x_root
                rank[x_root] += 1

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + \
                    abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        edges.sort() 

        stat = [i for i in range(n)]
        rank = [0] * n
        cost = 0
        num_edges = 0

        for edge in edges:
            dist, u, v = edge
            if find(u) != find(v):
                union(rank, u, v)
                cost += dist
                num_edges += 1
                if num_edges == n - 1:
                    break

        return cost

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        adj_list = defaultdict(list)

        for v1,v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        n = len(adj_list.keys())
        center = 0
        for vertice in adj_list.keys():
            if(len(adj_list[vertice])==n-1):
                return vertice

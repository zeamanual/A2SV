class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_ls = defaultdict(list)   
        in_degree  = [ 0 for i in range(n) ]

        for index, edge in enumerate(edges):
             adj_ls[edge[0]].append(edge[1])
             in_degree[edge[1]]+=1


        ancestors = [ set() for i in range(n)]
        que = deque()
        for n in range(n):
            if(in_degree[n]==0):
                que.append(n)

        while(que):
            curr = que.popleft()
            for nbr in adj_ls[curr]:
                ancestors[nbr].add(curr)
                ancestors[nbr] = ancestors[nbr].union(ancestors[curr])
                in_degree[nbr]-=1
                if(in_degree[nbr]==0):
                    que.append(nbr)
            
        ancestors = list(map(lambda ances: sorted(ances),ancestors))
        return ancestors

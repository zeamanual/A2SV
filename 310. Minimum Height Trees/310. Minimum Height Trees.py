class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)

        for n1, n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)

        que = deque()

        for i in range(n):
            if( len(adj[i]) ==1 ):
                que.append(i)

        while(que and len(adj.keys())>2):
            curr_leafs = que
            new_que = deque()
            for leaf in curr_leafs:
                for nbr in adj[leaf]:
                    adj[nbr].discard(leaf)
                    if(len(adj[nbr])==1):
                        new_que.append(nbr)
                del adj[leaf]
            que = new_que

        return list(adj.keys())

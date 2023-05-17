class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        stat = [i for i in range(n)]
        
        def get_rep(node):
            rep = stat[node]
            while(rep!=node):
                node = stat[rep]
                rep = stat[node]
            
            return rep

        def union(node1, node2):
            node1_rep = get_rep(node1)
            node2_rep = get_rep(node2)

            stat[node1_rep]=node2_rep
        
        for edge in edges:
            union(edge[0],edge[1])

        
        return get_rep(source)==get_rep(destination)

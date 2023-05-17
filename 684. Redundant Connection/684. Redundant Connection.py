class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        stat = [i for i in range(1001)]
        
        def get_rep(node):
            rep = stat[node]
            while(rep!=node):
                node = stat[rep]
                rep = stat[node]
            
            return rep
        answer = []
        def union(node1, node2):
            nonlocal answer
            node1_rep = get_rep(node1)
            node2_rep = get_rep(node2)
            if(node1_rep ==node2_rep ):
                answer =[node1,node2]

            stat[node1_rep]=node2_rep
        
        for edge in edges:
            union(edge[0],edge[1])

        
        return answer

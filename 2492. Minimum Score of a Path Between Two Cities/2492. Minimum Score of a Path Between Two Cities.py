class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        stat = [i for i in range (n+1)]
        rank = [1 for i in range (n+1)]
        scores = [ float('inf') for i in range(n+1)]

        def union(n1, n2,dis):
            rep1 = get_rep(n2)
            rep2 = get_rep(n1)

            if(rep1 == rep2):
                scores[rep1]=min(scores[rep1],scores[rep2],dis)  
                return

            if(rank[rep2]==rank[rep1]):
                rank[rep2]+=1
                stat[rep1]=rep2
                scores[rep2] = min(scores[rep1],scores[rep2],dis)   
            elif(rank[rep2]>rank[rep1]):
                stat[rep1]=rep2
                scores[rep2] = min(scores[rep1],scores[rep2],dis)   
            else:
                stat[rep2]=rep1
                scores[rep1] = min(scores[rep1],scores[rep2],dis)   


        def get_rep(node):
            rep = stat[node]
            if(rep !=node):
                stat[node] = get_rep(rep)
            return stat[node] 

        def is_connected(n1, n2):
            n1_rep = get_rep(n1)
            n2_rep = get_rep(n2)
            return n1_rep == n2_rep

        for road in roads:
            union(road[0],road[1],road[2])

        return scores[get_rep(1)]

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)

        for index,edge in enumerate(edges):
            node1,node2 = edge
            graph[node1].append((node2,succProb[index]))
            graph[node2].append((node1,succProb[index]))

        probbs=defaultdict(lambda :0)
        visited = set()
        que = [(-1,start_node)]
        
        while(que):
            curr_prob,curr_node = heapq.heappop(que)
            visited.add(curr_node)

            if(probbs[curr_node]<-(curr_prob)):
                probbs[curr_node]=-curr_prob

            for nbr,prob in graph[curr_node]:
                if(nbr not in visited):
                    heapq.heappush(que,(curr_prob*prob,nbr))

        return probbs[end_node]

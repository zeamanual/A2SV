class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for fro,to,price in flights:
            graph[fro].append((to,price))

        heap = [(0,1,src)]    
        costs=defaultdict(lambda : float('inf'))    

        answer = float('inf')
        visited= set()
        while(heap):

            curr_cost,nodes,curr_node,=heapq.heappop(heap)

            if((curr_node,nodes) in visited):
                continue

            if(curr_node==dst):
                answer = min(answer,curr_cost)
            visited.add((curr_node,nodes))

            for nbr,cost in graph[curr_node]:
                if((nbr,nodes+1 ) not in visited and (nodes+1)-2<=k):
                    costs[nbr]=min(curr_cost+cost,costs[nbr])
                    heapq.heappush(heap,(curr_cost+cost,nodes+1,nbr))

        return answer if answer !=float('inf') else -1

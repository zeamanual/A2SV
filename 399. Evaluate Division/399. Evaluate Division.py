class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for index, (start,end) in enumerate(equations):
            graph[start].append((end,values[index]))
            graph[end].append((start,1/values[index] if values[index]!=0 else 0))


        answer = []
        for start,end in queries:
   
            distances = defaultdict(lambda : float('inf'))
            que = [(1,start)]
            distances[start]=1 if start!=end else float('inf')
            while(que):
                cost,node = que.pop()

                for nbr,nbr_cost in graph[node]:
                    if(distances[nbr]>cost*nbr_cost):
                        distances[nbr]=cost*nbr_cost
                        que.append((cost*nbr_cost,nbr))

            answer.append(distances[end] if distances[end]!=float('inf') else -1)
        return answer

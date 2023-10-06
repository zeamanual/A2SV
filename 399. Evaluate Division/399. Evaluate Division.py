class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for index, (start,end) in enumerate(equations):
            graph[start].append((end,values[index]))
            graph[end].append((start,1/values[index] if values[index]!=0 else 0))


        answer = []
        for start,end in queries:
   
            evaluations = defaultdict(lambda : float('inf'))
            que = [(1,start)]
            evaluations[start]=1 if start!=end else float('inf')
            while(que):
                weight,node = que.pop()

                for nbr,nbr_weight in graph[node]:
                    if(evaluations[nbr]>weight*nbr_weight):
                        evaluations[nbr]=weight*nbr_weight
                        que.append((weight*nbr_weight,nbr))

            answer.append(evaluations[end] if evaluations[end]!=float('inf') else -1)
        return answer

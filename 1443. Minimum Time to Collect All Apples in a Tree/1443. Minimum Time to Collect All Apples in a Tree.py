class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        graph= defaultdict(list)
        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = set()

        def dfs(curr):
            nonlocal visited 
            visited.add(curr)
            total_cost = 0
            curr_has_apple = hasApple[curr]
            for nbr in graph[curr]:
                if(nbr not in visited):
                    child_has_apple,child_cost = dfs(nbr)
                    if(child_has_apple):
                        total_cost+=2+child_cost
                        curr_has_apple=True

            return curr_has_apple,total_cost

        return dfs(0)[1]

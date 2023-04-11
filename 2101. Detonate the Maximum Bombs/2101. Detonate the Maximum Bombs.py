class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        n =  len(bombs)
        graph = defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if bombs[i][2]**2 >= (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2:
                    graph[i].append(j)
        
        def dfs(bomb):
            nonlocal visited

            for nbr in graph[bomb]:
                if(nbr not in visited):
                    visited.add(nbr)
                    dfs(nbr)

        max_possible = 0
        keys = list(graph.keys()).copy()
        for node in keys:
            visited = set()
            visited.add(node)
            dfs(node)
            max_possible=max(max_possible,len(visited))

        return max_possible

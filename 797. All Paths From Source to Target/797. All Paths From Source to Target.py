class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph)
        paths = []
        def dfs(node,curr_path):

            if(node == n-1):
                paths.append(curr_path.copy())
                return 

            for nbr in graph[node]:
                curr_path.append(nbr)
                dfs(nbr,curr_path)
                curr_path.pop()

        
        dfs(0,[0])

        return paths

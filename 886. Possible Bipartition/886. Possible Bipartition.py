class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for edge in dislikes:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        colors = [0 for i in range(n+1)]
        for node in graph.keys():
            if(not colors[node]):
                if(not self.dfs(node,graph,colors,1)):
                    return False
        return True

    def dfs(self,node,graph,colors,curr_color):

        if(colors[node] != 0):
            if(colors[node]==curr_color):
                return True
            else:
                return False
            
        colors[node]=curr_color
        for nbr in graph[node]:
            if(not self.dfs(nbr,graph,colors,-curr_color)):
                return False

        return True

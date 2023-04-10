class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row = len(isConnected)
        col = len(isConnected[0])
        graph = dict()
        visited = [False for i in range(col+1)]

        def dfs(node):
            nonlocal visited
            for nbr in graph[node]:
                if(not visited[nbr]):
                    visited[nbr] = True
                    dfs(nbr)

        for row_count in range(row):
            graph[row_count+1]=set()
            curr_row = isConnected[row_count]
            for col_count in range(col):
                if( row_count != col_count and  isConnected[row_count][col_count]==1):
                    graph[row_count+1].add(col_count+1)

        count = 0
        for node in graph:
            if(not visited[node]):
                visited[node]=True
                count+=1
                dfs(node)

        return count
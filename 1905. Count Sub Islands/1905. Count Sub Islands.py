class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        directions = [[0,-1],[-1,0],[0,1],[1,0]]

        def is_valid(row,col):
            return 0<=row<len(grid2) and 0 <=col<len(grid2[0])

        def dfs(row,col):
            nonlocal visited
            nonlocal directions
            nonlocal is_sub_island
            if(is_valid(row,col)) and grid2[row][col]==1:
                visited.add((row,col))

                if(grid1[row][col]==0):
                    is_sub_island = False
               
                for r,c in directions:
                    if((r+row,c+col) not in visited):
                        dfs(r+row,c+col)


        visited = set()
        count = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if((row,col) not in visited and grid2[row][col]!=0):
                    is_sub_island=True
                    dfs(row,col)

                    count+=1 if is_sub_island else 0

        return count

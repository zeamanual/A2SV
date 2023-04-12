class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows,cols = len(grid),len(grid[0])
        visited = set()
        max_area = 0

        def is_valid(x,y):
            return x < rows and x >= 0 and y < cols and y >= 0

        def dfs(curr):
            nonlocal grid
            nonlocal visited
            nonlocal max_area
            nonlocal curr_area

            visited.add((curr[0],curr[1]))
            if(grid[curr[0]][curr[1]] != 1):
                return
            curr_area+=1
            grid[curr[0]][curr[1]]=0
            max_area = max(max_area,curr_area)
            for dir_cor in directions:
                new_x, new_y = curr[0]+dir_cor[0],curr[1]+dir_cor[1]
                if(is_valid(new_x,new_y) and (new_x, new_y) not in visited):
                    dfs((new_x,new_y))

        curr_area = 0
        for i in range(rows):
            for j in range(cols):
                dfs((i,j))
                visited = set()
                curr_area = 0
    
        return max_area

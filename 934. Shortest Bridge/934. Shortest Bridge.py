class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        que = deque()
        starting_index = (0,0)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col]==1):
                    starting_index=(row,col)

        def in_bound(x,y):
            return 0<=x<len(grid) and 0<=y<len(grid[0])

        visited = set()
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(cord):
            nonlocal visited
            nonlocal que

            if(grid[cord[0]][cord[1]]==0):
                return
            visited.add(cord)
            que.append([cord,0])

            for move in moves:
                new_x,new_y = cord[0]+move[0], cord[1]+move[1]
                if(in_bound(new_x,new_y) and (new_x,new_y) not in visited):
                    dfs((new_x,new_y))

        dfs(starting_index)
        min_distance = float('inf')
        while(que):

            cord, distance = que.popleft()
            if(distance!=0 and grid[cord[0]][cord[1]]==1):
                min_distance = min(min_distance,distance)

            for move in moves:
                new_x,new_y = cord[0]+move[0], cord[1]+move[1]
                if(in_bound(new_x,new_y) and (new_x,new_y) not in visited):
                    visited.add((new_x,new_y))
                    que.append([(new_x,new_y),distance+1])
        return min_distance-1

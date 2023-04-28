class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        moves = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        n = len(grid)
        visited = set()

        def is_valid(x,y):
            return 0<=x<n and 0<=y<n

        que = deque([[(0,0),1]])

        while(que):
            curr,count = que.popleft()
            if grid[curr[0]][curr[1]] != 0:
                continue 

            if(curr==(n-1,n-1)):
                return count

            for move in moves:
                new_x,new_y = curr[0] + move[0], curr[1] + move[1]
                if(is_valid(new_x,new_y) and (new_x,new_y) not in visited):
                    visited.add((new_x, new_y))
                    que.append([(new_x,new_y),count+1])

        return -1

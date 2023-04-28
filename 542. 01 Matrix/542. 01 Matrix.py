class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m,n = len(mat),len(mat[0])
        answer = [[ float('inf') for i in range(n)] for j in range(m)]
        visited = set()
        que = deque()
        for x in range(m):
            for y in range(n):
                if(mat[x][y]==0):
                    answer[x][y]=0
                    visited.add((x,y))
                    que.append([(x,y),0])
                    
        self.bfs(visited,answer,mat,que)
        return answer

    def bfs(self,visited,answer,mat,que):
        
        m,n = len(mat),len(mat[0])
        moves = [[-1,0],[0,1],[1,0],[0,-1]]

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y <n

        while(que):
            curr, distance = que.popleft()
            for move in moves:
                new_x,new_y = curr[0] + move[0] , curr[1] + move[1]
                if(is_valid(new_x,new_y) and (new_x,new_y) not in visited):
                    visited.add((new_x,new_y))
                    answer[new_x][new_y]=distance+1
                    que.append([(new_x,new_y),distance+1])

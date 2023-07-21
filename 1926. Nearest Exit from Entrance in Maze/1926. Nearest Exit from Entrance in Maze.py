class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        moves = [[1,0],[0,1],[0,-1],[-1,0]]
        def in_bound(pos):
            row,col = pos
            return 0<=row<len(maze) and 0<=col<len(maze[0])

        visited = set()
        que = deque([(entrance[0],entrance[1],0)])
        min_step = float('inf')

        while(que):
            curr = que.popleft()
            for move in moves:
                next = (move[0]+curr[0],move[1]+curr[1])
                if(in_bound(next) and next not in visited and maze[next[0]][next[1]]=='.'):
                    visited.add(next)
                    que.append((next[0],next[1],curr[2]+1))

                if(not in_bound(next) and (entrance[0]!=curr[0] or entrance[1]!=curr[1])):
                    min_step=min(min_step,curr[2])

        return min_step if min_step!=float('inf') else -1

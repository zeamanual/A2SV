class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        def in_bound(cord):
            return 0<=cord[0]<m and 0<=cord[1]<n

        moves = [[0,1],[0,-1],[1,0],[-1,0],]
        def dfs(cord):
            nonlocal curr_area_valid
            nonlocal temp
            nonlocal visited
            visited.add(cord)
            temp.add(cord)

            for move in moves:
                new_cord = (cord[0]+move[0],cord[1]+move[1])
                if(not in_bound(new_cord)):
                    curr_area_valid=False
                elif(board[new_cord[0]][new_cord[1]]=='O' and new_cord not in visited):
                    visited.add(new_cord)
                    dfs(new_cord)
                
        visited,curr_area_valid, temp= set(),True,set()
        for i in range(m):
            for j in range(n):
                curr_area_valid=True
                temp = set()
                curr_cord = (i,j)

                if(board[i][j]=='O' and curr_cord not in visited):
                    dfs(curr_cord)

                if(curr_area_valid):
                    for cord in temp:
                        board[cord[0]][cord[1]]="X"

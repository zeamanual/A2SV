class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        directions = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        def is_valid(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def dfs(row,col):

            if(not is_valid(row,col)):
                return 

            if(board[row][col]=='M'):
               board[row][col]='X'
               return

            if(board[row][col]=='E'):
                adj_mines = 0
                for x,y in directions:
                    adj_mines+=1 if( is_valid(row+x,col+y ) and board[row+x][col+y]=='M') else 0
                if(not adj_mines):
                    board[row][col]='B'
                else:
                    board[row][col]=f'{adj_mines}'
                    return

                for x,y in directions:
                    dfs(row+x,col+y)              

        dfs(click[0],click[1])
        return board

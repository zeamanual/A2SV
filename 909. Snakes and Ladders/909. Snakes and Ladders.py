class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        def get_cor(num):
            row = max(0,len(board)-ceil(num/len(board)))
            col = max((num-1)%len(board),0) 
            if (len(board) - row) % 2 == 0:
               col = (len(board)-1)-col

            return row,col
        
        que = deque([(1,0)])
        visited = set([1])
        while(que):
            curr,moves = que.popleft()

            if(curr==len(board)**2):
                return moves

            for next_move in range(1,7):
                new_desitination = curr+next_move

                if(new_desitination>len(board)**2):
                    break

                row,col = get_cor(new_desitination)

                if(board[row][col]!=-1):
                    new_desitination = board[row][col]

                if(new_desitination not in visited):
                    que.append((new_desitination,moves+1))
                    visited.add(new_desitination)

        return -1

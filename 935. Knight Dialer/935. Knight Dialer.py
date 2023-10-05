class Solution:
    def knightDialer(self, n: int) -> int:

        def get_key(row,col):
            if(row==3 and (col==0 or col==2)):
                return ''
            else:
                return ((row+1)*3)-(2-col)

        def is_valid(row,col):
            return 0<=row<4 and 0<=col<3

        moves = [[-1,-2],[1,-2],[2,-1],[-2,-1],[-2,1],[-1,2],[1,2],[2,1]]

        @lru_cache(None)
        def dp(row,col,remaining):
            if remaining == 0:
                return 1

            curr_answer=0
            for move in moves:
                new_row,new_col=row+move[0],col+move[1]
                if(is_valid(new_row,new_col) and get_key(new_row,new_col)):
                    curr_answer+=dp(new_row,new_col,remaining-1)
            return curr_answer

        answer = 0
        for row in range(4):
            for col in range(3):
                if( get_key(row,col) ):
                    answer+=dp(row,col,n-1)

        return answer%(10**9+7)

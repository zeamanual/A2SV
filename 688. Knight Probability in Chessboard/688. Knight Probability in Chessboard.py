class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        moves = [[-2,-1],[-1,-2],[-2,1],[-1,2],[1,2],[2,1],[1,-2],[2,-1]]

        def in_bound(row,col):
            return 0<=row<n and 0<=col<n

        @lru_cache(None)
        def get_prob(row,col,remaining_moves):
            if(remaining_moves==0):
                return 1

            curr_prob = 0
            for move in moves:
                new_row,new_col = move[0]+row,move[1]+col
                if(in_bound(new_row,new_col)):
                    curr_prob+=get_prob(new_row,new_col,remaining_moves-1)


            return curr_prob/8

        return get_prob(row,column,k)

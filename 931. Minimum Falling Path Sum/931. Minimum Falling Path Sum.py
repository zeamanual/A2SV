class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        moves = [[1,0],[1,1],[1,-1]]
        n = len(matrix)

        @lru_cache(None)
        def minimun_sum(row,col):

            minimum = float('inf')
            for move in moves:
                new_row,new_col = row+move[0],col+move[1]
                if( 0<=new_row<n and 0<=new_col<n ):
                    minimum= min(minimum,minimun_sum(new_row,new_col))

            return matrix[row][col]+minimum if minimum!=float('inf') else matrix[row][col]

        answer=float('inf')
        for i in range(n):
            answer = min(minimun_sum(0,i),answer)

        return answer

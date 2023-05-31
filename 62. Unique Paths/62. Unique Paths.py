class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        answer = [ [0 for i in range(n)] for j in range(m) ]
        answer[m-1][n-1]=1


        for x in range(n-1,-1,-1):
            for y in range(m-1,-1,-1):

                if(x<0 or y<0 or (x== n-1 and y == m-1) ):
                    continue

                if(x + 1 <= n-1):
                    answer[y][x]+=answer[y][x+1]
                
                if( y+1 <= m-1 ):
                    answer[y][x]+=answer[y+1][x]

        return answer[0][0]

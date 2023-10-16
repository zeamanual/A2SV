class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def check_path(x,y):

            if(x==n or y==m):
                return 0

            if(x==n-1 and y == m-1):
                return 1 
            else:
                return check_path(x,y+1) + check_path(x+1,y)

        return check_path(0,0)

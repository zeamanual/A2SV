class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:

        if(n <=1):
            return n
        elif(n==2):
            return 1

        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

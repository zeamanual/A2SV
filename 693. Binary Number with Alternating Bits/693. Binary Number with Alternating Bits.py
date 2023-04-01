class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
       
        return n ^ (n>>1) == 2**(floor(log2(n)) + 1 ) - 1

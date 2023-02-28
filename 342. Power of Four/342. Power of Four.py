class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n==1):
            return True
        elif(n<1):
            return False
        reduced_num = n/4

        return self.isPowerOfFour(reduced_num)

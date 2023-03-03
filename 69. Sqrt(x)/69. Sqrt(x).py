class Solution:
    def mySqrt(self, x: int) -> int:
       
        left,right = 0,x
        while(right-left>1):
            mid = left+(right-left)//2
            if(mid*mid>x):
                right=mid
            else:
                left=mid

        return left if x!=1 else right

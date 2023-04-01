class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)

        return self.find_gcd(max_val,min_val)

    def find_gcd( self,num1,num2 ):
        if( num2 == 0 ):
            return num1

        return self.find_gcd( num2,num1%num2 )

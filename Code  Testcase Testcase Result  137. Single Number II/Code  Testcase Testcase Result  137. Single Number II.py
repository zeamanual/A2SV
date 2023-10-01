class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0  
        twos = 0  

        for num in nums:

            twos |= ones & num
            ones ^= num
            
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes

        return ones     

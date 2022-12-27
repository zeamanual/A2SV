class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        list_size=len(nums)
        nums=set(nums)
        
        for i in range(list_size+1):
            if(i not in nums):
                return i

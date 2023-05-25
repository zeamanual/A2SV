class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if(len(nums)<=3):
            return 0
        nums.sort()
        
        min_val = float('inf')
        for i in range(4):
            min_val = min(min_val,nums[-1-i]-nums[3-i])

        return min_val

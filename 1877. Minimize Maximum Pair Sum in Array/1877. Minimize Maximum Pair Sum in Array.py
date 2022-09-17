class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        last_index = size-1
        max=0
        for index in range(size//2):
            temp_max = nums[last_index-index]+nums[index]
            if(temp_max>max):
                max=temp_max
        return max

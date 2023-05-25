class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if(len(nums)<=3):
            return 0
        nums.sort()
        
        opt1 = nums[-1]-nums[3]
        opt2 = nums[-4]-nums[0]
        opt3 = nums[-2]-nums[2]
        opt4 = nums[-3] - nums[1]

        return min(opt1,opt2,opt3,opt4)

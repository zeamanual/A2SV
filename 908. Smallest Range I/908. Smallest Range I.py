class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        nums.sort()
        return max((nums[-1]-k) - (nums[0]+k),0)

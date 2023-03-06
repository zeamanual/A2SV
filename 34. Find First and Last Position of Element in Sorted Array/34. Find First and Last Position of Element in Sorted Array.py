class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        starting = bisect_left(nums,target)
        ending = bisect_right(nums,target)

        if( (starting>len(nums)-1) or nums[starting]!=target):
            return [-1,-1]
        else:
            return [starting,ending-1]

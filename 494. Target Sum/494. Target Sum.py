class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        self.target = target

        @lru_cache(None)
        def back_track(index,curr):
            if(len(nums)==index):
                return int(curr==self.target)
            return back_track(index+1,curr-nums[index]) + back_track(index+1,curr+nums[index])

        return back_track(0,0)

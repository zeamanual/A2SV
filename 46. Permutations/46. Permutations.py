class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, [], ans)
        return ans

    def backtrack(self, nums, temp, ans):
        if len(nums)==0:
            ans.append(temp)
            return

        for i in range(len(nums)):
            self.backtrack(nums[:i]+nums[i+1:],temp+[nums[i]],ans )

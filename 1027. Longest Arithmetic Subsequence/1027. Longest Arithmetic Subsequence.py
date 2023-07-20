class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        if(len(nums)<=2):
            return len(nums)

        dp = [ defaultdict(lambda : 1) for i in range(len(nums))]
        answer = 2

        for end_index in range(len(nums)):
            
            for curr_index in range(end_index):
                curr_diff = nums[end_index]-nums[curr_index]
                
                dp[end_index][curr_diff] = dp[curr_index][curr_diff]+1
                answer = max(answer,dp[end_index][curr_diff])

        return answer

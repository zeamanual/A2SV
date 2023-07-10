class Solution:

    def maxScoreSightseeingPair(self, values: List[int]) -> int:  
        
        arr_size = len(values)
        dp = [0]*(arr_size)
        dp[0] = values[0]
        answer = 0
        
        for i in range(1, arr_size):
            dp[i] = max(dp[i-1], values[i-1]+i-1)
            answer = max(answer, dp[i]+values[i]-i)
        
        return answer

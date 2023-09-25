class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        data = []
        for i in range(len(ages)):
            data.append((ages[i],scores[i]))

        data.sort()
        dp = [data[i][1] for i in range(len(data))]

        for i in range(len(data)):
            for j in range(i):
                if( data[j][1] <= data[i][1] ):
                    dp[i] = max(dp[i],data[i][1]+dp[j])


        return max(dp)

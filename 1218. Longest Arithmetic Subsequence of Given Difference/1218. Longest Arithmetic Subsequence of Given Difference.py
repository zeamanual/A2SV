class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        memo = defaultdict(lambda: 1)
        ans = 0
        for i in range(len(arr)):
            curr = arr[i]
            if( curr-difference in memo):
                print('uba')
                memo[curr] = max(memo[curr],memo[curr-difference]+1)
            ans= max(ans,memo[curr])


        return ans

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        arr = [ 0 for i in range(len(nums)+1)]

        for req in requests:
            arr[req[0]]+=1
            arr[req[1]+1]-=1
        
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]


        arr.pop()
        arr.sort(reverse=True)
        nums.sort(reverse=True)
        ans=0
        for i in range(len(arr)):
            ans+=(arr[i]*nums[i])
        
        return ans%(10**9+7)

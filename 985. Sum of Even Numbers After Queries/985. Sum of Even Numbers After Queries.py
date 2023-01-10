class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        answer = []

        # initial even sum
        sum=0
        for num in nums:
            if(num%2==0):
                sum+=num
                
        for query in queries:

            if(nums[query[1]]%2==0):
                sum-=nums[query[1]]
            nums[query[1]]+=query[0]
            if(nums[query[1]]%2==0):
                sum+=nums[query[1]]

            answer.append(sum)

        return answer



class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0:1}

        curr_sum = 0
        count=0
        for num in nums:
            curr_sum+=num
            remainder = curr_sum%k
            count+=dic.get(remainder,0)
            dic[remainder]=dic.get(remainder,0)+1

        return count

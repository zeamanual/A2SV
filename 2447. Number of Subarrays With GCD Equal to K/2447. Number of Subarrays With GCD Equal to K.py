class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        count =0

        for i in range(len(nums)):
            current = nums[i]
            for j in range(i,len(nums)):
                current = gcd(current,nums[j])
                if(current==k):
                    count+=1

        return count

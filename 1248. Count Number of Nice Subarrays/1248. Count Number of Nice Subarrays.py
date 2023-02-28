class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        curr_count=0
        dic={0:1}
        count = 0
        for num in nums:

            curr_val = 0 if (num%2==0) else 1
            curr_count+=curr_val
            diff = curr_count-k
            count+=dic.get(diff,0)
            dic[curr_count]=dic.get(curr_count,0)+1
            

        return count

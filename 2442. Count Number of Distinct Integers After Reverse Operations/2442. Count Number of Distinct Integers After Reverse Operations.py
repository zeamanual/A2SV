class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        seen_before=set()
        distinct_count=0

        for num in nums:
            
            reversed_num = int(str(num)[::-1])
            if(num not in seen_before):
                distinct_count+=1
                seen_before.add(num)

            if(reversed_num not in seen_before):
                distinct_count+=1
                seen_before.add(reversed_num)

        return distinct_count

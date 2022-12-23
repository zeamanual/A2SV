class Solution:
    def average(self, salary: List[int]) -> float:

        smallest = float('inf')
        largest= -float('inf')
        salaries_len = len(salary)
        total_sum = 0

        for val in salary:
            largest=max(largest,val)
            smallest=min(smallest,val)
            total_sum+=val

        final_result = (total_sum-largest-smallest)/(salaries_len-2)
        return final_result
        

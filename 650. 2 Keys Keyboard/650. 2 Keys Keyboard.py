class Solution:
    def minSteps(self, n: int) -> int:

        curr_count = 1
        copied = 0
        operations = 0

        while(curr_count<n):

            if(n%curr_count==0):
                copied = curr_count
                operations +=1

            curr_count+=copied
            operations+=1

        return operations

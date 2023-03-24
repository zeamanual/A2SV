class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
       
        final_answer = []
        stored  = set()
        self.solve(final_answer,0,[],nums,stored)

        return final_answer
    
    def solve(self,answer,start,curr,num,visited):

        if(len(curr)>=2 and tuple(curr) not in visited ):
            answer.append(curr.copy())
            visited.add(tuple(curr))

        for i in range(start,len(num)):

            if(curr and curr[-1] > num[i]):
                continue

            curr.append(num[i])
            self.solve(answer,i+1,curr,num,visited)
            curr.pop()

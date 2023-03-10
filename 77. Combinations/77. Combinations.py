class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        self.helper(answer,[],1,n,k)
        
        return answer

    def helper(self,answer,curr,start,n,k):
        if(len(curr)==k):
            answer.append(curr.copy())
        else:
            for i in range(start,n+1):
                curr.append(i)
                self.helper(answer,curr,i+1,n,k)
                curr.pop()

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        start =0
        ans = float('-inf')
        status = defaultdict(int)
        for end in range(len(fruits)):
            status[fruits[end]]+=1

            while(len(status.keys()) > 2):
                status[fruits[start]]-=1
                if(status[fruits[start]]==0):
                    del status[fruits[start]]
                start+=1
            ans = max(ans,end-start+1)
        
        return ans

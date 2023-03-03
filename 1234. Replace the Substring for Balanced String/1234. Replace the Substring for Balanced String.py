class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)

        left_ptr = 0 
        size = len(s)
        required = size/4
        ans = float('inf')
    
        for right in range(size):
            counter[s[right]]-=1
            while(left_ptr<size and max(counter.values()) <=required):
                counter[s[left_ptr]]+=1
                ans = min(ans, right-left_ptr+1)
                left_ptr+=1


        return ans

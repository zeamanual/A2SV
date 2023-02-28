class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        p_sum = [0]*(len(s)+1)
        res=''

        for shift in shifts:
            p_sum[shift[0]]+= 1 if shift[2]==1 else -1
            p_sum[shift[1]+1] += -1 if shift[2]==1 else 1
        
        # computing prefix sum
        for index in range(1,len(p_sum)):
            p_sum[index]+=p_sum[index-1]

        for index in range(len(s)):
            curr_val = ord(s[index])-ord('a')
            final_val = ord('a')+(curr_val+p_sum[index])%26
            res+=chr(final_val)

        return res

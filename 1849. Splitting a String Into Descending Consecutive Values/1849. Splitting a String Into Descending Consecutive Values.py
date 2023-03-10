class Solution:
    def splitString(self, s: str) -> bool:

        return self.helper(s,0,0,-1)


    def helper(self,s,index,satisfied,prev_val):
        
        if(index == len(s)):
            return satisfied >=2
        bk = prev_val
        for i in range(index,len(s)):
            curr_val =  int(s[index:i+1])
            if(prev_val == -1 or curr_val == prev_val-1 ):
                prev_val = curr_val
                if(self.helper(s,i+1,satisfied+1,prev_val)):
                    return True
            prev_val = bk
        return False

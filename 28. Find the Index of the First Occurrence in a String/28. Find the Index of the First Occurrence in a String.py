class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        lps = self.get_LPS(needle)
        answer,j,index = -1,0,0
        while(index<len(haystack)):

            char=haystack[index]
            if(needle[j]==char):
                j+=1
                if(j==len(needle)):
                    answer = index-(len(needle)-1)
                    break
                index+=1
            elif( index==0 or j==0):
                j=0
                index+=1
            else:
                j = lps[j-1]

        return answer

    def get_LPS(self,pattern):

        lps = [0]*len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
                    
        return lps

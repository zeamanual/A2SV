class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        answer = 1
        temp = a
        while(len(a)<len(b)):
            answer+=1
            a+=temp

        if(self.search(a,b)):
            return answer
        else:
            a+=temp
            answer+=1
            if(self.search(a,b)):
                return answer
            else:
                return -1

        
    def search(self, original: str, pattern: str) -> int:
        
        lps = self.get_LPS(pattern)
        answer,j,index = -1,0,0
        while(index<len(original)):

            char=original[index]
            if(pattern[j]==char):
                j+=1
                if(j==len(pattern)):
                    answer = index-(len(pattern)-1)
                    break
                index+=1
            elif( index==0 or j==0):
                j=0
                index+=1
            else:
                j = lps[j-1]

        return True if answer!=-1 else False

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

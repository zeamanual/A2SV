class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len=len(word1)
        word1_ptr=0
        word2_len = len(word2)
        word2_ptr=0
        count =0
        result =''
        while(word1_ptr<word1_len or word2_ptr<word2_len):
            if(count%2==0 and word1_ptr<word1_len ):
                result+=word1[word1_ptr]
                word1_ptr+=1
            elif( count%2!=0 and word2_ptr<word2_len):
                result+=word2[word2_ptr]
                word2_ptr+=1      
            count+=1
        return result

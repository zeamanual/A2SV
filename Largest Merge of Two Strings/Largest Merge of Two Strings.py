class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        ptr_one = 0
        ptr_two = 0
        merge=[]

        while(ptr_one < len(word1) and ptr_two < len(word2)):
            if(word1[ptr_one:]>=word2[ptr_two:]):
                merge.append(word1[ptr_one])
                ptr_one+=1
            else:
                merge.append(word2[ptr_two])
                ptr_two+=1

        while(ptr_one < len(word1)):
                merge.append(word1[ptr_one])
                ptr_one+=1      

        while(ptr_two < len(word2)):
                merge.append(word2[ptr_two])
                ptr_two+=1    
                
        return ''.join(merge)   

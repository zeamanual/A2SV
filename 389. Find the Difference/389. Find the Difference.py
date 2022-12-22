class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic= {}
        for char in s:
            dic[char]=dic.get(char,0)+1
        for char in t:
            if(dic.get(char)!=None):
                dic[char]=dic.get(char)-1
            else:
                return char
        
        for char,val in dic.items():
            if (val==-1):
                return char

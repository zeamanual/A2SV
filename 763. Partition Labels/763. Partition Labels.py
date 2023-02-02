class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurences = {}

        for index,value in enumerate(s):
            last_occurences[value]=index

        farthest=0
        answer=[]
        size=0
        for index,char in enumerate(s):
            size+=1
            if(last_occurences[char]>farthest):
                farthest=last_occurences[char]
                
            if(index==farthest):
                answer.append(size)
                size=0


        return answer

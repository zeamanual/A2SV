class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        for index in range(len(words)):
            words[index]=self.f(words[index])

        words.sort(reverse=True)
        answer = []

        for query in queries:
            curr_val = self.f(query)
            count,left,right=0,0,len(words)-1
            while(left<=right):
                mid = left + (right-left)//2
                if(curr_val < words[mid]):
                    left=mid+1
                    count=mid+1
                else:
                    right=mid-1
                    
            answer.append(count)

        return answer
                
    def f(self,s):

        s=sorted(s)
        smallest_char = s[0]
        counter = Counter(s)
        return counter[smallest_char]

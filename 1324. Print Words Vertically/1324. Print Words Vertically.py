class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        words_len = len(words)

        # finding the longest word
        longest=0
        for word in words:
            longest=max(longest,len(word))

        answer=['' for i in range(longest)]
        for word in words:
            max_index=len(word)-1
            for i in range(longest):
                if(i<=max_index):
                    answer[i]+=word[i]
                else:
                    answer[i]+=' '
        
        # removing tralling spaces
        answer = map(lambda word : word.rstrip(),answer)

        return answer

class Solution:
    def longestWord(self, words: List[str]) -> str:

        words_set = set()
        for word in words:
            words_set.add(word)
 
        answer=''
        for word in words:
            is_valid=True
            for index in range(len(word)):
                
                if(word[:index+1] not in words_set):
                    is_valid=False
                    break

            answer = word if is_valid and (len(word)>len(answer) or (len(word)==len(answer) and word<answer)) else answer

        return answer

class Solution:
    def similarPairs(self, words: List[str]) -> int:

        words_len = len(words)
        similar_words=0
        for i in range(words_len):
            current_word=set(words[i])
            for j in range(i+1,words_len):
                if(current_word==set(words[j])):
                    similar_words+=1
            
        return similar_words
                    

            
            

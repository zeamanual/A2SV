class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        words_len =len(words)
        is_sorted=True
        if(words_len<=1):
            return True
        char_order= self.get_char_order_dictionary(order)
        # print(char_order)
        for i in range(words_len-1):
            are_sorted=self.compare_words(words[i],words[i+1],char_order)
            # print(words[i],words[i+1],are_sorted)
            if(not are_sorted):
                is_sorted=False
                break
        return is_sorted
    def compare_words(self,word1,word2,char_order):
        word1_ptr=0
        word1_len = len(word1)
        word2_ptr=0
        word2_len = len(word2)
        are_sorted=True

        while(word2_ptr < word2_len or word1_ptr < word1_len ):
            if(word1_ptr == word1_len  ):
                break
            if(word2_ptr == word2_len):
                are_sorted=False
                break
            if(char_order[word1[word1_ptr]]<char_order[word2[word2_ptr]]):
                break
            elif(char_order[word1[word1_ptr]]>char_order[word2[word2_ptr]]):
                are_sorted=False
                break
            word1_ptr+=1
            word2_ptr+=1

        return are_sorted



    def get_char_order_dictionary(self,order):
        char_order= {}
        order_length=len(order)
        for char_index in range(order_length):
            char_order[order[char_index]]=char_index  
        return char_order     

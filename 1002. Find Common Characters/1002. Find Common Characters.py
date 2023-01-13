class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        char_dic={}
        common_chars=[]
        words_count=len(words)

        for word in words:
            char_frq={}
            for char in word:
                char_frq[char]=char_frq.get(char,0)+1
                key_name=f'{char_frq.get(char,0)}{char}'
                char_dic[key_name]=char_dic.get(key_name,0)+1
                if(char_dic[key_name]>=words_count):
                    while(char_dic[key_name]>=words_count):
                        common_chars.append(char)
                        char_dic[key_name]-=words_count

        return common_chars

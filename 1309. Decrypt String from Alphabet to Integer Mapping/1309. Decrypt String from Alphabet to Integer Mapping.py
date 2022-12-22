class Solution:
    def freqAlphabets(self, s: str) -> str:
        dec_dic = {}
        for i in range(26):
            if(i<=8):
                dec_dic[f'{i+1}']=chr(97+i)
            else:
                dec_dic[f'{i+1}#']=chr(97+i)
        stack = []
        decrypted = ''
        current_index=len(s)-1
        while(current_index>=0):
            if(s[current_index]=='#'):
                single_code =f'{s[current_index-2]}{s[current_index-1]}#'
                decrypted=dec_dic[single_code]+decrypted
                current_index-=3
            else:
                decrypted=dec_dic[s[current_index]]+decrypted
                current_index-=1
        return decrypted
        

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_masks = []

        for word in words:
            bit_mask = 0
            for char in word:
                bit_mask = bit_mask | 1 << ord(char)-ord('a')
            bit_masks.append(bit_mask)

            
        max_len=0
        for curr_word in range(len(words)):
            for ptr in range(curr_word+1,len(words)):
                if(bit_masks[curr_word] & bit_masks[ptr] == 0):
                    max_len=max(max_len,len(words[curr_word]) * len(words[ptr]) )

        return max_len

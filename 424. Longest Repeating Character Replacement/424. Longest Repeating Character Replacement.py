class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
        freq = [0] *26
        size = len(s)
        highest_freq=0
        longest=0

        left_ptr =0
        right_ptr=0
        while(right_ptr<size):
            freq[ord(s[right_ptr])-ord('A')]+=1
            highest_freq = max(freq)

            chars_to_change = right_ptr - left_ptr + 1 -highest_freq
            if(chars_to_change > k):
                freq[ord(s[left_ptr])-ord('A')]-=1
                left_ptr+=1
            
            longest=max(longest,right_ptr - left_ptr  + 1)
            right_ptr+=1

        return longest

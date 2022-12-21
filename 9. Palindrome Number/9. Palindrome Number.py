class Solution:
    def isPalindrome(self, x: int) -> bool:
        left_ptr = 0
        right_ptr = len(str(x))-1
        x_in_words=str(x)
        while(left_ptr<=right_ptr):
            if(x_in_words[left_ptr]!=x_in_words[right_ptr]):
                return False
            left_ptr+=1
            right_ptr-=1
        
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=''
        # removing non-alphanumeric characters
        for char in s:
            if (char.isalnum()):
                new_s+=char.lower()

        left_ptr =0
        right_ptr=len(new_s)-1
        while(left_ptr<=right_ptr):
            if(new_s[left_ptr]!=new_s[right_ptr]):
                return False
            right_ptr-=1
            left_ptr+=1
        return True

        

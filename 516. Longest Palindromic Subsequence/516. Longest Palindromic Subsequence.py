class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def is_palindrome(string):
            return string[0:len(string)//2]==string[:ceil(len(string)/2)-1:-1]

        @lru_cache(None)
        def helper(left_ptr,right_ptr):

            if(left_ptr == right_ptr):
                return 1
            elif(left_ptr>right_ptr):
                return 0

            if(s[left_ptr]==s[right_ptr]):
                return 2 + helper(left_ptr+1,right_ptr-1)
            else:
                return max(helper(left_ptr+1,right_ptr),helper(left_ptr,right_ptr-1))

        return helper(0,len(s)-1)

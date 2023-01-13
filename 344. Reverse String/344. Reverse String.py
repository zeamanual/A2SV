class Solution:
    def reverseString(self, s: List[str]) -> None:
        string_len = len(s)
        last_index=string_len-1

        for i in range(string_len//2):
            s[i],s[last_index-i]=s[last_index-i],s[i]
        """
        Do not return anything, modify s in-place instead.
        """

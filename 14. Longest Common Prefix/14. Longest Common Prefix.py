class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if( len(strs)==0 or strs[0]==''):
            return ''
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for j in range(1,len(strs)):
                if( i>=len(strs[j]) or strs[j][i]!=current_char):
                    return strs[0][:i]
        return strs[0]

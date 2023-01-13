class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        col_count = len(strs[0])
        answer=0

        for col in range(col_count):
            current_char = strs[0][col]
            for string in strs:
                if(ord(current_char)<=ord(string[col])):
                    current_char=string[col]
                else:
                    answer+=1
                    break

        return answer


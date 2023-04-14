class Solution:
    def maxLength(self, arr: List[str]) -> int:
    
        def backtrack(start, curr_str):
            if len(set(curr_str)) != len(curr_str):
                return

            nonlocal max_len
            max_len = max(max_len, len(curr_str))
            for i in range(start, len(arr)):
                backtrack(i+1, curr_str + arr[i])

        max_len = 0
        backtrack(0, "")
        return max_len

class Solution:
 def reversePairs(self,nums):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left_arr, left_count = merge_sort(arr[:mid])
        right_arr, right_count = merge_sort(arr[mid:])
        merged_arr, merged_count = merge(left_arr, right_arr)
        return merged_arr, left_count + right_count + merged_count

    def merge(left_arr, right_arr):
        i = j = 0
        count = 0
        merged_arr = []
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= 2 * right_arr[j]:
                i += 1
            else:
                count += len(left_arr) - i
                j += 1
        i = j = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                merged_arr.append(left_arr[i])
                i += 1
            else:
                merged_arr.append(right_arr[j])
                j += 1
        merged_arr += left_arr[i:]
        merged_arr += right_arr[j:]
        return merged_arr, count

    sorted_nums, count = merge_sort(nums)
    return count

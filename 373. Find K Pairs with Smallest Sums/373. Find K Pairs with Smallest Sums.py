class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap = []
        result = []

        def push_sum(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j], i, j))

        push_sum(0, 0)
        added = set()
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            if((i,j) not in added):
                result.append([nums1[i], nums2[j]])
                added.add((i,j))
            push_sum(i, j + 1)
            if j == 0:
                push_sum(i + 1, 0)

        return result

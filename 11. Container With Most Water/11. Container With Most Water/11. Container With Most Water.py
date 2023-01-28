class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_ptr = 0
        right_ptr = len(height) -1
        
        while(left_ptr < right_ptr):
            temp_max_area = (min(height[left_ptr], height[right_ptr])) * (right_ptr - left_ptr)
            if(temp_max_area > max_area):
                max_area = temp_max_area
            
            if(height[left_ptr] < height[right_ptr]):
                left_ptr += 1
            else:
                right_ptr -= 1
        
        return max_area

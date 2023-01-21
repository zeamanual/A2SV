class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        arr_size = len(heights)
        for count in range(arr_size):
            for index in range((arr_size-1)-count):
                if(heights[index]<heights[index+1]):
                    heights[index],heights[index+1]=heights[index+1],heights[index]
                    names[index],names[index+1]=names[index+1],names[index]

        return names

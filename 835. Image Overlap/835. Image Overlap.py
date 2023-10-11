class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        rows,cols = len(img1),len(img1[0])

        img1_one_bits=set()
        img2_one_bits = set()

        for row in range(rows):
            for col in range(cols):

                if(img1[row][col]==1):
                    img1_one_bits.add((row,col))
                if(img2[row][col]==1):
                    img2_one_bits.add((row,col))

        possible_answers = defaultdict(int)
        for img1_one_bit in img1_one_bits:
            for img2_one_bit in img2_one_bits:
                possible_answers[(img1_one_bit[0]-img2_one_bit[0],img1_one_bit[1]-img2_one_bit[1])]+=1

        return max(possible_answers.values()) if possible_answers else 0
